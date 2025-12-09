"""
Ingredients Block - Generates ingredients content section
"""
from typing import Dict, Any


class IngredientsBlock:
    """Reusable logic block for generating ingredients content."""
    
    @staticmethod
    def execute(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate ingredients content block.
        
        Args:
            data: Product data containing ingredients information
            
        Returns:
            Formatted ingredients content
        """
        ingredients = data.get('ingredients', {})
        concentration = data.get('concentration', {})
        
        content = {
            'title': 'Key Ingredients',
            'ingredients': ingredients.get('list', []),
            'count': ingredients.get('count', 0),
            'primary_ingredient': ingredients.get('primary'),
            'concentration': concentration.get('display'),
            'formatted_list': [f"• {ing}" for ing in ingredients.get('list', [])],
            'ingredient_summary': (
                f"Contains {ingredients.get('count', 0)} active ingredients "
                f"at {concentration.get('display', 'optimal')} concentration."
            )
        }
        
        return content
