"""
Page Assembly Agent
Combines templates, logic blocks, and data to produce final JSON pages
"""

from typing import Dict, Any, List
from agents.base_agent import BaseAgent
import logging

logger = logging.getLogger(__name__)


class PageAssemblyAgent(BaseAgent):
    """
    Agent responsible for assembling final page outputs.
    
    Input: Template + Logic Blocks + Data
    Output: Complete JSON page
    
    Produces:
    - FAQ Page
    - Product Page
    - Comparison Page
    """
    
    def __init__(self):
        super().__init__(
            agent_id="page_assembly_001",
            agent_type="page_assembly"
        )
    
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """Validate input has required components."""
        required = ['page_type', 'data', 'logic_blocks']
        return all(key in input_data for key in required)
    
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assemble final page from components.
        
        Args:
            input_data: {
                'page_type': 'faq'|'product'|'comparison',
                'data': product/comparison data,
                'logic_blocks': processed logic blocks,
                'template': populated template (optional),
                'questions': questions data (for FAQ)
            }
            
        Returns:
            Complete JSON page
        """
        page_type = input_data['page_type']
        data = input_data['data']
        logic_blocks = input_data['logic_blocks']
        questions = input_data.get('questions', {})
        
        logger.info(f"Assembling {page_type} page")
        
        if page_type == 'faq':
            page = self._assemble_faq_page(data, questions, logic_blocks)
        elif page_type == 'product':
            page = self._assemble_product_page(data, logic_blocks)
        elif page_type == 'comparison':
            page = self._assemble_comparison_page(data, logic_blocks)
        else:
            raise ValueError(f"Unknown page type: {page_type}")
        
        logger.info(f"Successfully assembled {page_type} page")
        
        return page
    
    def _assemble_faq_page(
        self,
        product_data: Dict[str, Any],
        questions_data: Dict[str, Any],
        logic_blocks: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Assemble FAQ page."""
        
        all_questions = questions_data.get('all_questions', [])
        product_name = product_data.get('name', 'Product')
        
        # Generate answers using data and logic blocks
        faqs = []
        for q_item in all_questions[:15]:  # Limit to 15 questions
            question = q_item['question']
            category = q_item['category']
            
            answer = self._generate_answer(
                question,
                category,
                product_data,
                logic_blocks
            )
            
            faqs.append({
                'question': question,
                'answer': answer,
                'category': category
            })
        
        # Group by category
        faqs_by_category = {}
        for faq in faqs:
            cat = faq['category']
            if cat not in faqs_by_category:
                faqs_by_category[cat] = []
            faqs_by_category[cat].append({
                'question': faq['question'],
                'answer': faq['answer']
            })
        
        page = {
            'page_type': 'faq',
            'product_name': product_name,
            'title': f'{product_name} - Frequently Asked Questions',
            'total_questions': len(faqs),
            'faqs': faqs,
            'faqs_by_category': faqs_by_category,
            'metadata': {
                'generated_at': self._get_timestamp(),
                'version': '1.0',
                'categories': list(faqs_by_category.keys())
            }
        }
        
        return page
    
    def _assemble_product_page(
        self,
        product_data: Dict[str, Any],
        logic_blocks: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Assemble product description page."""
        
        overview = logic_blocks.get('overview_block', {})
        skin_type = logic_blocks.get('skin_type_block', {})
        ingredients = logic_blocks.get('ingredients_block', {})
        benefits = logic_blocks.get('benefits_block', {})
        usage = logic_blocks.get('usage_block', {})
        safety = logic_blocks.get('safety_block', {})
        pricing = logic_blocks.get('pricing_block', {})
        
        page = {
            'page_type': 'product',
            'product_id': product_data.get('product_id'),
            'product_name': product_data.get('name'),
            
            'overview': {
                'title': overview.get('title', 'Overview'),
                'description': overview.get('overview_text', ''),
                'key_points': overview.get('key_points', []),
                'concentration': overview.get('concentration', '')
            },
            
            'skin_type': {
                'title': skin_type.get('title', 'Suitable For'),
                'primary': skin_type.get('primary_skin_type', ''),
                'all_types': skin_type.get('all_skin_types', []),
                'description': skin_type.get('suitability_text', '')
            },
            
            'ingredients': {
                'title': ingredients.get('title', 'Key Ingredients'),
                'list': ingredients.get('ingredients', []),
                'primary_ingredient': ingredients.get('primary_ingredient', ''),
                'total_count': ingredients.get('count', 0),
                'summary': ingredients.get('ingredient_summary', '')
            },
            
            'benefits': {
                'title': benefits.get('title', 'Benefits'),
                'list': benefits.get('benefits', []),
                'categorized': benefits.get('categorized_benefits', {}),
                'summary': benefits.get('summary', '')
            },
            
            'usage': {
                'title': usage.get('title', 'How to Use'),
                'steps': usage.get('steps', []),
                'frequency': usage.get('frequency', ''),
                'quick_guide': usage.get('quick_guide', ''),
                'full_instructions': usage.get('full_instructions', '')
            },
            
            'safety': {
                'title': safety.get('title', 'Safety Information'),
                'side_effects': safety.get('side_effects', []),
                'warnings': safety.get('warnings', []),
                'severity': safety.get('severity', ''),
                'summary': safety.get('safety_summary', '')
            },
            
            'pricing': {
                'title': pricing.get('title', 'Pricing'),
                'price': pricing.get('display_price', ''),
                'formatted_price': pricing.get('price', ''),
                'value_proposition': pricing.get('value_proposition', ''),
                'summary': pricing.get('pricing_summary', '')
            },
            
            'metadata': {
                'generated_at': self._get_timestamp(),
                'version': '1.0',
                'data_source': 'product_parser'
            }
        }
        
        return page
    
    def _assemble_comparison_page(
        self,
        comparison_data: Dict[str, Any],
        logic_blocks: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Assemble comparison page."""
        
        comparison_block = logic_blocks.get('comparison_block', {})
        
        product_a = comparison_data.get('product_a', {})
        product_b = comparison_data.get('product_b', {})
        comparison = comparison_data.get('comparison', {})
        
        page = {
            'page_type': 'comparison',
            'title': f"{product_a.get('name', 'Product A')} vs {product_b.get('name', 'Product B')}",
            
            'products': {
                'product_a': {
                    'name': product_a.get('name'),
                    'id': product_a.get('product_id'),
                    'concentration': product_a.get('concentration', {}).get('display'),
                    'price': product_a.get('pricing', {}).get('formatted')
                },
                'product_b': {
                    'name': product_b.get('name'),
                    'id': product_b.get('product_id'),
                    'concentration': product_b.get('concentration', {}).get('display'),
                    'price': product_b.get('pricing', {}).get('formatted')
                }
            },
            
            'comparison': {
                'concentration': {
                    'product_a': comparison.get('concentration', {}).get('product_a'),
                    'product_b': comparison.get('concentration', {}).get('product_b'),
                    'analysis': comparison.get('concentration', {}).get('difference')
                },
                
                'ingredients': {
                    'product_a': comparison.get('ingredients', {}).get('product_a', []),
                    'product_b': comparison.get('ingredients', {}).get('product_b', []),
                    'common_ingredients': comparison.get('ingredients', {}).get('common', []),
                    'unique_to_a': comparison.get('ingredients', {}).get('unique_to_a', []),
                    'unique_to_b': comparison.get('ingredients', {}).get('unique_to_b', [])
                },
                
                'benefits': {
                    'product_a': comparison.get('benefits', {}).get('product_a', []),
                    'product_b': comparison.get('benefits', {}).get('product_b', []),
                    'analysis': comparison.get('benefits', {}).get('comparison')
                },
                
                'pricing': {
                    'product_a': comparison.get('pricing', {}).get('product_a'),
                    'product_b': comparison.get('pricing', {}).get('product_b'),
                    'price_difference': comparison.get('pricing', {}).get('difference'),
                    'value_assessment': comparison.get('pricing', {}).get('value_assessment')
                }
            },
            
            'summary': comparison_data.get('summary', ''),
            'recommendation': comparison_block.get('recommendation', ''),
            
            'metadata': {
                'generated_at': self._get_timestamp(),
                'version': '1.0',
                'comparison_type': 'side_by_side'
            }
        }
        
        return page
    
    def _generate_answer(
        self,
        question: str,
        category: str,
        product_data: Dict[str, Any],
        logic_blocks: Dict[str, Any]
    ) -> str:
        """Generate answer to a question based on product data."""
        
        question_lower = question.lower()
        
        # Extract relevant data based on question keywords
        if 'what is' in question_lower or 'what are' in question_lower:
            if 'ingredient' in question_lower:
                ingredients = logic_blocks.get('ingredients_block', {})
                return ingredients.get('ingredient_summary', 'Information not available.')
            elif 'benefit' in question_lower:
                benefits = logic_blocks.get('benefits_block', {})
                return benefits.get('summary', 'Information not available.')
            else:
                overview = logic_blocks.get('overview_block', {})
                return overview.get('overview_text', 'Information not available.')
        
        elif 'how' in question_lower:
            if 'use' in question_lower or 'apply' in question_lower:
                usage = logic_blocks.get('usage_block', {})
                return usage.get('quick_guide', 'Follow product instructions.')
            elif 'often' in question_lower:
                usage = logic_blocks.get('usage_block', {})
                return f"Use {usage.get('frequency', 'as directed')}."
        
        elif 'price' in question_lower or 'cost' in question_lower:
            pricing = logic_blocks.get('pricing_block', {})
            return pricing.get('pricing_summary', 'Pricing information not available.')
        
        elif 'side effect' in question_lower or 'safe' in question_lower:
            safety = logic_blocks.get('safety_block', {})
            return safety.get('safety_summary', 'Consult product safety information.')
        
        elif 'skin type' in question_lower:
            skin_type = logic_blocks.get('skin_type_block', {})
            return skin_type.get('suitability_text', 'Suitable for most skin types.')
        
        # Default answer based on category
        return self._get_default_answer(category, product_data)
    
    def _get_default_answer(
        self,
        category: str,
        product_data: Dict[str, Any]
    ) -> str:
        """Get a default answer based on category."""
        
        name = product_data.get('name', 'this product')
        
        if category == 'informational':
            return f"{name} is a skin care product formulated with quality ingredients."
        elif category == 'usage':
            return "Follow the usage instructions provided with the product."
        elif category == 'safety':
            return "Perform a patch test before use and discontinue if irritation occurs."
        elif category == 'purchase':
            return "Check the product pricing information for current costs."
        elif category == 'comparison':
            return f"{name} offers unique benefits compared to similar products."
        else:
            return "For more information, please refer to the product documentation."
    
    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()
