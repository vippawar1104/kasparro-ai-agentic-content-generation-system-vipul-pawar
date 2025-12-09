"""
Comparison Agent
Creates a fictional Product B and generates comparison data
"""

from typing import Dict, Any
from agents.base_agent import BaseAgent
import logging
import random

logger = logging.getLogger(__name__)


class ComparisonAgent(BaseAgent):
    """
    Agent responsible for creating a fictional comparison product.
    
    Input: Product A data
    Output: Product B data + comparison matrix
    
    Creates realistic variations:
    - Different concentration
    - Different ingredients
    - Different price
    - Similar but distinct benefits
    """
    
    def __init__(self):
        super().__init__(
            agent_id="comparison_agent_001",
            agent_type="comparison"
        )
        
        # Alternative ingredients for generation
        self.alternative_ingredients = {
            'Niacinamide': ['Alpha Arbutin', 'Kojic Acid', 'Licorice Extract'],
            'Salicylic Acid': ['Glycolic Acid', 'Lactic Acid', 'Mandelic Acid'],
            'Retinol': ['Bakuchiol', 'Retinyl Palmitate', 'Tretinoin'],
            'Vitamin C': ['Vitamin E', 'Ferulic Acid', 'Resveratrol'],
            'Hyaluronic Acid': ['Glycerin', 'Ceramides', 'Squalane']
        }
    
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """Validate product A data."""
        required = ['name', 'concentration', 'ingredients', 'benefits', 'pricing']
        return all(key in input_data for key in required)
    
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate Product B and comparison data.
        
        Args:
            input_data: Product A structured data
            
        Returns:
            Dictionary with Product B and comparison matrix
        """
        logger.info("Generating comparison product...")
        
        product_a = input_data
        product_b = self._generate_product_b(product_a)
        comparison = self._generate_comparison(product_a, product_b)
        
        result = {
            'product_a': product_a,
            'product_b': product_b,
            'comparison': comparison,
            'summary': self._generate_summary(comparison)
        }
        
        logger.info(f"Generated comparison between {product_a['name']} and {product_b['name']}")
        
        return result
    
    def _generate_product_b(self, product_a: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a fictional Product B based on Product A."""
        
        # Generate variant name
        original_name = product_a.get('name', 'Serum')
        base_name = original_name.split()[0] if ' ' in original_name else original_name
        
        suffixes = ['Plus', 'Pro', 'Ultra', 'Advanced', 'Premium']
        product_b_name = f"{base_name} {random.choice(suffixes)}"
        
        # Vary concentration
        original_conc = product_a.get('concentration', {})
        product_b_conc = self._vary_concentration(original_conc)
        
        # Vary ingredients
        product_b_ingredients = self._vary_ingredients(
            product_a.get('ingredients', {})
        )
        
        # Vary benefits
        product_b_benefits = self._vary_benefits(
            product_a.get('benefits', {})
        )
        
        # Vary price
        product_b_pricing = self._vary_pricing(
            product_a.get('pricing', {})
        )
        
        # Keep skin type similar
        skin_type = product_a.get('skin_type', {})
        
        product_b = {
            'product_id': product_b_name.lower().replace(' ', '_'),
            'name': product_b_name,
            'concentration': product_b_conc,
            'skin_type': skin_type,
            'ingredients': product_b_ingredients,
            'benefits': product_b_benefits,
            'pricing': product_b_pricing,
            'metadata': {
                'generated': True,
                'based_on': product_a.get('product_id'),
                'variant_type': 'comparison'
            }
        }
        
        return product_b
    
    def _vary_concentration(self, original: Dict[str, Any]) -> Dict[str, Any]:
        """Generate different concentration."""
        original_pct = original.get('percentage', 10.0)
        
        # Vary by ±20-40%
        variation = random.choice([-0.3, -0.2, 0.2, 0.3])
        new_pct = round(original_pct * (1 + variation), 1)
        
        return {
            'value': f"{new_pct}%",
            'percentage': new_pct,
            'display': f"{new_pct}%"
        }
    
    def _vary_ingredients(self, original: Dict[str, Any]) -> Dict[str, Any]:
        """Generate different ingredient list."""
        original_list = original.get('list', [])
        
        new_ingredients = []
        
        for ingredient in original_list:
            # 60% chance to keep the ingredient
            if random.random() < 0.6:
                new_ingredients.append(ingredient)
            else:
                # Replace with alternative
                alternative = self._get_alternative_ingredient(ingredient)
                new_ingredients.append(alternative)
        
        # Maybe add one more ingredient
        if random.random() < 0.4:
            additional = random.choice([
                'Peptides',
                'Antioxidants',
                'Plant Extracts',
                'Moisturizers'
            ])
            new_ingredients.append(additional)
        
        return {
            'list': new_ingredients,
            'count': len(new_ingredients),
            'primary': new_ingredients[0] if new_ingredients else None,
            'formatted': ', '.join(new_ingredients)
        }
    
    def _get_alternative_ingredient(self, ingredient: str) -> str:
        """Get an alternative ingredient."""
        # Check if we have predefined alternatives
        for key, alternatives in self.alternative_ingredients.items():
            if key.lower() in ingredient.lower():
                return random.choice(alternatives)
        
        # Generic alternatives
        generic_alternatives = [
            'Botanical Extract',
            'Active Complex',
            'Skin Enhancer',
            'Bio-Active'
        ]
        return random.choice(generic_alternatives)
    
    def _vary_benefits(self, original: Dict[str, Any]) -> Dict[str, Any]:
        """Generate different benefits list."""
        original_list = original.get('list', [])
        
        # Keep most benefits, vary some
        new_benefits = []
        
        for benefit in original_list:
            if random.random() < 0.7:
                new_benefits.append(benefit)
            else:
                # Modify benefit slightly
                new_benefits.append(self._modify_benefit(benefit))
        
        # Add unique benefit
        unique_benefits = [
            'Enhanced absorption',
            'Long-lasting results',
            'Gentle formula',
            'Fast-acting'
        ]
        new_benefits.append(random.choice(unique_benefits))
        
        return {
            'list': new_benefits,
            'count': len(new_benefits),
            'primary': new_benefits[0] if new_benefits else None,
            'categories': self._categorize_benefits(new_benefits)
        }
    
    def _modify_benefit(self, benefit: str) -> str:
        """Slightly modify a benefit."""
        modifiers = ['Enhanced', 'Improved', 'Advanced', 'Superior']
        return f"{random.choice(modifiers)} {benefit.lower()}"
    
    def _categorize_benefits(self, benefits: list) -> Dict[str, list]:
        """Simple benefit categorization."""
        return {
            'treatment': [b for b in benefits if any(w in b.lower() for w in ['reduce', 'treat', 'fade'])],
            'prevention': [b for b in benefits if any(w in b.lower() for w in ['prevent', 'protect'])],
            'enhancement': [b for b in benefits if any(w in b.lower() for w in ['enhance', 'improve', 'boost'])],
            'general': [b for b in benefits if b not in sum([
                [b for b in benefits if any(w in b.lower() for w in ['reduce', 'treat', 'fade', 'prevent', 'protect', 'enhance', 'improve', 'boost'])]
            ], [])]
        }
    
    def _vary_pricing(self, original: Dict[str, Any]) -> Dict[str, Any]:
        """Generate different pricing."""
        original_value = original.get('value', 30.0)
        currency = original.get('currency', '$')
        
        # Vary by -15% to +30%
        variation = random.uniform(-0.15, 0.30)
        new_value = round(original_value * (1 + variation), 2)
        
        return {
            'value': new_value,
            'currency': currency,
            'display': f"{currency}{new_value}",
            'formatted': f"{currency}{new_value:.2f}"
        }
    
    def _generate_comparison(
        self,
        product_a: Dict[str, Any],
        product_b: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate comparison matrix."""
        
        comparison = {
            'basic_info': {
                'product_a_name': product_a.get('name'),
                'product_b_name': product_b.get('name')
            },
            'concentration': {
                'product_a': product_a.get('concentration', {}).get('display'),
                'product_b': product_b.get('concentration', {}).get('display'),
                'difference': self._compare_concentrations(
                    product_a.get('concentration', {}),
                    product_b.get('concentration', {})
                )
            },
            'ingredients': {
                'product_a': product_a.get('ingredients', {}).get('list', []),
                'product_b': product_b.get('ingredients', {}).get('list', []),
                'common': self._find_common_ingredients(
                    product_a.get('ingredients', {}),
                    product_b.get('ingredients', {})
                ),
                'unique_to_a': self._find_unique_ingredients(
                    product_a.get('ingredients', {}),
                    product_b.get('ingredients', {})
                ),
                'unique_to_b': self._find_unique_ingredients(
                    product_b.get('ingredients', {}),
                    product_a.get('ingredients', {})
                )
            },
            'benefits': {
                'product_a': product_a.get('benefits', {}).get('list', []),
                'product_b': product_b.get('benefits', {}).get('list', []),
                'comparison': self._compare_benefits(
                    product_a.get('benefits', {}),
                    product_b.get('benefits', {})
                )
            },
            'pricing': {
                'product_a': product_a.get('pricing', {}).get('formatted'),
                'product_b': product_b.get('pricing', {}).get('formatted'),
                'difference': self._compare_pricing(
                    product_a.get('pricing', {}),
                    product_b.get('pricing', {})
                ),
                'value_assessment': self._assess_value(
                    product_a.get('pricing', {}),
                    product_b.get('pricing', {})
                )
            }
        }
        
        return comparison
    
    def _compare_concentrations(
        self,
        conc_a: Dict[str, Any],
        conc_b: Dict[str, Any]
    ) -> str:
        """Compare concentrations."""
        pct_a = conc_a.get('percentage', 0)
        pct_b = conc_b.get('percentage', 0)
        
        if pct_a > pct_b:
            return f"Product A has higher concentration (+{pct_a - pct_b:.1f}%)"
        elif pct_b > pct_a:
            return f"Product B has higher concentration (+{pct_b - pct_a:.1f}%)"
        else:
            return "Same concentration"
    
    def _find_common_ingredients(
        self,
        ing_a: Dict[str, Any],
        ing_b: Dict[str, Any]
    ) -> list:
        """Find common ingredients."""
        list_a = set([i.lower() for i in ing_a.get('list', [])])
        list_b = set([i.lower() for i in ing_b.get('list', [])])
        return list(list_a.intersection(list_b))
    
    def _find_unique_ingredients(
        self,
        ing_a: Dict[str, Any],
        ing_b: Dict[str, Any]
    ) -> list:
        """Find ingredients unique to product A."""
        list_a = set([i.lower() for i in ing_a.get('list', [])])
        list_b = set([i.lower() for i in ing_b.get('list', [])])
        return list(list_a.difference(list_b))
    
    def _compare_benefits(
        self,
        ben_a: Dict[str, Any],
        ben_b: Dict[str, Any]
    ) -> str:
        """Compare benefits."""
        count_a = ben_a.get('count', 0)
        count_b = ben_b.get('count', 0)
        
        if count_a > count_b:
            return f"Product A offers more benefits ({count_a} vs {count_b})"
        elif count_b > count_a:
            return f"Product B offers more benefits ({count_b} vs {count_a})"
        else:
            return "Similar number of benefits"
    
    def _compare_pricing(
        self,
        price_a: Dict[str, Any],
        price_b: Dict[str, Any]
    ) -> str:
        """Compare pricing."""
        val_a = price_a.get('value', 0)
        val_b = price_b.get('value', 0)
        currency = price_a.get('currency', '$')
        
        diff = abs(val_a - val_b)
        
        if val_a < val_b:
            return f"Product A is {currency}{diff:.2f} cheaper"
        elif val_b < val_a:
            return f"Product B is {currency}{diff:.2f} cheaper"
        else:
            return "Same price"
    
    def _assess_value(
        self,
        price_a: Dict[str, Any],
        price_b: Dict[str, Any]
    ) -> str:
        """Assess value proposition."""
        val_a = price_a.get('value', 0)
        val_b = price_b.get('value', 0)
        
        if val_a < val_b:
            return "Product A offers better value"
        elif val_b < val_a:
            return "Product B is premium priced"
        else:
            return "Similar value proposition"
    
    def _generate_summary(self, comparison: Dict[str, Any]) -> str:
        """Generate comparison summary."""
        prod_a = comparison['basic_info']['product_a_name']
        prod_b = comparison['basic_info']['product_b_name']
        
        summary = f"{prod_a} vs {prod_b}: "
        summary += comparison['concentration']['difference'] + ". "
        summary += comparison['pricing']['difference'] + ". "
        summary += comparison['benefits']['comparison'] + "."
        
        return summary
