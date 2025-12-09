# Multi-Agent Product Content Generation System

> **Kasparro AI Engineer Challenge Submission**  
> **By: Vipul Pawar**

A production-grade modular agentic automation system that transforms minimal product data into comprehensive, structured JSON content pages through orchestrated multi-agent workflows.

---

## 🎯 Challenge Objective

Design and implement a **modular agentic automation system** that demonstrates:
- Multi-agent workflows with clear boundaries
- Automation graphs and orchestration
- Reusable content logic blocks
- Template-based generation
- Structured JSON output
- System abstraction & documentation

**This is NOT**: A prompting assignment, LLM wrapper, content writing test, or UI challenge.  
**This IS**: A systems design + automation + agent orchestration challenge.

---

## 📦 Input Data

The system operates on **GlowBoost Vitamin C Serum** product data:

```json
{
  "product_name": "GlowBoost Vitamin C Serum",
  "concentration": "10% Vitamin C",
  "skin_type": "Oily, Combination",
  "key_ingredients": "Vitamin C, Hyaluronic Acid",
  "benefits": "Brightening, Fades dark spots",
  "usage_instructions": "Apply 2–3 drops in the morning before sunscreen",
  "side_effects": "Mild tingling for sensitive skin",
  "price": "₹699"
}
```

**Constraint**: No external data or research allowed. System must work with this data type only.

---

## ✅ Requirements Met

### 1. **Parse & Understand Product Data** ✓
- `ProductParserAgent` converts raw data into clean internal model
- Validates 8 required fields
- Structures data with proper typing and categorization

### 2. **Generate 15+ Categorized Questions** ✓
- System generates **25 questions** (exceeds requirement)
- 5 categories: Informational, Usage, Safety, Purchase, Comparison
- Automatic categorization and context-aware generation

### 3. **Custom Templates** ✓
- **FAQ Template**: Q&A structure with category grouping
- **Product Page Template**: 7-section comprehensive layout
- **Comparison Template**: Side-by-side analysis matrix

### 4. **Reusable Logic Blocks** ✓
8 modular content processing blocks:
- `benefits_block` - Benefits categorization
- `usage_block` - Usage instructions formatting
- `ingredients_block` - Ingredient details
- `safety_block` - Safety warnings generation
- `pricing_block` - Price presentation & value analysis
- `comparison_block` - Comparison matrix creation
- `overview_block` - Product summary
- `skin_type_block` - Skin compatibility

### 5. **Assemble 3 Pages** ✓
- **FAQ Page**: 15 Q&A pairs minimum (generates 15)
- **Product Page**: Complete product description
- **Comparison Page**: GlowBoost vs GlowBoost Premium (fictional)

### 6. **Machine-Readable JSON Output** ✓
All outputs are clean, structured JSON:
- `output/faq.json`
- `output/product_page.json`
- `output/comparison_page.json`

### 7. **Agent Pipeline** ✓
7 specialized agents, not a monolith:
- Product Parser Agent
- Question Generator Agent
- Comparison Agent
- Template Engine Agent
- Logic Blocks Processor Agent
- Page Assembly Agent
- Orchestrator Agent

---

## 🏗️ System Architecture

### **Multi-Agent Workflow (DAG Pipeline)**

```
Raw Product Data
      ↓
[Product Parser Agent] → Structured Data
      ↓
      ├─→ [Question Generator] → 25 Questions
      └─→ [Comparison Agent] → Product B
      ↓
[Logic Blocks Processor] → 8 Content Blocks
      ↓
[Template Engine] → 3 Populated Templates
      ↓
[Page Assembly Agent] → 3 Complete JSON Pages
      ↓
Output: faq.json, product_page.json, comparison_page.json
```

### **Agent Boundaries**

Each agent has:
- ✅ Single responsibility
- ✅ Defined input/output contracts
- ✅ No hidden global state
- ✅ Independent operation
- ✅ Error handling & validation

### **Orchestration Flow**

Sequential DAG pipeline managed by Orchestrator:
1. **Parse** → Validate & structure product data
2. **Generate** → Create questions & comparison product
3. **Process** → Execute logic blocks on data
4. **Template** → Apply structured templates
5. **Assemble** → Combine components into pages
6. **Output** → Save JSON files

---

## 📁 Project Structure

```
kasparro-ai-agentic-content-generation-system-vipul-pawar/
├── agents/                          # 7 Specialized Agents
│   ├── base_agent.py               # Base agent interface
│   ├── product_parser_agent.py     # Data parsing & validation
│   ├── question_generator_agent.py # Question generation
│   ├── comparison_agent.py         # Product B creation
│   ├── template_engine_agent.py    # Template application
│   ├── logic_blocks_processor_agent.py # Logic execution
│   └── page_assembly_agent.py      # Final page assembly
│
├── logic_blocks/                    # 8 Reusable Logic Blocks
│   ├── benefits_block.py
│   ├── usage_block.py
│   ├── ingredients_block.py
│   ├── safety_block.py
│   ├── pricing_block.py
│   ├── comparison_block.py
│   ├── overview_block.py
│   └── skin_type_block.py
│
├── templates/                       # 3 Custom Templates
│   ├── faq_template.json
│   ├── product_page_template.json
│   └── comparison_template.json
│
├── orchestrator/                    # Workflow Controller
│   └── orchestrator.py
│
├── output/                          # Generated JSON Files
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
│
├── docs/                            # Documentation
│   ├── ARCHITECTURE.md
│   └── projectdocumentation.md
│
├── main.py                          # Entry point
├── sample_product.json              # Input data
└── requirements.txt                 # Dependencies
```

