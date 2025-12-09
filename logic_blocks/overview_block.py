"""
Overview Block - Generates product overview content
"""
from typing import Dict, Any


class OverviewBlock:
    """Reusable logic block for generating overview content."""
    
    @staticmethod
    def execute(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate product overview content block.
        
        Args:
            data: Product data
            
        Returns:
            Formatted overview content
        """
        name = data.get('name', 'Product')
        concentration = data.get('concentration', {})
        ingredients = data.get('ingredients', {})
        
        overview_text = (
            f"{name} is formulated with {concentration.get('display', '')} "
            f"{ingredients.get('primary', 'active ingredients')} to deliver visible results."
        )
        
        content = {
            'title': 'Product Overview',
            'product_name': name,
            'concentration': concentration.get('display', ''),
            'primary_ingredient': ingredients.get('primary', ''),
            'overview_text': overview_text,
            'key_points': [
                f"Concentration: {concentration.get('display', 'N/A')}",
                f"Primary Ingredient: {ingredients.get('primary', 'N/A')}",
                f"Total Ingredients: {ingredients.get('count', 0)}"
            ]
        }
        
        return content
