# Multi-Agent Product Content Generation System

> **Kasparro AI Engineer Challenge Submission by Vipul Pawar**

A sophisticated multi-agent system that automatically generates structured content pages from product data using specialized AI agents, reusable logic blocks, and custom templates.

## 🎯 Challenge Overview

Build a **modular agentic system** (not a single script) that transforms product data into 3 types of JSON pages:
- **FAQ Page** (15+ Q&A pairs)
- **Product Description Page** (comprehensive product info)
- **Comparison Page** (vs fictional Product B)

### ✅ Key Requirements Met

- ✅ **7 Specialized Agents** with single responsibilities
- ✅ **Custom Template Engine** for structured content
- ✅ **8 Reusable Logic Blocks** for content processing
- ✅ **15+ Categorized Questions** (5 categories)
- ✅ **3 JSON Outputs** (machine-readable)
- ✅ **Orchestrated Workflow** (systematic pipeline)
- ✅ **No External Data** (uses only input product data)
- ✅ **Complete Documentation** (architecture + implementation)

---

## 🏗️ System Architecture

```
Raw Product Data → Parser → Question Gen + Comparison → Logic Blocks → Template Engine → Page Assembly → 3 JSON Files
```

### The 7 Agents

1. **Product Parser Agent** - Cleans and structures raw data
2. **Question Generator Agent** - Creates 15+ categorized questions  
3. **Comparison Agent** - Generates fictional Product B
4. **Template Engine Agent** - Applies structured templates
5. **Logic Blocks Processor** - Executes reusable content logic
6. **Page Assembly Agent** - Combines components into pages
7. **Orchestrator Agent** - Controls entire workflow

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- No external dependencies (pure Python)

### Installation

```bash
git clone <repository-url>
cd kasparro-agentic-Vipul-Pawar
pip install -r requirements.txt  # Optional (no external deps needed)
```

### Usage

```bash
# Run with sample product
python main.py

# Run with custom product JSON
python main.py --input your_product.json

# Specify output directory
python main.py --input data.json --output-dir results
```

### Expected Output

```
✓ Content Generation Completed Successfully!

Generated Files:
  • FAQ: output/faq.json
  • PRODUCT: output/product_page.json
  • COMPARISON: output/comparison_page.json

Statistics:
  • Total Questions: 17
  • Comparison Product: Niacinamide Plus
```

---

## 📁 Project Structure

```
kasparro-agentic-Vipul-Pawar/
├── agents/                          # 7 specialized agents
│   ├── product_parser_agent.py     
│   ├── question_generator_agent.py
│   ├── comparison_agent.py
│   ├── template_engine_agent.py
│   ├── logic_blocks_processor_agent.py
│   ├── page_assembly_agent.py
│   └── base_agent.py
│
├── orchestrator/                    # Workflow controller
│   └── orchestrator.py
│
├── output/                          # Generated JSON files
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
│
├── docs/                            # Documentation
│   ├── ARCHITECTURE.md              # System architecture details
│   ├── projectdocumentation.md      # Complete project docs
│   └── IMPLEMENTATION_GUIDE.md
│
├── main.py                          # Entry point
├── sample_product.json              # Sample input data
└── requirements.txt                 # Dependencies
```

---

## 📊 Input Format

Provide a JSON file with 8 required fields:

```json
{
  "product_name": "Niacinamide 10% + Zinc 1% Serum",
  "concentration": "10% Niacinamide, 1% Zinc",
  "skin_type": "Oily, Combination, Acne-Prone",
  "key_ingredients": "Niacinamide, Zinc PCA, Hyaluronic Acid",
  "benefits": "Reduce blemishes, Minimize pores, Control oil",
  "usage_instructions": "Apply 2-3 drops twice daily...",
  "side_effects": "Mild tingling, Temporary redness",
  "price": "₹599"
}
```

---

## 📤 Output Examples

### 1. FAQ Page (`faq.json`)
```json
{
  "page_type": "faq",
  "product_name": "Niacinamide 10% + Zinc 1% Serum",
  "total_questions": 17,
  "faqs": [
    {
      "question": "What is Niacinamide 10% + Zinc 1% Serum?",
      "answer": "A skincare serum formulated with...",
      "category": "informational"
    }
  ],
  "faqs_by_category": {
    "informational": [...],
    "usage": [...],
    "safety": [...],
    "purchase": [...],
    "comparison": [...]
  }
}
```

