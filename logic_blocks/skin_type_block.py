"""
Skin Type Block - Generates skin type suitability content
"""
from typing import Dict, Any


class SkinTypeBlock:
    """Reusable logic block for generating skin type content."""
    
    @staticmethod
    def execute(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate skin type information content block.
        
        Args:
            data: Product data containing skin type information
            
        Returns:
            Formatted skin type content
        """
        skin_type = data.get('skin_type', {})
        
        all_types = skin_type.get('all_types', ['All skin types'])
        formatted_types = ', '.join(all_types)
        
        content = {
            'title': 'Suitable For',
            'primary_skin_type': skin_type.get('primary', 'All skin types'),
            'all_skin_types': all_types,
            'skin_type_count': skin_type.get('count', 1),
            'formatted_types': formatted_types,
            'suitability_text': f"Suitable for {formatted_types}."
        }
        
        return content
