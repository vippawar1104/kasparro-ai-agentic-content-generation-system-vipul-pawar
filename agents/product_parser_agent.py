"""
Product Parser Agent
Cleans and converts raw product data into structured internal JSON
"""

from typing import Dict, Any
from agents.base_agent import BaseAgent
import logging

logger = logging.getLogger(__name__)


class ProductParserAgent(BaseAgent):
    """
    Agent responsible for parsing and structuring raw product data.
    
    Input: Raw product dictionary
    Output: Cleaned, validated, structured product JSON
    """
    
    # Required product fields
    REQUIRED_FIELDS = [
        'product_name',
        'concentration',
        'skin_type',
        'key_ingredients',
        'benefits',
        'usage_instructions',
        'side_effects',
        'price'
    ]
    
    def __init__(self):
        super().__init__(agent_id="product_parser_001", agent_type="product_parser")
    
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """
        Validate that all required product fields are present.
        
        Args:
            input_data: Raw product data
            
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(input_data, dict):
            logger.error("Input data must be a dictionary")
            return False
        
        missing_fields = [
            field for field in self.REQUIRED_FIELDS 
            if field not in input_data
        ]
        
        if missing_fields:
            logger.error(f"Missing required fields: {missing_fields}")
            return False
        
        return True
    
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse and structure the product data.
        
        Args:
            input_data: Raw product dictionary
            
        Returns:
            Structured product JSON
        """
        logger.info("Parsing product data...")
        
        # Clean and structure the data
        structured_product = {
            'product_id': self._generate_product_id(input_data['product_name']),
            'name': self._clean_text(input_data['product_name']),
            'concentration': self._parse_concentration(input_data['concentration']),
            'skin_type': self._parse_skin_type(input_data['skin_type']),
            'ingredients': self._parse_ingredients(input_data['key_ingredients']),
            'benefits': self._parse_benefits(input_data['benefits']),
            'usage': self._parse_usage(input_data['usage_instructions']),
            'safety': self._parse_safety(input_data['side_effects']),
            'pricing': self._parse_pricing(input_data['price']),
            'metadata': {
                'parsed_at': self._get_timestamp(),
                'data_source': 'raw_input',
                'version': '1.0'
            }
        }
        
        logger.info(f"Successfully parsed product: {structured_product['name']}")
        
        return structured_product
    
    def _generate_product_id(self, name: str) -> str:
        """Generate a unique product ID from name."""
        return name.lower().replace(' ', '_').replace('-', '_')
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize text."""
        if isinstance(text, list):
            text = ', '.join(text)
        return str(text).strip()
    
    def _parse_concentration(self, concentration: str) -> Dict[str, Any]:
        """Parse concentration information."""
        cleaned = self._clean_text(concentration)
        
        # Extract numeric value if present
        import re
        numbers = re.findall(r'\d+\.?\d*', cleaned)
        percentage = float(numbers[0]) if numbers else None
        
        return {
            'value': cleaned,
            'percentage': percentage,
            'display': cleaned
        }
    
    def _parse_skin_type(self, skin_type: str) -> Dict[str, Any]:
        """Parse skin type information."""
        if isinstance(skin_type, str):
            types = [t.strip() for t in skin_type.split(',')]
        else:
            types = skin_type if isinstance(skin_type, list) else [str(skin_type)]
        
        return {
            'primary': types[0] if types else 'All skin types',
            'all_types': types,
            'count': len(types)
        }
    
    def _parse_ingredients(self, ingredients: Any) -> Dict[str, Any]:
        """Parse ingredients list."""
        if isinstance(ingredients, str):
            ingredient_list = [
                ing.strip() for ing in ingredients.split(',')
            ]
        elif isinstance(ingredients, list):
            ingredient_list = ingredients
        else:
            ingredient_list = [str(ingredients)]
        
        return {
            'list': ingredient_list,
            'count': len(ingredient_list),
            'primary': ingredient_list[0] if ingredient_list else None,
            'formatted': ', '.join(ingredient_list)
        }
    
    def _parse_benefits(self, benefits: Any) -> Dict[str, Any]:
        """Parse benefits information."""
        if isinstance(benefits, str):
            benefit_list = [
                b.strip() for b in benefits.split(',')
                if b.strip()
            ]
        elif isinstance(benefits, list):
            benefit_list = benefits
        else:
            benefit_list = [str(benefits)]
        
        return {
            'list': benefit_list,
            'count': len(benefit_list),
            'primary': benefit_list[0] if benefit_list else None,
            'categories': self._categorize_benefits(benefit_list)
        }
    
    def _categorize_benefits(self, benefits: list) -> Dict[str, list]:
        """Categorize benefits by type."""
        categories = {
            'treatment': [],
            'prevention': [],
            'enhancement': [],
            'general': []
        }
        
        treatment_keywords = ['treat', 'reduce', 'fade', 'remove', 'clear']
        prevention_keywords = ['prevent', 'protect', 'shield', 'guard']
        enhancement_keywords = ['improve', 'boost', 'enhance', 'brighten']
        
        for benefit in benefits:
            benefit_lower = benefit.lower()
            if any(kw in benefit_lower for kw in treatment_keywords):
                categories['treatment'].append(benefit)
            elif any(kw in benefit_lower for kw in prevention_keywords):
                categories['prevention'].append(benefit)
            elif any(kw in benefit_lower for kw in enhancement_keywords):
                categories['enhancement'].append(benefit)
            else:
                categories['general'].append(benefit)
        
        return categories
    
    def _parse_usage(self, usage: Any) -> Dict[str, Any]:
        """Parse usage instructions."""
        if isinstance(usage, str):
            instructions = usage
        elif isinstance(usage, list):
            instructions = ' '.join(usage)
        else:
            instructions = str(usage)
        
        # Try to extract steps
        steps = self._extract_steps(instructions)
        
        return {
            'full_instructions': instructions,
            'steps': steps,
            'step_count': len(steps),
            'frequency': self._extract_frequency(instructions)
        }
    
    def _extract_steps(self, text: str) -> list:
        """Extract numbered or bulleted steps from text."""
        import re
        
        # Try to find numbered steps
        numbered = re.findall(r'\d+\.\s*([^\n\d]+)', text)
        if numbered:
            return [step.strip() for step in numbered]
        
        # Try to find sentences
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        if len(sentences) > 1:
            return sentences
        
        # Return as single step
        return [text] if text else []
    
    def _extract_frequency(self, text: str) -> str:
        """Extract usage frequency from text."""
        text_lower = text.lower()
        
        if 'twice' in text_lower or '2' in text_lower:
            return 'Twice daily'
        elif 'once' in text_lower or 'daily' in text_lower:
            return 'Once daily'
        elif 'weekly' in text_lower:
            return 'Weekly'
        else:
            return 'As directed'
    
    def _parse_safety(self, side_effects: Any) -> Dict[str, Any]:
        """Parse safety and side effects information."""
        if isinstance(side_effects, str):
            effects_list = [
                e.strip() for e in side_effects.split(',')
                if e.strip()
            ]
        elif isinstance(side_effects, list):
            effects_list = side_effects
        else:
            effects_list = [str(side_effects)]
        
        severity = self._assess_severity(effects_list)
        
        return {
            'side_effects': effects_list,
            'count': len(effects_list),
            'severity': severity,
            'warnings': self._generate_warnings(effects_list, severity)
        }
    
    def _assess_severity(self, effects: list) -> str:
        """Assess severity of side effects."""
        severe_keywords = ['severe', 'serious', 'burn', 'blister', 'emergency']
        moderate_keywords = ['irritation', 'redness', 'peeling', 'dry']
        
        effects_text = ' '.join(effects).lower()
        
        if any(kw in effects_text for kw in severe_keywords):
            return 'high'
        elif any(kw in effects_text for kw in moderate_keywords):
            return 'moderate'
        else:
            return 'low'
    
    def _generate_warnings(self, effects: list, severity: str) -> list:
        """Generate safety warnings based on side effects."""
        warnings = []
        
        if severity == 'high':
            warnings.append("Discontinue use if severe reactions occur")
            warnings.append("Consult a healthcare professional")
        
        if severity in ['high', 'moderate']:
            warnings.append("Perform patch test before use")
            warnings.append("Avoid contact with eyes")
        
        warnings.append("For external use only")
        
        return warnings
    
    def _parse_pricing(self, price: Any) -> Dict[str, Any]:
        """Parse pricing information."""
        import re
        
        price_str = str(price).strip()
        
        # Extract numeric value
        numbers = re.findall(r'\d+\.?\d*', price_str)
        numeric_value = float(numbers[0]) if numbers else 0.0
        
        # Extract currency
        currency = '₹' if '₹' in price_str or 'INR' in price_str else '$'
        
        return {
            'value': numeric_value,
            'currency': currency,
            'display': price_str,
            'formatted': f"{currency}{numeric_value:.2f}"
        }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()
