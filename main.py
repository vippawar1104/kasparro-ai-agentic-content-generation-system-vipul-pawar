"""
Main Entry Point for Multi-Agent Product Content Generation System

Usage:
    python main.py
    python main.py --input sample_product.json
"""

import json
import logging
import argparse
from pathlib import Path
from orchestrator import Orchestrator


def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('content_generation.log')
        ]
    )


def load_product_data(file_path: str) -> dict:
    """Load product data from JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Multi-Agent Product Content Generation System'
    )
    parser.add_argument(
        '--input',
        type=str,
        default='sample_product.json',
        help='Path to input product JSON file'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='output',
        help='Directory to save output files'
    )
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("="*60)
    logger.info("Multi-Agent Product Content Generation System")
    logger.info("="*60)
    
    try:
        # Load product data
        logger.info(f"Loading product data from: {args.input}")
        product_data = load_product_data(args.input)
        logger.info(f"Product: {product_data.get('product_name', 'Unknown')}")
        
        # Initialize orchestrator
        logger.info("Initializing orchestrator...")
        orchestrator = Orchestrator(output_dir=args.output_dir)
        
        # Generate all pages
        logger.info("\nStarting content generation pipeline...\n")
        result = orchestrator.generate_all_pages(product_data)
        
        if result['success']:
            logger.info("\n" + "="*60)
            logger.info("✓ Content Generation Completed Successfully!")
            logger.info("="*60)
            logger.info("\nGenerated Files:")
            for page_type, file_path in result['output_files'].items():
                logger.info(f"  • {page_type.upper()}: {file_path}")
            
            logger.info("\nStatistics:")
            stats = result['statistics']
            logger.info(f"  • Product: {stats['product_name']}")
            logger.info(f"  • Total Questions: {stats['total_questions']}")
            logger.info(f"  • Comparison Product: {stats['comparison_product']}")
            
            logger.info("\n" + "="*60)
            logger.info("Check the output directory for generated JSON files")
            logger.info("="*60)
            
        else:
            logger.error(f"\n✗ Content generation failed: {result.get('error')}")
            return 1
        
        return 0
        
    except FileNotFoundError:
        logger.error(f"Input file not found: {args.input}")
        logger.error("Please provide a valid product JSON file")
        return 1
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in input file: {args.input}")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return 1


if __name__ == "__main__":
    exit(main())