---

## 🚀 Quick Start

### **Prerequisites**
- Python 3.9+
- No external dependencies (pure Python)

### **Installation**
```bash
git clone https://github.com/vippawar1104/kasparro-ai-agentic-content-generation-system-vipul-pawar.git
cd kasparro-ai-agentic-content-generation-system-vipul-pawar
```

### **Usage**

**Run with default sample:**
```bash
python3 main.py
```

**Run with custom product:**
```bash
python3 main.py --input your_product.json
```

**Specify output directory:**
```bash
python3 main.py --input sample_product.json --output-dir results
```

### **Expected Output**
```
============================================================
Multi-Agent Product Content Generation System
============================================================
Product: GlowBoost Vitamin C Serum

✓ Step 1: Product data parsed
✓ Step 2: Generated 25 questions
✓ Step 3: Comparison product created
✓ Step 4: Logic blocks processed
✓ Steps 5-6: All pages assembled
✓ Step 7: Output files saved

Generated Files:
  • FAQ: output/faq.json
  • PRODUCT: output/product_page.json
  • COMPARISON: output/comparison_page.json

Statistics:
  • Total Questions: 25
  • Comparison Product: GlowBoost Premium
============================================================
```

**Execution Time**: < 0.01 seconds ⚡

---

## 📊 Output Examples

### **FAQ Page** (`faq.json`)
```json
{
  "page_type": "faq",
  "product_name": "GlowBoost Vitamin C Serum",
  "total_questions": 15,
  "faqs": [
    {
      "question": "What is GlowBoost Vitamin C Serum?",
      "answer": "GlowBoost Vitamin C Serum is formulated with...",
      "category": "informational"
    }
  ],
  "faqs_by_category": {
    "informational": [...],
    "usage": [...],
    "safety": [...]
  }
}
```

### **Product Page** (`product_page.json`)
```json
{
  "page_type": "product",
  "product_name": "GlowBoost Vitamin C Serum",
  "overview": {...},
  "skin_type": {...},
  "ingredients": {...},
  "benefits": {...},
  "usage": {...},
  "safety": {...},
  "pricing": {...}
}
```

### **Comparison Page** (`comparison_page.json`)
```json
{
  "page_type": "comparison",
  "title": "GlowBoost Vitamin C Serum vs GlowBoost Premium",
  "products": {
    "product_a": {...},
    "product_b": {...}
  },
  "comparison": {
    "concentration": {...},
    "ingredients": {...},
    "benefits": {...},
    "pricing": {...}
  },
  "recommendation": "..."
}
```

---

## 🎨 System Highlights

### **1. Modular Agent Design**
- Each agent operates independently
- Clear input/output contracts
- No cross-agent dependencies
- Stateless execution

### **2. Reusable Logic Blocks**
- Composable content functions
- Template-agnostic processing
- Single source of truth
- Easy to extend

### **3. Custom Template Engine**
- Structured JSON templates
- Field validation
- Logic block integration
- Placeholder replacement

### **4. Orchestrated Workflow**
- Sequential DAG pipeline
- Error handling at each step
- Comprehensive logging
- Metadata tracking

### **5. Production-Ready**
- Type hints throughout
- Comprehensive error handling
- Detailed logging
- Clean code structure

---

## 📚 Documentation

- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Detailed system architecture
- **[projectdocumentation.md](docs/projectdocumentation.md)** - Complete project documentation
  - Problem Statement
  - Solution Overview
  - Scopes & Assumptions
  - System Design
  - Implementation Details

---

## 🧮 Evaluation Criteria Alignment

| Criteria | Weight | Implementation |
|----------|--------|----------------|
| **Agentic System Design** | 45% | ✅ Clear responsibilities, modular, extensible, correct flow |
| **Types & Quality of Agents** | 25% | ✅ 7 meaningful agents with appropriate boundaries |
| **Content System Engineering** | 20% | ✅ Quality templates, logic blocks, composability |
| **Data & Output Structure** | 10% | ✅ Valid JSON, clean data mapping |

---

## 🔧 Technical Stack

- **Language**: Python 3.9+
- **Architecture**: Multi-agent orchestration
- **Design Pattern**: DAG pipeline with message passing
- **Data Format**: JSON
- **Dependencies**: None (pure Python standard library)

---

## 🎯 Key Features

✨ **7 Specialized Agents** - Single responsibility principle  
✨ **8 Logic Blocks** - Reusable content processing  
✨ **3 Templates** - Structured page definitions  
✨ **25+ Questions** - Automatic generation & categorization  
✨ **3 JSON Outputs** - Machine-readable pages  
✨ **DAG Pipeline** - Orchestrated workflow  
✨ **Zero External Deps** - Pure Python implementation  
✨ **< 0.01s Execution** - Lightning fast  

---

## 🚫 What This Is NOT

- ❌ Not a prompting assignment
- ❌ Not a single LLM wrapper function
- ❌ Not a content writing test
- ❌ Not a UI/website challenge

**This IS**: A production-style agentic system demonstrating modular design, orchestration, and systematic automation.

---

## 📝 License

MIT License

---

## 👤 Author

**Vipul Pawar**  
Kasparro AI Engineer Challenge Submission

---

## 🙏 Acknowledgments

Built for the Kasparro AI Engineer Challenge - demonstrating production-style multi-agent system design, reusable component architecture, and systematic content generation.

---

**⭐ Star this repository if you find it helpful!**
