"""
Usage Block - Generates usage instructions content
"""
from typing import Dict, Any


class UsageBlock:
    """Reusable logic block for generating usage content."""
    
    @staticmethod
    def execute(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate usage instructions content block.
        
        Args:
            data: Product data containing usage information
            
        Returns:
            Formatted usage content
        """
        usage = data.get('usage', {})
        
        content = {
            'title': 'How to Use',
            'steps': usage.get('steps', []),
            'frequency': usage.get('frequency', 'As directed'),
            'full_instructions': usage.get('full_instructions', ''),
            'formatted_steps': [
                f"{i+1}. {step}" 
                for i, step in enumerate(usage.get('steps', []))
            ],
            'quick_guide': f"Apply {usage.get('frequency', 'as directed').lower()}"
        }
        
        return content
