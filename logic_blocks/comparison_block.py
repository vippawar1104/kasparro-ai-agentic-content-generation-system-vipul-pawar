"""
Comparison Block - Generates product comparison content
"""
from typing import Dict, Any


class ComparisonBlock:
    """Reusable logic block for generating comparison content."""
    
    @staticmethod
    def execute(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate comparison content block.
        
        Args:
            data: Comparison data containing both products
            
        Returns:
            Formatted comparison content
        """
        comparison = data.get('comparison', {})
        
        content = {
            'title': 'Product Comparison',
            'product_a': comparison.get('basic_info', {}).get('product_a_name'),
            'product_b': comparison.get('basic_info', {}).get('product_b_name'),
            'concentration_comparison': comparison.get('concentration', {}),
            'ingredients_comparison': comparison.get('ingredients', {}),
            'benefits_comparison': comparison.get('benefits', {}),
            'pricing_comparison': comparison.get('pricing', {}),
            'summary': data.get('summary', ''),
            'recommendation': ComparisonBlock._generate_recommendation(comparison)
        }
        
        return content
    
    @staticmethod
    def _generate_recommendation(comparison: Dict[str, Any]) -> str:
        """Generate product recommendation based on comparison."""
        pricing = comparison.get('pricing', {})
        value_assessment = pricing.get('value_assessment', '')
        
        if 'better value' in value_assessment.lower():
            return "Product A recommended for budget-conscious consumers"
        elif 'premium' in value_assessment.lower():
            return "Product B recommended for those seeking premium formulation"
        else:
            return "Both products offer comparable value - choose based on specific needs"
