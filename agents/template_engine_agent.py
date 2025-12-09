"""
Template Engine Agent
Applies structured templates to data and populates them
"""

from typing import Dict, Any
from agents.base_agent import BaseAgent
import json
import logging

logger = logging.getLogger(__name__)


class TemplateEngineAgent(BaseAgent):
    """
    Agent responsible for loading and applying templates.
    
    Input: Template ID + data
    Output: Populated template structure
    
    Supports:
    - FAQ Template
    - Product Page Template
    - Comparison Template
    """
    
    def __init__(self, templates_dir: str = "templates"):
        super().__init__(
            agent_id="template_engine_001",
            agent_type="template_engine"
        )
        self.templates_dir = templates_dir
        self.loaded_templates = {}
    
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """Validate input has template_id and data."""
        return 'template_id' in input_data and 'data' in input_data
    
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply template to data.
        
        Args:
            input_data: {
                'template_id': str,
                'data': dict,
                'logic_blocks': dict (optional)
            }
            
        Returns:
            Populated template structure
        """
        template_id = input_data['template_id']
        data = input_data['data']
        logic_blocks = input_data.get('logic_blocks', {})
        
        logger.info(f"Applying template: {template_id}")
        
        # Load template
        template = self._load_template(template_id)
        
        # Populate template
        populated = self._populate_template(template, data, logic_blocks)
        
        return populated
    
    def _load_template(self, template_id: str) -> Dict[str, Any]:
        """Load template by ID."""
        if template_id in self.loaded_templates:
            return self.loaded_templates[template_id]
        
        # Return built-in template
        if template_id == 'faq':
            template = self._get_faq_template()
        elif template_id == 'product_page':
            template = self._get_product_page_template()
        elif template_id == 'comparison':
            template = self._get_comparison_template()
        else:
            raise ValueError(f"Unknown template: {template_id}")
        
        self.loaded_templates[template_id] = template
        return template
    
    def _get_faq_template(self) -> Dict[str, Any]:
        """Get FAQ page template."""
        return {
            'template_id': 'faq',
            'template_type': 'faq_page',
            'sections': [
                {
                    'section_id': 'header',
                    'section_type': 'header',
                    'required_data': ['product_name'],
                    'format': 'text'
                },
                {
                    'section_id': 'faqs',
                    'section_type': 'faq_list',
                    'required_data': ['questions', 'answers'],
                    'format': 'qa_pairs'
                }
            ],
            'structure': {
                'page_title': '{{product_name}} - Frequently Asked Questions',
                'introduction': 'Common questions about {{product_name}}',
                'faqs': []
            }
        }
    
    def _get_product_page_template(self) -> Dict[str, Any]:
        """Get product page template."""
        return {
            'template_id': 'product_page',
            'template_type': 'product_description',
            'sections': [
                {
                    'section_id': 'overview',
                    'section_type': 'product_overview',
                    'required_data': ['name', 'concentration'],
                    'logic_block': 'overview_block'
                },
                {
                    'section_id': 'skin_type',
                    'section_type': 'skin_type_info',
                    'required_data': ['skin_type'],
                    'logic_block': 'skin_type_block'
                },
                {
                    'section_id': 'ingredients',
                    'section_type': 'ingredients_list',
                    'required_data': ['ingredients'],
                    'logic_block': 'ingredients_block'
                },
                {
                    'section_id': 'benefits',
                    'section_type': 'benefits_list',
                    'required_data': ['benefits'],
                    'logic_block': 'benefits_block'
                },
                {
                    'section_id': 'usage',
                    'section_type': 'usage_guide',
                    'required_data': ['usage'],
                    'logic_block': 'usage_block'
                },
                {
                    'section_id': 'safety',
                    'section_type': 'safety_info',
                    'required_data': ['safety'],
                    'logic_block': 'safety_block'
                },
                {
                    'section_id': 'pricing',
                    'section_type': 'pricing_info',
                    'required_data': ['pricing'],
                    'logic_block': 'pricing_block'
                }
            ]
        }
    
    def _get_comparison_template(self) -> Dict[str, Any]:
        """Get comparison page template."""
        return {
            'template_id': 'comparison',
            'template_type': 'product_comparison',
            'sections': [
                {
                    'section_id': 'header',
                    'section_type': 'comparison_header',
                    'required_data': ['product_a', 'product_b']
                },
                {
                    'section_id': 'comparison_table',
                    'section_type': 'comparison_matrix',
                    'required_data': ['comparison'],
                    'logic_block': 'comparison_block'
                },
                {
                    'section_id': 'summary',
                    'section_type': 'summary',
                    'required_data': ['summary']
                }
            ]
        }
    
    def _populate_template(
        self,
        template: Dict[str, Any],
        data: Dict[str, Any],
        logic_blocks: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Populate template with data."""
        result = {
            'template_id': template['template_id'],
            'template_type': template['template_type'],
            'sections': []
        }
        
        for section in template['sections']:
            populated_section = self._populate_section(
                section,
                data,
                logic_blocks
            )
            result['sections'].append(populated_section)
        
        return result
    
    def _populate_section(
        self,
        section: Dict[str, Any],
        data: Dict[str, Any],
        logic_blocks: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Populate a single section."""
        section_data = {
            'section_id': section['section_id'],
            'section_type': section['section_type'],
            'content': {}
        }
        
        # Get required data
        for required_field in section.get('required_data', []):
            if required_field in data:
                section_data['content'][required_field] = data[required_field]
        
        # Apply logic block if specified
        logic_block_name = section.get('logic_block')
        if logic_block_name and logic_block_name in logic_blocks:
            section_data['processed_content'] = logic_blocks[logic_block_name]
        
        return section_data
    
    def _replace_placeholders(self, text: str, data: Dict[str, Any]) -> str:
        """Replace {{placeholder}} with actual data."""
        import re
        
        def replace(match):
            key = match.group(1)
            keys = key.split('.')
            value = data
            
            for k in keys:
                if isinstance(value, dict) and k in value:
                    value = value[k]
                else:
                    return match.group(0)  # Return original if not found
            
            return str(value)
        
        return re.sub(r'\{\{([^}]+)\}\}', replace, text)
