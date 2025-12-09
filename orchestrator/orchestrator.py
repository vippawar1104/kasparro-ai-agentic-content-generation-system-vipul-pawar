"""
Orchestrator - Controls the entire multi-agent workflow
"""

import json
import logging
from typing import Dict, Any
from pathlib import Path

from agents import (
    ProductParserAgent,
    QuestionGeneratorAgent,
    ComparisonAgent,
    TemplateEngineAgent,
    LogicBlocksProcessorAgent,
    PageAssemblyAgent
)

logger = logging.getLogger(__name__)


class Orchestrator:
    """
    Main orchestrator for the multi-agent product content generation system.
    
    Workflow:
    1. Parse raw product data
    2. Generate questions
    3. Create comparison product
    4. Process logic blocks
    5. Apply templates
    6. Assemble pages
    7. Save output files
    """
    
    def __init__(self, output_dir: str = "output"):
        """
        Initialize orchestrator with all agents.
        
        Args:
            output_dir: Directory to save output JSON files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize all agents
        self.product_parser = ProductParserAgent()
        self.question_generator = QuestionGeneratorAgent()
        self.comparison_agent = ComparisonAgent()
        self.template_engine = TemplateEngineAgent()
        self.logic_blocks_processor = LogicBlocksProcessorAgent()
        self.page_assembly = PageAssemblyAgent()
        
        # Store intermediate results
        self.parsed_product = None
        self.questions = None
        self.comparison = None
        self.logic_blocks = None
        
        logger.info("Orchestrator initialized with all agents")
    
    def generate_all_pages(self, raw_product_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main entry point - generates all three pages from raw product data.
        
        Args:
            raw_product_data: Raw product dictionary
            
        Returns:
            Dictionary with paths to all generated files
        """
        logger.info("Starting multi-agent content generation pipeline")
        
        try:
            # Step 1: Parse product data
            parsed_result = self.product_parser.run(raw_product_data)
            if not parsed_result['success']:
                raise Exception(f"Product parsing failed: {parsed_result.get('error')}")
            self.parsed_product = parsed_result['data']
            logger.info("✓ Step 1: Product data parsed")
            
            # Step 2: Generate questions
            questions_result = self.question_generator.run(self.parsed_product)
            if not questions_result['success']:
                raise Exception(f"Question generation failed: {questions_result.get('error')}")
            self.questions = questions_result['data']
            logger.info(f"✓ Step 2: Generated {self.questions['total_count']} questions")
            
            # Step 3: Create comparison
            comparison_result = self.comparison_agent.run(self.parsed_product)
            if not comparison_result['success']:
                raise Exception(f"Comparison generation failed: {comparison_result.get('error')}")
            self.comparison = comparison_result['data']
            logger.info("✓ Step 3: Comparison product created")
            
            # Step 4: Process logic blocks for all pages
            self.logic_blocks = self._process_all_logic_blocks()
            logger.info("✓ Step 4: Logic blocks processed")
            
            # Step 5 & 6: Generate all three pages
            faq_page = self._generate_faq_page()
            product_page = self._generate_product_page()
            comparison_page = self._generate_comparison_page()
            logger.info("✓ Steps 5-6: All pages assembled")
            
            # Step 7: Save outputs
            output_files = self._save_outputs(faq_page, product_page, comparison_page)
            logger.info("✓ Step 7: Output files saved")
            
            results = {
                'success': True,
                'output_files': output_files,
                'statistics': {
                    'total_questions': self.questions['total_count'],
                    'product_name': self.parsed_product['name'],
                    'comparison_product': self.comparison['product_b']['name']
                }
            }
            
            logger.info("Pipeline completed successfully!")
            return results
            
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def _process_all_logic_blocks(self) -> Dict[str, Any]:
        """Process all logic blocks for both products."""
        
        # Blocks for product page
        product_blocks = self.logic_blocks_processor.run({
            'blocks_to_process': [
                'overview_block',
                'skin_type_block',
                'ingredients_block',
                'benefits_block',
                'usage_block',
                'safety_block',
                'pricing_block'
            ],
            'data': self.parsed_product
        })
        
        # Blocks for comparison page
        comparison_blocks = self.logic_blocks_processor.run({
            'blocks_to_process': ['comparison_block'],
            'data': self.comparison
        })
        
        # Merge all blocks
        all_blocks = {}
        if product_blocks['success']:
            all_blocks.update(product_blocks['data']['processed_blocks'])
        if comparison_blocks['success']:
            all_blocks.update(comparison_blocks['data']['processed_blocks'])
        
        return all_blocks
    
    def _generate_faq_page(self) -> Dict[str, Any]:
        """Generate FAQ page."""
        
        faq_result = self.page_assembly.run({
            'page_type': 'faq',
            'data': self.parsed_product,
            'logic_blocks': self.logic_blocks,
            'questions': self.questions
        })
        
        if not faq_result['success']:
            raise Exception(f"FAQ page assembly failed: {faq_result.get('error')}")
        
        return faq_result['data']
    
    def _generate_product_page(self) -> Dict[str, Any]:
        """Generate product description page."""
        
        product_result = self.page_assembly.run({
            'page_type': 'product',
            'data': self.parsed_product,
            'logic_blocks': self.logic_blocks,
            'template': None
        })
        
        if not product_result['success']:
            raise Exception(f"Product page assembly failed: {product_result.get('error')}")
        
        return product_result['data']
    
    def _generate_comparison_page(self) -> Dict[str, Any]:
        """Generate comparison page."""
        
        comparison_result = self.page_assembly.run({
            'page_type': 'comparison',
            'data': self.comparison,
            'logic_blocks': self.logic_blocks,
            'template': None
        })
        
        if not comparison_result['success']:
            raise Exception(f"Comparison page assembly failed: {comparison_result.get('error')}")
        
        return comparison_result['data']
    
    def _save_outputs(
        self,
        faq_page: Dict[str, Any],
        product_page: Dict[str, Any],
        comparison_page: Dict[str, Any]
    ) -> Dict[str, str]:
        """Save all output files."""
        
        output_files = {}
        
        # Save FAQ page
        faq_path = self.output_dir / "faq.json"
        with open(faq_path, 'w', encoding='utf-8') as f:
            json.dump(faq_page, f, indent=2, ensure_ascii=False)
        output_files['faq'] = str(faq_path)
        logger.info(f"Saved FAQ page to {faq_path}")
        
        # Save product page
        product_path = self.output_dir / "product_page.json"
        with open(product_path, 'w', encoding='utf-8') as f:
            json.dump(product_page, f, indent=2, ensure_ascii=False)
        output_files['product'] = str(product_path)
        logger.info(f"Saved product page to {product_path}")
        
        # Save comparison page
        comparison_path = self.output_dir / "comparison_page.json"
        with open(comparison_path, 'w', encoding='utf-8') as f:
            json.dump(comparison_page, f, indent=2, ensure_ascii=False)
        output_files['comparison'] = str(comparison_path)
        logger.info(f"Saved comparison page to {comparison_path}")
        
        return output_files
    
    def get_workflow_status(self) -> Dict[str, Any]:
        """Get current workflow status."""
        return {
            'product_parsed': self.parsed_product is not None,
            'questions_generated': self.questions is not None,
            'comparison_created': self.comparison is not None,
            'logic_blocks_processed': self.logic_blocks is not None
        }
