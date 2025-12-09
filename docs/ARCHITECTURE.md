# Multi-Agent Product Content Generation System - Architecture

## 🎯 **System Overview**

This is a **modular multi-agent system** that transforms product data into structured JSON pages without external data sources.

### **Core Principle**
- **Input**: Single product dataset (8 fields)
- **Process**: 7+ specialized agents working in orchestrated pipeline
- **Output**: 3 JSON pages (FAQ, Product, Comparison)

---

## 🏗️ **System Architecture**

```
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR AGENT                        │
│  - Controls workflow                                         │
│  - Manages agent communication                               │
│  - Ensures data flow integrity                               │
└────────────┬────────────────────────────────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
┌───▼────────────┐   ┌▼──────────────────┐
│ Product Parser │   │ Question Generator │
│    Agent       │   │      Agent         │
└───┬────────────┘   └┬──────────────────┘
    │                 │
    │    ┌────────────┴─────────┐
    │    │                      │
┌───▼────▼─────┐   ┌───────────▼────────┐
│ Comparison   │   │ Template Engine    │
│    Agent     │   │      Agent         │
└───┬──────────┘   └┬───────────────────┘
    │               │
    │  ┌────────────┴──────────┐
    │  │                       │
┌───▼──▼──────────┐  ┌────────▼─────────┐
│ Logic Blocks    │  │ Page Assembly    │
│   Processor     │  │     Agent        │
└─────────────────┘  └──────┬───────────┘
                             │
                    ┌────────▼──────────┐
                    │  Final JSON Pages │
                    │  - FAQ            │
                    │  - Product        │
                    │  - Comparison     │
                    └───────────────────┘
```

---

## 🤖 **Agent Specifications**

### **1. Product Parser Agent**
**Purpose**: Clean and structure raw product data  
**Input**: Raw product dictionary  
**Output**: Validated, structured JSON  
**Responsibilities**:
- Validate all required fields
- Normalize data formats
- Extract metadata
- Create internal product schema

### **2. Question Generator Agent**
**Purpose**: Generate user questions from product data  
**Input**: Structured product data  
**Output**: 15+ categorized questions  
**Categories**:
- Informational (what is this?)
- Usage (how to use?)
- Safety (side effects?)
- Purchase (pricing?)
- Comparison (vs others?)

### **3. Comparison Agent**
**Purpose**: Create fictional Product B for comparison  
**Input**: Product A data  
**Output**: Product B data + comparison matrix  
**Logic**:
- Generate similar but different product
- Different concentration
- Different ingredients
- Different price point
- Maintain realistic differences

### **4. Template Engine Agent**
**Purpose**: Apply structured templates to data  
**Input**: Template ID + data  
**Output**: Populated template structure  
**Templates**:
- FAQ Template
- Product Page Template
- Comparison Page Template

### **5. Logic Blocks Processor Agent**
**Purpose**: Execute reusable content logic  
**Input**: Block ID + data  
**Output**: Processed content section  
**Blocks**:
- benefits_block()
- usage_block()
- ingredients_block()
- safety_warnings_block()
- pricing_block()
- comparison_block()

### **6. Page Assembly Agent**
**Purpose**: Combine all components into final pages  
**Input**: Templates + Logic Blocks + Data  
**Output**: Complete JSON pages  
**Process**:
- Merge template with content
- Apply logic blocks
- Validate structure
- Format output

### **7. Orchestrator Agent**
**Purpose**: Control entire workflow  
**Input**: Raw product data  
**Output**: 3 final JSON files  
**Responsibilities**:
- Initialize agents
- Manage execution sequence
- Handle agent communication
- Ensure data consistency
- Error handling

---

## 📊 **Data Flow Diagram**

```
Raw Product Data
      │
      ▼
┌─────────────────┐
│ Product Parser  │
└─────┬───────────┘
      │
      ├──► Cleaned Product Data
      │
      ▼
┌────────────────────┐
│ Question Generator │
└─────┬──────────────┘
      │
      ├──► 15+ Questions
      │
      ▼
┌─────────────────┐
│ Comparison Agent│
└─────┬───────────┘
      │
      ├──► Product B Data
      │
      ▼
┌──────────────────────┐
│ Template Engine      │
└─────┬────────────────┘
      │
      ├──► Template Structures
      │
      ▼
┌──────────────────────┐
│ Logic Blocks Process │
└─────┬────────────────┘
      │
      ├──► Content Blocks
      │
      ▼
┌──────────────────┐
│ Page Assembly    │
└─────┬────────────┘
      │
      ├──► faq.json
      ├──► product_page.json
      └──► comparison_page.json
```

---