### 2. Product Page (`product_page.json`)
```json
{
  "page_type": "product",
  "product_name": "Niacinamide 10% + Zinc 1% Serum",
  "overview": { "description": "...", "key_points": [] },
  "skin_type": { "primary": "Oily", "all_types": [] },
  "ingredients": { "list": [], "primary": "Niacinamide" },
  "benefits": { "list": [], "categorized": {} },
  "usage": { "steps": [], "frequency": "Twice daily" },
  "safety": { "side_effects": [], "warnings": [] },
  "pricing": { "price": "₹599", "value_proposition": "Good" }
}
```

### 3. Comparison Page (`comparison_page.json`)
```json
{
  "page_type": "comparison",
  "title": "Niacinamide Serum vs Niacinamide Plus",
  "products": {
    "product_a": { "name": "...", "concentration": "10%", "price": "₹599" },
    "product_b": { "name": "...", "concentration": "13%", "price": "₹699" }
  },
  "comparison": {
    "concentration": { "analysis": "Product B has higher concentration" },
    "ingredients": { "common": [], "unique_to_a": [], "unique_to_b": [] },
    "pricing": { "difference": "Product B is ₹100 more expensive" }
  },
  "recommendation": "Product A recommended for budget-conscious consumers"
}
```

---

## 🎨 System Highlights

### Multi-Agent Design
Each agent has **single responsibility** and operates independently:
- Receives specific input
- Performs focused task
- Returns structured output
- No cross-agent dependencies

### Reusable Logic Blocks
8 logic blocks handle content generation:
- `overview_block` - Product summary
- `benefits_block` - Benefits formatting
- `usage_block` - Usage instructions
- `ingredients_block` - Ingredient details
- `safety_block` - Safety warnings
- `pricing_block` - Price presentation
- `skin_type_block` - Skin compatibility
- `comparison_block` - Comparison analysis

### Custom Templates
3 structured templates define page layouts:
- FAQ Template (Q&A structure)
- Product Template (7 sections)
- Comparison Template (side-by-side matrix)

### Orchestrated Workflow
Sequential pipeline with validation:
1. Parse → 2. Generate → 3. Compare → 4. Process → 5. Assemble → 6. Output

---

## 📚 Documentation

- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Detailed system architecture
- **[projectdocumentation.md](docs/projectdocumentation.md)** - Complete project documentation
- **[IMPLEMENTATION_GUIDE.md](docs/IMPLEMENTATION_GUIDE.md)** - Implementation details

---

## 🧪 Testing

Test with sample data:
```bash
python main.py
```

Test with custom data:
```bash
python main.py --input test_product.json
```

View generated files:
```bash
cat output/faq.json | python -m json.tool
cat output/product_page.json | python -m json.tool
cat output/comparison_page.json | python -m json.tool
```

---

## 🔄 How It Works

### Step-by-Step Process:

1. **Input**: Provide product JSON with 8 fields
2. **Parser**: Validates and structures data
3. **Question Gen**: Creates 15+ categorized questions
4. **Comparison**: Generates realistic Product B
5. **Logic Blocks**: Processes content with 8 blocks
6. **Templates**: Applies 3 page templates
7. **Assembly**: Combines all components
8. **Output**: Saves 3 JSON files

### Data Flow:
```
Product Data
    ↓
[Parser Agent] → Structured Data
    ↓
[Question Agent] → 15+ Questions
[Comparison Agent] → Product B
    ↓
[Logic Blocks] → 8 Content Blocks
    ↓
[Template Engine] → 3 Templates
    ↓
[Page Assembly] → 3 Complete Pages
    ↓
Output: faq.json, product_page.json, comparison_page.json
```

---

## 🎯 Key Features

✨ **Fully Modular** - Each agent is independent  
✨ **No External Data** - Uses only input product data  
✨ **Systematic Approach** - Orchestrated workflow  
✨ **Reusable Components** - Logic blocks & templates  
✨ **Clean Output** - Machine-readable JSON  
✨ **Extensible** - Easy to add new agents/blocks  
✨ **Well Documented** - Comprehensive docs included  
✨ **Production Ready** - Error handling & logging  

---

## 🚀 Future Enhancements

- [ ] Multi-product batch processing
- [ ] Custom template creation
- [ ] HTML/PDF export
- [ ] REST API interface
- [ ] AI-powered content enhancement
- [ ] Multi-language support
- [ ] Content quality scoring

---

## 📝 License

MIT License

---

## 👤 Author

**Vipul Pawar**  
Kasparro AI Engineer Challenge Submission

---

## 🙏 Acknowledgments

Built for the Kasparro AI Engineer Challenge - demonstrating modular multi-agent system design, reusable component architecture, and systematic content generation.

---

**⭐ Star this project if you find it helpful!**
