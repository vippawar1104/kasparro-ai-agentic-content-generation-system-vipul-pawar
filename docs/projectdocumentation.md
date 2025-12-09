# Project Documentation
## Multi-Agent Product Content Generation System

### Kasparro AI Engineer Challenge Submission
**By: Vipul Pawar**

---

## 📋 Table of Contents

1. [Problem Statement](#problem-statement)
2. [Scope & Assumptions](#scope--assumptions)
3. [Solution Overview](#solution-overview)
4. [Architecture & System Design](#architecture--system-design)
5. [Agent Responsibilities](#agent-responsibilities)
6. [Data Flow & Orchestration](#data-flow--orchestration)
7. [Template System Design](#template-system-design)
8. [Logic Blocks System](#logic-blocks-system)
9. [JSON Output Explanation](#json-output-explanation)
10. [Implementation Details](#implementation-details)
11. [Usage Instructions](#usage-instructions)
12. [Future Improvements](#future-improvements)

---

## 1. Problem Statement

Build a **modular multi-agent automation system** that generates structured content pages from a small product dataset.

### Requirements:
- ✅ Design a multi-agent system (not a single script)
- ✅ Create 7+ specialized agents with clear responsibilities
- ✅ Implement a custom template engine
- ✅ Build reusable logic blocks for content processing
- ✅ Generate 15+ categorized user questions
- ✅ Produce 3 JSON pages: FAQ, Product Description, Comparison
- ✅ Use ONLY the given product data (no external sources)
- ✅ Create systematic, structured, reusable architecture
- ✅ Implement proper orchestration workflow

---

## 2. Scope & Assumptions

### Scope:
- **Input**: Single product with 8 fields (name, concentration, skin_type, ingredients, benefits, usage, side_effects, price)
- **Processing**: Multi-agent pipeline with specialized roles
- **Output**: 3 machine-readable JSON files

### Assumptions:
1. Product data is complete and valid
2. All 8 required fields are provided
3. Product is skincare/beauty related
4. Processing is sequential (agents run in order)
5. No external API calls or internet lookups
6. System generates content deterministically from input data
7. Comparison product is fictional but realistic

### Out of Scope:
- Multi-product batch processing
- Real-time content updates
- User interface/dashboard
- External data enrichment
- Content translation
- Image generation

---

## 3. Solution Overview

### System Type:
**Modular Multi-Agent Architecture** with specialized agents, reusable components, and orchestrated workflow.

### Key Components:
1. **7 Specialized Agents**:
   - Product Parser Agent
   - Question Generator Agent
   - Comparison Agent
   - Template Engine Agent
   - Logic Blocks Processor Agent
   - Page Assembly Agent
   - Orchestrator Agent (coordinator)

2. **8 Logic Blocks**:
   - Overview Block
   - Skin Type Block
   - Ingredients Block
   - Benefits Block
   - Usage Block
   - Safety Block
   - Pricing Block
   - Comparison Block

3. **3 Templates**:
   - FAQ Template
   - Product Page Template
   - Comparison Template

4. **3 JSON Outputs**:
   - `faq.json`
   - `product_page.json`
   - `comparison_page.json`

---

## 4. Architecture & System Design

### High-Level Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                       ORCHESTRATOR AGENT                          │
│                  (Workflow Coordinator & Manager)                 │
└────────────────┬─────────────────────────────────────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
┌───────▼────────┐  ┌─────▼──────────┐
│ Product Parser │  │    Question    │
│     Agent      │  │   Generator    │
└───────┬────────┘  └────────┬───────┘
        │                    │
        │     ┌──────────────┴──────────┐
        │     │                         │
┌───────▼─────▼─────┐     ┌────────────▼──────┐
│  Comparison Agent  │     │ Logic Blocks      │
│                    │     │ Processor Agent   │
└───────┬────────────┘     └────────┬──────────┘
        │                           │
        │      ┌────────────────────┴──────────┐
        │      │                               │
┌───────▼──────▼───────┐        ┌──────────────▼────┐
│  Template Engine     │        │  Page Assembly    │
│      Agent           │        │      Agent        │
└──────────────────────┘        └──────────┬────────┘
                                           │
                                  ┌────────▼─────────┐
                                  │  Final Outputs   │
                                  │  • faq.json      │
                                  │  • product.json  │
                                  │  • comparison.json│
                                  └──────────────────┘
```

### Design Principles:

1. **Modularity**: Each agent is self-contained with single responsibility
2. **Reusability**: Logic blocks are composable and template-agnostic
3. **Scalability**: Stateless agents allow parallel execution (future)
4. **Maintainability**: Clear interfaces and type hints
5. **Testability**: Each component can be tested independently

### Technology Stack:
- **Language**: Python 3.9+
- **Architecture**: Agent-based microservices pattern
- **Data Format**: JSON
- **Logging**: Python logging module

---

## 5. Agent Responsibilities

### 5.1 Product Parser Agent
**Purpose**: Clean and structure raw product data

**Input**:
```json
{
  "product_name": "string",
  "concentration": "string",
  "skin_type": "string",
  "key_ingredients": "string",
  "benefits": "string",
  "usage_instructions": "string",
  "side_effects": "string",
  "price": "string"
}
```

**Output**: Validated structured JSON with:
- Product ID generation
- Concentration parsing (extract percentage)
- Skin type categorization
- Ingredient list parsing
- Benefit categorization (treatment/prevention/enhancement)
- Usage step extraction
- Safety warnings generation
- Pricing normalization

**Key Functions**:
- `_parse_concentration()`: Extract numeric values
- `_parse_ingredients()`: Convert to list
- `_categorize_benefits()`: Group by type
- `_extract_steps()`: Parse usage instructions
- `_assess_severity()`: Analyze side effects

---

### 5.2 Question Generator Agent
**Purpose**: Generate user questions from product data

**Input**: Structured product data
**Output**: 15+ questions in 5 categories

**Categories**:
1. **Informational** (What is this? What are ingredients?)
2. **Usage** (How to use? When to apply?)
3. **Safety** (Side effects? Precautions?)
4. **Purchase** (Price? Value?)
5. **Comparison** (vs others? Unique features?)

**Logic**:
- Analyzes product fields
- Creates context-aware questions
- Ensures minimum 15 questions
- Categorizes automatically

**Example Output**:
```json
{
  "informational": [
    "What is Niacinamide 10% + Zinc 1% Serum?",
    "What are the key ingredients?"
  ],
  "usage": [
    "How do I use this product?",
    "How often should I apply it?"
  ]
  ...
}
```

---

### 5.3 Comparison Agent
**Purpose**: Create fictional Product B and comparison matrix

**Input**: Product A data
**Output**: Product B + comparison data

**Generation Logic**:
- **Name**: Adds suffix (Plus, Pro, Ultra, Advanced)
- **Concentration**: Varies by ±20-40%
- **Ingredients**: 60% overlap, 40% variations
- **Benefits**: Similar but distinct
- **Price**: Varies by -15% to +30%

**Comparison Matrix Includes**:
- Concentration difference
- Common/unique ingredients
- Benefits comparison
- Price difference
- Value assessment
- Recommendation

**Example**:
```
Product A: Niacinamide 10%
Product B: Niacinamide Plus (13%)
Difference: Product B has higher concentration (+3%)
```

---

### 5.4 Template Engine Agent
**Purpose**: Load and populate templates

**Input**: Template ID + data + logic blocks
**Output**: Populated template structure

**Supported Templates**:
1. **FAQ Template**: Q&A pairs with categories
2. **Product Template**: 7 sections (overview, ingredients, benefits, etc.)
3. **Comparison Template**: Side-by-side matrix

**Features**:
- Placeholder replacement (`{{product.name}}`)
- Section validation
- Logic block integration
- Reusable templates

---

### 5.5 Logic Blocks Processor Agent
**Purpose**: Execute reusable content logic

**Input**: List of block names + data
**Output**: Processed content blocks

**Available Blocks**:

| Block | Purpose | Output |
|-------|---------|--------|
| `overview_block` | Product summary | Overview text + key points |
| `skin_type_block` | Skin compatibility | Suitability info |
| `ingredients_block` | Ingredient details | List + summary |
| `benefits_block` | Benefits formatting | Categorized benefits |
| `usage_block` | Usage instructions | Steps + frequency |
| `safety_block` | Safety warnings | Side effects + warnings |
| `pricing_block` | Price presentation | Formatted price + value |
| `comparison_block` | Comparison analysis | Matrix + recommendation |

**Each Block Returns**:
- Title
- Formatted content
- Summary text
- Metadata

---

### 5.6 Page Assembly Agent
**Purpose**: Combine all components into final pages

**Input**: Template + Logic Blocks + Data
**Output**: Complete JSON page

**Process**:
1. Receive assembled components
2. Map logic blocks to sections
3. Generate Q&A answers (for FAQ)
4. Structure final JSON
5. Add metadata
6. Validate completeness

**Answer Generation Logic** (FAQ):
- Keyword matching (question → data source)
- Category-based fallback
- Uses logic blocks for answers
- Ensures all questions answered

---

### 5.7 Orchestrator Agent
**Purpose**: Control entire workflow

**Workflow Sequence**:
1. Initialize all agents
2. Parse product data (Agent #1)
3. Generate questions (Agent #2)
4. Create comparison (Agent #3)
5. Process logic blocks (Agent #5)
6. Apply templates (Agent #4)
7. Assemble pages (Agent #6)
8. Save JSON outputs

**Error Handling**:
- Validates each step
- Logs progress
- Fails gracefully
- Returns detailed errors

---

## 6. Data Flow & Orchestration

### Sequential Pipeline

```
┌─────────────────┐
│  Raw Product    │
│  JSON Input     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Product Parser  │───► Structured Product Data
└────────┬────────┘
         │
         ├──────────────────┐
         │                  │
         ▼                  ▼
┌────────────────┐  ┌──────────────┐
│ Question Gen   │  │ Comparison   │
└────────┬───────┘  └──────┬───────┘
         │                 │
         │ 15+ Questions   │ Product B
         │                 │
         └────────┬────────┘
                  │
                  ▼
         ┌────────────────┐
         │ Logic Blocks   │───► 8 Content Blocks
         │ Processor      │
         └────────┬───────┘
                  │
                  ▼
         ┌────────────────┐
         │ Template       │───► Populated Templates
         │ Engine         │
         └────────┬───────┘
                  │
                  ▼
         ┌────────────────┐
         │ Page Assembly  │───► faq.json
         │                │───► product_page.json
         │                │───► comparison_page.json
         └────────────────┘
```

### State Management:
- **No shared state** between agents
- Each agent receives immutable input
- Each agent returns new output
- Orchestrator maintains execution context

### Message Passing:
```python
# Step 1
parsed = parser.run(raw_data)

# Step 2
questions = question_gen.run(parsed['data'])

# Step 3
comparison = comparison_agent.run(parsed['data'])

# Steps combined by orchestrator
```

---

## 7. Template System Design

### Template Structure

Each template defines:
- **Template ID**: Unique identifier
- **Type**: Page type (FAQ, Product, Comparison)
- **Sections**: List of content sections
- **Metadata**: Template version and info

### Example Template (Product Page):

```python
{
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
            'section_id': 'ingredients',
            'section_type': 'ingredients_list',
            'required_data': ['ingredients'],
            'logic_block': 'ingredients_block'
        }
        # ... more sections
    ]
}
```

### Placeholder System:
- `{{product.name}}` → Replace with actual product name
- `{{logic.benefits}}` → Insert from benefits logic block
- `{{data.price}}` → Insert from data field

### Template Rendering:
1. Load template by ID
2. Validate required data present
3. Execute associated logic blocks
4. Replace all placeholders
5. Return structured content

---

## 8. Logic Blocks System

### Logic Block Interface:

```python
class LogicBlock:
    def execute(data: dict) -> dict:
        """
        Process data and return formatted content
        
        Returns:
            {
                'title': str,
                'content': any,
                'formatted': list,
                'summary': str
            }
        """
```

### Benefits of Logic Blocks:

1. **Reusability**: Same block used across multiple pages
2. **Consistency**: Uniform formatting
3. **Maintainability**: Change once, apply everywhere
4. **Testability**: Each block tested independently
5. **Composability**: Combine blocks for complex content

### Example: Benefits Block

```python
def _benefits_block(data):
    benefits = data['benefits']
    return {
        'title': 'Key Benefits',
        'benefits': benefits['list'],
        'categorized': benefits['categories'],
        'formatted_list': ['• ' + b for b in benefits['list']],
        'summary': f"Offers {len(benefits['list'])} benefits"
    }
```

---

## 9. JSON Output Explanation

### 9.1 FAQ Page (`faq.json`)

**Structure**:
```json
{
  "page_type": "faq",
  "product_name": "Product Name",
  "title": "Product Name - FAQ",
  "total_questions": 15,
  "faqs": [
    {
      "question": "What is this product?",
      "answer": "Detailed answer...",
      "category": "informational"
    }
  ],
  "faqs_by_category": {
    "informational": [...],
    "usage": [...],
    "safety": [...],
    "purchase": [...],
    "comparison": [...]
  },
  "metadata": {
    "generated_at": "ISO timestamp",
    "version": "1.0"
  }
}
```

**Key Features**:
- Minimum 15 Q&A pairs
- 5 category groupings
- Auto-generated answers from logic blocks
- Searchable format

---

### 9.2 Product Page (`product_page.json`)

**Structure**:
```json
{
  "page_type": "product",
  "product_id": "unique_id",
  "product_name": "Name",
  
  "overview": {
    "title": "Overview",
    "description": "...",
    "key_points": []
  },
  
  "skin_type": {
    "title": "Suitable For",
    "primary": "Oily",
    "all_types": ["Oily", "Combination"]
  },
  
  "ingredients": {
    "title": "Key Ingredients",
    "list": [],
    "primary_ingredient": "...",
    "summary": "..."
  },
  
  "benefits": {
    "title": "Benefits",
    "list": [],
    "categorized": {}
  },
  
  "usage": {
    "title": "How to Use",
    "steps": [],
    "frequency": "Twice daily"
  },
  
  "safety": {
    "title": "Safety",
    "side_effects": [],
    "warnings": []
  },
  
  "pricing": {
    "title": "Pricing",
    "price": "₹599",
    "value_proposition": "Good"
  }
}
```

---

### 9.3 Comparison Page (`comparison_page.json`)

**Structure**:
```json
{
  "page_type": "comparison",
  "title": "Product A vs Product B",
  
  "products": {
    "product_a": {
      "name": "...",
      "concentration": "...",
      "price": "..."
    },
    "product_b": {
      "name": "...",
      "concentration": "...",
      "price": "..."
    }
  },
  
  "comparison": {
    "concentration": {
      "product_a": "10%",
      "product_b": "13%",
      "analysis": "Product B has higher concentration"
    },
    "ingredients": {
      "common": [],
      "unique_to_a": [],
      "unique_to_b": []
    },
    "pricing": {
      "difference": "Product B is ₹50 more expensive",
      "value_assessment": "Both offer good value"
    }
  },
  
  "summary": "Overall comparison summary",
  "recommendation": "Which product to choose"
}
```

---

## 10. Implementation Details

### File Structure:
```
kasparro-agentic-Vipul-Pawar/
├── agents/                      # All 7 agents
│   ├── base_agent.py
│   ├── product_parser_agent.py
│   ├── question_generator_agent.py
│   ├── comparison_agent.py
│   ├── template_engine_agent.py
│   ├── logic_blocks_processor_agent.py
│   └── page_assembly_agent.py
│
├── orchestrator/                # Workflow controller
│   └── orchestrator.py
│
├── output/                      # Generated JSON files
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
│
├── docs/                        # Documentation
│   ├── ARCHITECTURE.md
│   └── projectdocumentation.md
│
├── main.py                      # Entry point
├── sample_product.json          # Sample input
└── requirements.txt             # Dependencies
```

### Dependencies:
- Python 3.9+
- No external libraries required (pure Python)
- Uses only standard library modules

---

## 11. Usage Instructions

### Running the System:

```bash
# Install (if needed)
pip install -r requirements.txt

# Run with default sample
python main.py

# Run with custom input
python main.py --input your_product.json

# Specify output directory
python main.py --input data.json --output-dir results
```

### Expected Output:
```
==============================================================
Multi-Agent Product Content Generation System
==============================================================
Loading product data from: sample_product.json
Product: Niacinamide 10% + Zinc 1% Serum
Initializing orchestrator...

Starting content generation pipeline...

✓ Step 1: Product data parsed
✓ Step 2: Generated 17 questions
✓ Step 3: Comparison product created
✓ Step 4: Logic blocks processed
✓ Steps 5-6: All pages assembled
✓ Step 7: Output files saved

==============================================================
✓ Content Generation Completed Successfully!
==============================================================

Generated Files:
  • FAQ: output/faq.json
  • PRODUCT: output/product_page.json
  • COMPARISON: output/comparison_page.json

Statistics:
  • Product: Niacinamide 10% + Zinc 1% Serum
  • Total Questions: 17
  • Comparison Product: Niacinamide Plus

==============================================================
```

---

## 12. Future Improvements

### Phase 2 Enhancements:

1. **Multi-Product Support**
   - Batch processing
   - Product catalogs
   - Cross-product comparisons

2. **Enhanced Templates**
   - User-defined custom templates
   - Template marketplace
   - Conditional sections

3. **Advanced Logic Blocks**
   - AI-powered content generation
   - Sentiment analysis
   - SEO optimization blocks

4. **Output Formats**
   - HTML generation
   - Markdown export
   - PDF reports
   - API responses

5. **Quality Enhancements**
   - Content validation scores
   - Readability analysis
   - Grammar checking
   - SEO scoring

6. **Performance**
   - Parallel agent execution
   - Caching frequently used blocks
   - Streaming output

7. **Integration**
   - REST API
   - Webhooks
   - Database storage
   - CMS integration

8. **Analytics**
   - Content performance metrics
   - Question effectiveness
   - Comparison insights

### Scalability Improvements:
- Agent pooling
- Distributed processing
- Message queues
- Microservices architecture

---

## Conclusion

This multi-agent system demonstrates:
- ✅ **Modular architecture** with 7 specialized agents
- ✅ **Reusable components** (8 logic blocks, 3 templates)
- ✅ **Clean data flow** through orchestrated pipeline
- ✅ **Quality outputs** (3 machine-readable JSON files)
- ✅ **Scalable design** ready for future enhancements
- ✅ **No external dependencies** on internet data
- ✅ **Systematic approach** following software engineering best practices

**The system successfully transforms a simple 8-field product dataset into comprehensive, structured content pages suitable for e-commerce, documentation, or customer support applications.**

---

**Submitted for: Kasparro AI Engineer Challenge**  
**Date**: December 2025  
**Author**: Vipul Pawar
