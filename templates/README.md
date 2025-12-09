# Templates Directory

This directory contains structured templates for content generation.

## Available Templates

### 1. FAQ Template (`faq_template.json`)
- **Purpose**: Generate FAQ pages
- **Sections**: Header, Q&A pairs
- **Minimum**: 5 questions required
- **Format**: JSON with categorized questions

### 2. Product Page Template (`product_page_template.json`)
- **Purpose**: Generate product description pages
- **Sections**: 7 content sections
  - Overview
  - Skin Type Suitability
  - Ingredients
  - Benefits
  - Usage Instructions
  - Safety Information
  - Pricing
- **Logic Blocks**: Each section links to a specific logic block

### 3. Comparison Template (`comparison_template.json`)
- **Purpose**: Generate product comparison pages
- **Sections**: Header, Comparison Matrix, Summary
- **Dimensions**: Concentration, Ingredients, Benefits, Pricing
- **Format**: Side-by-side comparison structure

## Template Structure

Each template includes:
- `template_id`: Unique identifier
- `template_type`: Category of template
- `sections`: Array of content sections
- `required_data`: Fields needed for rendering
- `logic_block`: Associated processing block (if applicable)

## Usage

Templates are loaded by the Template Engine Agent and populated with:
1. Product data (parsed)
2. Logic block outputs (processed)
3. Generated questions (for FAQ)

The final output is a structured JSON page matching the template specification.
