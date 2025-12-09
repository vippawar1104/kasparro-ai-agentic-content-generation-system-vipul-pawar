"""
Safety Block - Generates safety and side effects content
"""
from typing import Dict, Any


class SafetyBlock:
    """Reusable logic block for generating safety content."""
    
    @staticmethod
    def execute(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate safety information content block.
        
        Args:
            data: Product data containing safety information
            
        Returns:
            Formatted safety content
        """
        safety = data.get('safety', {})
        
        content = {
            'title': 'Safety Information',
            'side_effects': safety.get('side_effects', []),
            'warnings': safety.get('warnings', []),
            'severity': safety.get('severity', 'low'),
            'formatted_side_effects': [
                f"• {effect}" for effect in safety.get('side_effects', [])
            ],
            'formatted_warnings': [
                f"⚠ {warning}" for warning in safety.get('warnings', [])
            ],
            'safety_summary': (
                f"Severity: {safety.get('severity', 'low').title()}. "
                "Always perform a patch test before use."
            )
        }
        
        return content
