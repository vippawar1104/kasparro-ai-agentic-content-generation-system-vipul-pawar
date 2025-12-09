"""
Question Generator Agent
Generates 15+ user questions categorized by type from product data
"""

from typing import Dict, Any, List
from agents.base_agent import BaseAgent
import logging

logger = logging.getLogger(__name__)


class QuestionGeneratorAgent(BaseAgent):
    """
    Agent responsible for generating user questions from product data.
    
    Input: Structured product data
    Output: 15+ categorized questions
    
    Categories:
    - Informational (what is this?)
    - Usage (how to use?)
    - Safety (side effects?)
    - Purchase (pricing?)
    - Comparison (vs others?)
    """
    
    REQUIRED_CATEGORIES = [
        'informational',
        'usage',
        'safety',
        'purchase',
        'comparison'
    ]
    
    MIN_QUESTIONS = 15
    
    def __init__(self):
        super().__init__(
            agent_id="question_generator_001",
            agent_type="question_generator"
        )
    
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """Validate that product data is present."""
        if not isinstance(input_data, dict):
            return False
        
        required = ['name', 'ingredients', 'benefits', 'usage']
        return all(key in input_data for key in required)
    
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate categorized questions from product data.
        
        Args:
            input_data: Structured product data
            
        Returns:
            Dictionary with categorized questions
        """
        logger.info("Generating questions from product data...")
        
        questions = {
            'informational': self._generate_informational_questions(input_data),
            'usage': self._generate_usage_questions(input_data),
            'safety': self._generate_safety_questions(input_data),
            'purchase': self._generate_purchase_questions(input_data),
            'comparison': self._generate_comparison_questions(input_data)
        }
        
        # Flatten for total count
        all_questions = []
        for category, q_list in questions.items():
            for q in q_list:
                all_questions.append({
                    'question': q,
                    'category': category
                })
        
        result = {
            'questions_by_category': questions,
            'all_questions': all_questions,
            'total_count': len(all_questions),
            'category_counts': {
                cat: len(q_list) for cat, q_list in questions.items()
            }
        }
        
        logger.info(f"Generated {result['total_count']} questions across {len(questions)} categories")
        
        return result
    
    def _generate_informational_questions(self, product: Dict[str, Any]) -> List[str]:
        """Generate informational questions."""
        questions = []
        
        name = product.get('name', 'this product')
        ingredients = product.get('ingredients', {})
        benefits = product.get('benefits', {})
        concentration = product.get('concentration', {})
        
        # Basic product questions
        questions.append(f"What is {name}?")
        questions.append(f"What are the key ingredients in {name}?")
        
        # Ingredient questions
        if ingredients.get('list'):
            primary = ingredients['list'][0]
            questions.append(f"What is {primary} and how does it work?")
            questions.append(f"What does {concentration.get('display', 'the concentration')} mean?")
        
        # Benefit questions
        if benefits.get('list'):
            questions.append(f"What are the main benefits of {name}?")
            questions.append("How does this product improve skin health?")
        
        return questions
    
    def _generate_usage_questions(self, product: Dict[str, Any]) -> List[str]:
        """Generate usage-related questions."""
        questions = []
        
        name = product.get('name', 'this product')
        skin_type = product.get('skin_type', {})
        usage = product.get('usage', {})
        
        # Basic usage
        questions.append(f"How do I use {name}?")
        questions.append("When should I apply this product?")
        questions.append(f"How often should I use {name}?")
        
        # Skin type specific
        if skin_type.get('all_types'):
            types = skin_type['all_types']
            if len(types) > 1:
                questions.append(f"Can I use this product if I have {types[0]} skin?")
            else:
                questions.append("Is this suitable for all skin types?")
        
        # Application
        questions.append("Should I use this in my morning or evening routine?")
        
        return questions
    
    def _generate_safety_questions(self, product: Dict[str, Any]) -> List[str]:
        """Generate safety and side effect questions."""
        questions = []
        
        name = product.get('name', 'this product')
        safety = product.get('safety', {})
        
        # General safety
        questions.append(f"What are the side effects of {name}?")
        questions.append("Is this product safe for sensitive skin?")
        questions.append("Can I use this product during pregnancy?")
        
        # Side effects
        if safety.get('side_effects'):
            questions.append("What should I do if I experience irritation?")
            questions.append("Are there any precautions I should take?")
        
        return questions
    
    def _generate_purchase_questions(self, product: Dict[str, Any]) -> List[str]:
        """Generate purchase and pricing questions."""
        questions = []
        
        name = product.get('name', 'this product')
        pricing = product.get('pricing', {})
        
        # Pricing
        questions.append(f"How much does {name} cost?")
        questions.append("What is the price of this product?")
        questions.append("Is this product worth the price?")
        
        # Value
        if pricing.get('value'):
            questions.append("How long will one bottle last?")
        
        return questions
    
    def _generate_comparison_questions(self, product: Dict[str, Any]) -> List[str]:
        """Generate comparison questions"""
        questions = []
        
        name = product.get('name', 'this product')
        ingredients = product.get('ingredients', {})
        concentration = product.get('concentration', {})
        
        # General comparisons
        questions.append(f"How is {name} different from other similar products?")
        questions.append("What makes this product unique?")
        
        # Ingredient comparisons
        if ingredients.get('primary'):
            primary = ingredients['primary']
            questions.append(f"Is {primary} better than other active ingredients?")
        
        # Concentration
        if concentration.get('percentage'):
            questions.append("Is a higher concentration always better?")
        
        questions.append("Should I use this product alone or with other serums?")
        
        return questions