## 🏛️ **Template System Design**

### **Template Structure**
```json
{
  "template_id": "string",
  "template_type": "faq|product|comparison",
  "sections": [
    {
      "section_id": "string",
      "section_type": "string",
      "required_data": ["field1", "field2"],
      "logic_block": "block_name",
      "format": "string"
    }
  ],
  "metadata": {}
}
```

### **Template Placeholders**
- `{{product.name}}`
- `{{product.concentration}}`
- `{{logic.benefits}}`
- `{{logic.usage}}`

### **Template Rendering Process**
1. Load template by ID
2. Validate required data fields
3. Execute logic blocks
4. Replace placeholders
5. Return structured content

---

## 🧩 **Logic Blocks Architecture**

### **Logic Block Interface**
```python
class LogicBlock:
    def execute(self, data: dict) -> dict:
        pass
    
    def validate_input(self, data: dict) -> bool:
        pass
    
    def format_output(self, result: any) -> dict:
        pass
```

### **Available Logic Blocks**

1. **BenefitsBlock**
   - Input: key_ingredients, benefits
   - Output: Formatted benefits section

2. **UsageBlock**
   - Input: usage_instructions, skin_type
   - Output: Step-by-step usage guide

3. **IngredientsBlock**
   - Input: key_ingredients, concentration
   - Output: Ingredient breakdown

4. **SafetyBlock**
   - Input: side_effects, skin_type
   - Output: Safety warnings & precautions

5. **PricingBlock**
   - Input: price, concentration
   - Output: Pricing details & value analysis

6. **ComparisonBlock**
   - Input: product_a, product_b
   - Output: Side-by-side comparison

---

## 🔄 **Orchestration Flow**

### **Execution Sequence**
```
1. START
2. Orchestrator.initialize()
3. ProductParser.parse(raw_data)
4. QuestionGenerator.generate(parsed_data)
5. ComparisonAgent.create_product_b(parsed_data)
6. TemplateEngine.load_templates()
7. LogicBlocksProcessor.process_all_blocks(data)
8. PageAssembly.assemble_faq(questions, templates, blocks)
9. PageAssembly.assemble_product(data, templates, blocks)
10. PageAssembly.assemble_comparison(product_a, product_b, templates, blocks)
11. Orchestrator.save_outputs()
12. END
```

### **State Management**
- Each agent receives immutable input
- Each agent returns new output
- No shared state between agents
- Orchestrator maintains execution context

---

## 📁 **Project Structure**

```
kasparro-agentic-Vipul-Pawar/
├── agents/
│   ├── __init__.py
│   ├── product_parser_agent.py
│   ├── question_generator_agent.py
│   ├── comparison_agent.py
│   ├── template_engine_agent.py
│   ├── logic_blocks_processor_agent.py
│   ├── page_assembly_agent.py
│   └── base_agent.py
│
├── logic_blocks/
│   ├── __init__.py
│   ├── benefits_block.py
│   ├── usage_block.py
│   ├── ingredients_block.py
│   ├── safety_block.py
│   ├── pricing_block.py
│   └── comparison_block.py
│
├── templates/
│   ├── faq_template.json
│   ├── product_page_template.json
│   └── comparison_template.json
│
├── orchestrator/
│   ├── __init__.py
│   └── orchestrator.py
│
├── output/
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── projectdocumentation.md
│   └── AGENT_SPECIFICATIONS.md
│
├── data/
│   └── sample_product.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🎨 **Design Principles**

### **1. Modularity**
- Each agent is self-contained
- Clear interfaces between components
- Easy to add/remove agents

### **2. Reusability**
- Logic blocks are composable
- Templates are data-agnostic
- Agents can be used independently

### **3. Maintainability**
- Single Responsibility Principle
- Clear documentation
- Type hints and validation

### **4. Scalability**
- Stateless agents
- Parallel execution ready
- Easy to add new product types

---

## 🔒 **Constraints & Assumptions**

### **Constraints**
- NO external data sources
- NO internet lookups
- NO hardcoded content
- ONLY product dataset

### **Assumptions**
- Product data is complete
- All 8 fields are provided
- Data is in valid format
- Single product processing

---

## 🚀 **Future Enhancements**

1. **Multi-product Support**: Batch processing
2. **Custom Templates**: User-defined templates
3. **More Logic Blocks**: Expandable block library
4. **AI Integration**: LLM for question generation
5. **Validation Layer**: Enhanced data validation
6. **Export Formats**: HTML, Markdown, PDF
7. **Analytics**: Content quality metrics
8. **Caching**: Template and block caching

---

**Built for Kasparro AI Engineer Challenge**
