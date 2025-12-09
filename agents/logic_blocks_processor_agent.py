"""
Logic Blocks Processor Agent
Executes reusable content logic blocks
"""

from typing import Dict, Any
from agents.base_agent import BaseAgent
import logging

# Import all logic blocks
from logic_blocks import (
    BenefitsBlock,
    UsageBlock,
    IngredientsBlock,
    SafetyBlock,
    PricingBlock,
    ComparisonBlock,
    OverviewBlock,
    SkinTypeBlock
)

logger = logging.getLogger(__name__)


class LogicBlocksProcessorAgent(BaseAgent):
    """
    Agent responsible for processing logic blocks.
    
    Input: Block IDs + data
    Output: Processed content blocks
    
    Available Blocks:
    - benefits_block
    - usage_block
    - ingredients_block
    - safety_block
    - pricing_block
    - comparison_block
    """
    
    def __init__(self):
        super().__init__(
            agent_id="logic_blocks_processor_001",
            agent_type="logic_blocks_processor"
        )
    
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """Validate input has blocks to process."""
        return 'blocks_to_process' in input_data and 'data' in input_data
    
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process all requested logic blocks.
        
        Args:
            input_data: {
                'blocks_to_process': list of block names,
                'data': product data
            }
            
        Returns:
            Dictionary of processed blocks
        """
        blocks_to_process = input_data['blocks_to_process']
        data = input_data['data']
        
        logger.info(f"Processing {len(blocks_to_process)} logic blocks")
        
        processed_blocks = {}
        
        for block_name in blocks_to_process:
            try:
                block_result = self._process_block(block_name, data)
                processed_blocks[block_name] = block_result
            except Exception as e:
                logger.error(f"Error processing block {block_name}: {str(e)}")
                processed_blocks[block_name] = {
                    'error': str(e),
                    'success': False
                }
        
        return {
            'processed_blocks': processed_blocks,
            'total_blocks': len(blocks_to_process),
            'successful_blocks': sum(
                1 for b in processed_blocks.values() 
                if b.get('success', True)
            )
        }
    
    def _process_block(self, block_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process a single logic block using modular block classes."""
        
        block_map = {
            'benefits_block': BenefitsBlock,
            'usage_block': UsageBlock,
            'ingredients_block': IngredientsBlock,
            'safety_block': SafetyBlock,
            'pricing_block': PricingBlock,
            'comparison_block': ComparisonBlock,
            'overview_block': OverviewBlock,
            'skin_type_block': SkinTypeBlock,
        }
        
        block_class = block_map.get(block_name)
        if not block_class:
            raise ValueError(f"Unknown block: {block_name}")
        
        return block_class.execute(data)
