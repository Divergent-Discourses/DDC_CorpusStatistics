#!/usr/bin/env python3
"""
Corpus Utilities
Helper functions for working with the newspaper corpus
"""

import os
from pathlib import Path
from collections import defaultdict
import re

from .constants import NEWSPAPER_NAMES, VALID_EXTENSIONS, FILENAME_PATTERN


def validate_filename(filename):
    """
    Validate if a filename matches the expected pattern
    Returns: (is_valid, error_message)
    """
    # Remove extension
    name = Path(filename).stem
    
    if not re.match(FILENAME_PATTERN, name):
        # Provide specific error feedback
        parts = name.split('_')
        
        if len(parts) < 6:
            return False, f"Too few parts (expected at least 6, got {len(parts)})"
        
        # Check newspaper code
        if len(parts[0]) != 3 or not parts[0].isupper():
            return False, f"Invalid newspaper code '{parts[0]}' (must be 3 uppercase letters)"
        
        # Check year
        if not (parts[1].isdigit() and len(parts[1]) == 4):
            return False, f"Invalid year '{parts[1]}' (must be 4 digits)"
        
        # Check month
        if not (parts[2].isdigit() and len(parts[2]) == 2 and 1 <= int(parts[2]) <= 12):
            return False, f"Invalid month '{parts[2]}' (must be 2 digits, 01-12)"
        
        # Check day
        if not (parts[3].isdigit() and len(parts[3]) == 2 and 1 <= int(parts[3]) <= 31):
            return False, f"Invalid day '{parts[3]}' (must be 2 digits, 01-31)"
        
        # Check page
        if not (parts[4].isdigit() and len(parts[4]) == 3):
            return False, f"Invalid page number '{parts[4]}' (must be 3 digits)"
        
        # Check library code
        if len(parts[5]) != 2 or not parts[5].isupper():
            return False, f"Invalid library code '{parts[5]}' (must be 2 uppercase letters)"
        
        return False, "Unknown error in filename format"
    
    return True, "Valid"


def generate_filename(newspaper_code, year, month, day, page, library_code, 
                      shelfmark='', extension='.jpg'):
    """
    Generate a properly formatted filename
    
    Args:
        newspaper_code: 3-letter code (e.g., 'TID')
        year: 4-digit year (e.g., 1964)
        month: month number (1-12)
        day: day number (1-31)
        page: page number (1-999)
        library_code: 2-letter code (e.g., 'SB')
        shelfmark: optional shelfmark string
        extension: file extension (default .jpg)
    
    Returns:
        Formatted filename string
    """
    # Validate inputs
    if len(newspaper_code) != 3 or not newspaper_code.isupper():
        raise ValueError("Newspaper code must be 3 uppercase letters")
    
    if not (1000 <= year <= 9999):
        raise ValueError("Year must be 4 digits")
    
    if not (1 <= month <= 12):
        raise ValueError("Month must be 1-12")
    
    if not (1 <= day <= 31):
        raise ValueError("Day must be 1-31")
    
    if not (1 <= page <= 999):
        raise ValueError("Page must be 1-999")
    
    if len(library_code) != 2 or not library_code.isupper():
        raise ValueError("Library code must be 2 uppercase letters")
    
    # Format filename
    filename = f"{newspaper_code}_{year:04d}_{month:02d}_{day:02d}_{page:03d}_{library_code}"
    
    if shelfmark:
        filename += f"_{shelfmark}"
    
    filename += extension
    
    return filename


def find_missing_pages_in_issue(corpus_root, newspaper_code, year, month, day):
    """
    Find missing page numbers for a specific issue
    
    Returns: list of missing page numbers
    """
    from newspaper_corpus_analyzer import NewspaperCorpusAnalyzer
    
    analyzer = NewspaperCorpusAnalyzer(corpus_root)
    analyzer.scan_corpus()
    
    date = f"{year:04d}-{month:02d}-{day:02d}"
    
    if date not in analyzer.issues_detail[newspaper_code]:
        return None  # Issue not found
    
    pages = sorted(analyzer.issues_detail[newspaper_code][date])
    expected_pages = set(range(1, max(pages) + 1))
    missing_pages = sorted(expected_pages - set(pages))
    
    return missing_pages


def list_newspapers_in_corpus(corpus_root):
    """
    List all newspapers found in the corpus
    
    Returns: dict mapping newspaper codes to issue counts
    """
    from newspaper_corpus_analyzer import NewspaperCorpusAnalyzer
    
    analyzer = NewspaperCorpusAnalyzer(corpus_root)
    analyzer.scan_corpus()
    
    newspapers = {}
    for code in sorted(analyzer.data.keys()):
        newspapers[code] = {
            'name': NEWSPAPER_NAMES.get(code, f'Unknown ({code})'),
            'issues': len(analyzer.issues[code]),
            'pages': analyzer.pages_by_newspaper[code]
        }
    
    return newspapers


