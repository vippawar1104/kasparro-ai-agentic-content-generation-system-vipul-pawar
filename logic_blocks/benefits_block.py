"""
Benefits Block - Generates benefits content section
"""
from typing import Dict, Any


class BenefitsBlock:
    """Reusable logic block for generating benefits content."""
    
    @staticmethod
    def execute(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate benefits content block.
        
        Args:
            data: Product data containing benefits information
            
        Returns:
            Formatted benefits content
        """
        benefits = data.get('benefits', {})
        benefit_list = benefits.get('list', [])
        categories = benefits.get('categories', {})
        
        content = {
            'title': 'Key Benefits',
            'benefits': benefit_list,
            'categorized_benefits': categories,
            'formatted_list': [f"• {benefit}" for benefit in benefit_list],
            'summary': f"This product offers {len(benefit_list)} key benefits for your skin."
        }
        
        return content
