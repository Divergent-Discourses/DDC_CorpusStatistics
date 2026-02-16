"""Command-line interface for DD Corpus Tools"""

import sys
import os
from pathlib import Path

from .analyzer import NewspaperCorpusAnalyzer
from .advanced_analyzer import AdvancedCorpusAnalyzer
from .excel_exporter import ConsolidatedExporter
from .library_reporter import LibraryHoldingsReporter
from .utilities import validate_filename, batch_validate_files


def main_analyze():
    """Main entry point for dd-analyze command"""
    if len(sys.argv) < 2:
        print("Usage: dd-analyze <corpus_root_directory>")
        print("\nGenerates comprehensive corpus statistics including:")
        print("  • Newspaper list with sources")
        print("  • Library holdings by newspaper, year, and issue")
        print("  • Missing issues estimates")
        print("  • Year-by-year coverage")
        print("\nExample: dd-analyze /path/to/newspaper/corpus")
        sys.exit(1)
    
    corpus_path = sys.argv[1]
    
    if not os.path.exists(corpus_path):
        print(f"Error: Directory not found: {corpus_path}")
        sys.exit(1)
    
    analyzer = NewspaperCorpusAnalyzer(corpus_path)
    analyzer.run_full_analysis()


def main_advanced():
    """Main entry point for dd-analyze-advanced command"""
    if len(sys.argv) < 2:
        print("Usage: dd-analyze-advanced <corpus_root_directory>")
        print("\nGenerates detailed analysis with:")
        print("  • All basic analysis features")
        print("  • Page-level completeness checking")
        print("  • Duplicate page detection")
        print("  • Monthly statistics")
        print("  • Multiple CSV exports")
        print("\nExample: dd-analyze-advanced /path/to/newspaper/corpus")
        sys.exit(1)
    
    corpus_path = sys.argv[1]
    
    if not os.path.exists(corpus_path):
        print(f"Error: Directory not found: {corpus_path}")
        sys.exit(1)
    
    analyzer = AdvancedCorpusAnalyzer(corpus_path)
    analyzer.run_advanced_analysis()


def main_excel():
    """Main entry point for dd-excel-export command"""
    if len(sys.argv) < 2:
        print("Usage: dd-excel-export <corpus_root_directory>")
        print("\nGenerates Excel-optimized exports:")
        print("  • corpus_pivot_table_data.csv - Single CSV for pivot tables")
        print("  • corpus_analysis_workbook.xlsx - Multi-sheet Excel workbook")
        print("\nPerfect for creating pivot tables and charts in Excel!")
        print("\nExample: dd-excel-export /path/to/newspaper/corpus")
        sys.exit(1)
    
    corpus_path = sys.argv[1]
    
    if not os.path.exists(corpus_path):
        print(f"Error: Directory not found: {corpus_path}")
        sys.exit(1)
    
    exporter = ConsolidatedExporter(corpus_path)
    exporter.export_all()


def main_reports():
    """Main entry point for dd-reports command"""
    if len(sys.argv) < 2:
        print("Usage: dd-reports <corpus_root_directory>")
        print("\nGenerates detailed text reports:")
        print("  • library_holdings_report.txt - Comprehensive library holdings")
        print("  • missing_issues_report.txt - Detailed gap analysis")
        print("\nExample: dd-reports /path/to/newspaper/corpus")
        sys.exit(1)
    
    corpus_path = sys.argv[1]
    
    if not os.path.exists(corpus_path):
        print(f"Error: Directory not found: {corpus_path}")
        sys.exit(1)
    
    reporter = LibraryHoldingsReporter(corpus_path)
    reporter.generate_combined_report()


def main_validate():
    """Main entry point for dd-validate command"""
    if len(sys.argv) < 2:
        print("Usage: dd-validate <directory>")
        print("\nValidates all filenames in a directory against the expected pattern:")
        print("  XXX_YYYY_MM_DD_ppp_LL_abcd.ext")
        print("\nExample: dd-validate /path/to/newspaper/corpus")
        sys.exit(1)
    
    directory = sys.argv[1]
    
    if not os.path.exists(directory):
        print(f"Error: Directory not found: {directory}")
        sys.exit(1)
    
    print("Validating filenames...")
    results = batch_validate_files(directory)
    
    print(f"\nValidation Results:")
    print(f"  Valid files: {len(results['valid'])}")
    print(f"  Invalid files: {len(results['invalid'])}")
    
    if results['invalid']:
        print(f"\nInvalid files (first 20):")
        for item in results['invalid'][:20]:
            print(f"  {item['file']}")
            print(f"    Error: {item['error']}")
        
        if len(results['invalid']) > 20:
            print(f"  ... and {len(results['invalid']) - 20} more")
    
    if results['suggestions']:
        print(f"\nSuggested fixes available for {len(results['suggestions'])} files")


if __name__ == '__main__':
    print("This module should be run via the installed commands:")
    print("  dd-analyze")
    print("  dd-analyze-advanced")
    print("  dd-excel-export")
    print("  dd-reports")
    print("  dd-validate")
