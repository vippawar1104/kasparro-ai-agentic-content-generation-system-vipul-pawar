"""
Pricing Block - Generates pricing content section
"""
from typing import Dict, Any


class PricingBlock:
    """Reusable logic block for generating pricing content."""
    
    @staticmethod
    def execute(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate pricing content block.
        
        Args:
            data: Product data containing pricing information
            
        Returns:
            Formatted pricing content
        """
        pricing = data.get('pricing', {})
        
        value_proposition = PricingBlock._assess_price_value(pricing.get('value', 0))
        
        content = {
            'title': 'Pricing',
            'price': pricing.get('formatted', 'Contact for pricing'),
            'currency': pricing.get('currency', '$'),
            'value': pricing.get('value', 0),
            'display_price': pricing.get('display', ''),
            'value_proposition': value_proposition,
            'pricing_summary': (
                f"Priced at {pricing.get('formatted', 'N/A')}, "
                f"offering {value_proposition.lower()} value."
            )
        }
        
        return content
    
    @staticmethod
    def _assess_price_value(price: float) -> str:
        """Assess price value proposition."""
        if price < 20:
            return "Excellent"
        elif price < 40:
            return "Good"
        elif price < 60:
            return "Fair"
        else:
            return "Premium"