def find_issues_by_date_range(corpus_root, newspaper_code, start_date, end_date):
    """
    Find all issues for a newspaper within a date range
    
    Args:
        corpus_root: path to corpus
        newspaper_code: 3-letter newspaper code
        start_date: start date as 'YYYY-MM-DD' string
        end_date: end date as 'YYYY-MM-DD' string
    
    Returns: list of issue dates in range
    """
    from newspaper_corpus_analyzer import NewspaperCorpusAnalyzer
    from datetime import datetime
    
    analyzer = NewspaperCorpusAnalyzer(corpus_root)
    analyzer.scan_corpus()
    
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    
    issues_in_range = []
    for date_str in sorted(analyzer.issues[newspaper_code]):
        date = datetime.strptime(date_str, '%Y-%m-%d')
        if start <= date <= end:
            issues_in_range.append(date_str)
    
    return issues_in_range


def generate_citation_report(corpus_root, output_file='citations.txt'):
    """
    Generate a report suitable for citations/references
    """
    from newspaper_corpus_analyzer import NewspaperCorpusAnalyzer
    
    analyzer = NewspaperCorpusAnalyzer(corpus_root)
    analyzer.scan_corpus()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("DIVERGENT DISCOURSES CORPUS - NEWSPAPER HOLDINGS\n")
        f.write("=" * 80 + "\n\n")
        
        for newspaper in sorted(analyzer.data.keys()):
            name = NEWSPAPER_NAMES.get(newspaper, newspaper)
            years = sorted(analyzer.data[newspaper].keys())
            issues = len(analyzer.issues[newspaper])
            pages = analyzer.pages_by_newspaper[newspaper]
            
            f.write(f"{name}\n")
            f.write(f"  Code: {newspaper}\n")
            f.write(f"  Holdings: {min(years)}-{max(years)}\n")
            f.write(f"  Issues: {issues}\n")
            f.write(f"  Pages: {pages}\n")
            f.write("\n")
    
    print(f"Citation report saved to: {output_file}")


def batch_validate_files(directory, fix_minor_errors=False):
    """
    Validate all files in a directory
    
    Args:
        directory: path to check
        fix_minor_errors: if True, suggest corrected filenames
    
    Returns: dict with validation results
    """
    results = {
        'valid': [],
        'invalid': [],
        'suggestions': {}
    }
    
    for filepath in Path(directory).rglob('*'):
        if not filepath.is_file():
            continue
        
        if filepath.suffix.lower() not in VALID_EXTENSIONS:
            continue
        
        is_valid, message = validate_filename(filepath.name)
        
        if is_valid:
            results['valid'].append(str(filepath))
        else:
            results['invalid'].append({
                'file': str(filepath),
                'error': message
            })
            
            if fix_minor_errors:
                # Try to suggest fixes for common errors
                suggestion = suggest_filename_fix(filepath.name)
                if suggestion:
                    results['suggestions'][str(filepath)] = suggestion
    
    return results


def suggest_filename_fix(filename):
    """
    Try to suggest a corrected filename for common errors
    
    Returns: suggested filename or None
    """
    name = Path(filename).stem
    ext = Path(filename).suffix
    parts = name.split('_')
    
    if len(parts) < 6:
        return None
    
    suggestions = []
    
    # Check and fix newspaper code
    if len(parts[0]) == 3:
        suggestions.append(parts[0].upper())
    else:
        return None
    
    # Check and fix year (must be 4 digits)
    if parts[1].isdigit():
        suggestions.append(f"{int(parts[1]):04d}")
    else:
        return None
    
    # Check and fix month (must be 2 digits, 01-12)
    if parts[2].isdigit() and 1 <= int(parts[2]) <= 12:
        suggestions.append(f"{int(parts[2]):02d}")
    else:
        return None
    
    # Check and fix day (must be 2 digits, 01-31)
    if parts[3].isdigit() and 1 <= int(parts[3]) <= 31:
        suggestions.append(f"{int(parts[3]):02d}")
    else:
        return None
    
    # Check and fix page (must be 3 digits)
    if parts[4].isdigit() and 1 <= int(parts[4]) <= 999:
        suggestions.append(f"{int(parts[4]):03d}")
    else:
        return None
    
    # Check and fix library code
    if len(parts[5]) == 2:
        suggestions.append(parts[5].upper())
    else:
        return None
    
    # Add shelfmark if present
    if len(parts) > 6:
        suggestions.append('_'.join(parts[6:]))
    
    suggested = '_'.join(suggestions) + ext
    
    # Only return if different from original
    return suggested if suggested != filename else None


if __name__ == '__main__':
    # Example usage
    import sys
    
    if len(sys.argv) > 1:
        corpus_path = sys.argv[1]
        
        print("Listing newspapers in corpus...")
        newspapers = list_newspapers_in_corpus(corpus_path)
        
        for code, info in newspapers.items():
            print(f"{code}: {info['name']}")
            print(f"  Issues: {info['issues']}, Pages: {info['pages']}")
    else:
        # Demonstrate filename generation
        print("Example: Generate a valid filename")
        filename = generate_filename(
            newspaper_code='TID',
            year=1964,
            month=1,
            day=9,
            page=1,
            library_code='SB',
            shelfmark='Zsn128162MR'
        )
        print(f"Generated filename: {filename}")
        
        # Validate it
        is_valid, msg = validate_filename(filename)
        print(f"Validation: {msg}")
