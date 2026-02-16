#!/usr/bin/env python3
"""
Example Usage of Corpus Analysis Tools
Demonstrates how to use the analyzer programmatically for custom analysis
"""

from dd_corpus_tools import NewspaperCorpusAnalyzer, NEWSPAPER_NAMES


def example_basic_usage(corpus_path):
    """Example 1: Basic usage - get overall statistics"""
    print("=" * 80)
    print("EXAMPLE 1: Basic Usage")
    print("=" * 80)
    
    analyzer = NewspaperCorpusAnalyzer(corpus_path)
    analyzer.scan_corpus()
    
    # Access statistics directly
    total_newspapers = len(analyzer.data)
    total_issues = sum(len(dates) for dates in analyzer.issues.values())
    total_pages = sum(analyzer.pages_by_newspaper.values())
    
    print(f"Total newspapers: {total_newspapers}")
    print(f"Total issues: {total_issues}")
    print(f"Total pages: {total_pages}")
    print()


def example_newspaper_query(corpus_path, newspaper_code):
    """Example 2: Query specific newspaper information"""
    print("=" * 80)
    print(f"EXAMPLE 2: Query Specific Newspaper ({newspaper_code})")
    print("=" * 80)
    
    analyzer = NewspaperCorpusAnalyzer(corpus_path)
    analyzer.scan_corpus()
    
    if newspaper_code not in analyzer.data:
        print(f"Newspaper {newspaper_code} not found in corpus")
        return
    
    name = NEWSPAPER_NAMES.get(newspaper_code, newspaper_code)
    issues = len(analyzer.issues[newspaper_code])
    pages = analyzer.pages_by_newspaper[newspaper_code]
    years = sorted(analyzer.data[newspaper_code].keys())
    
    print(f"Name: {name}")
    print(f"Issues: {issues}")
    print(f"Pages: {pages}")
    print(f"Year range: {min(years)}-{max(years)}")
    print(f"Years covered: {', '.join(map(str, years))}")
    
    # Show year-by-year breakdown
    print("\nYear-by-year:")
    for year in years:
        year_issues = len(analyzer.issues_by_year[newspaper_code][year])
        year_pages = analyzer.pages_by_newspaper_year[newspaper_code][year]
        print(f"  {year}: {year_issues} issues, {year_pages} pages")
    print()


def example_library_query(corpus_path, library_code):
    """Example 3: Query specific library holdings"""
    print("=" * 80)
    print(f"EXAMPLE 3: Query Library Holdings ({library_code})")
    print("=" * 80)
    
    analyzer = NewspaperCorpusAnalyzer(corpus_path)
    analyzer.scan_corpus()
    
    if library_code not in analyzer.libraries:
        print(f"Library {library_code} not found in corpus")
        return
    
    total_newspapers = len(analyzer.libraries[library_code])
    total_issues = sum(len(analyzer.library_issues[library_code][np]) 
                      for np in analyzer.library_issues[library_code])
    total_pages = sum(analyzer.libraries[library_code].values())
    
    print(f"Total newspapers: {total_newspapers}")
    print(f"Total issues: {total_issues}")
    print(f"Total pages: {total_pages}")
    print("\nNewspapers held:")
    
    for newspaper in sorted(analyzer.libraries[library_code].keys()):
        issues = len(analyzer.library_issues[library_code][newspaper])
        pages = analyzer.libraries[library_code][newspaper]
        years = sorted(analyzer.library_years[library_code][newspaper])
        print(f"  {newspaper}: {issues} issues, {pages} pages ({min(years)}-{max(years)})")
    print()


def example_year_range_query(corpus_path, start_year, end_year):
    """Example 4: Query coverage for a specific year range"""
    print("=" * 80)
    print(f"EXAMPLE 4: Coverage for {start_year}-{end_year}")
    print("=" * 80)
    
    analyzer = NewspaperCorpusAnalyzer(corpus_path)
    analyzer.scan_corpus()
    
    total_pages = 0
    total_issues = 0
    newspapers_active = set()
    
    for year in range(start_year, end_year + 1):
        if year in analyzer.pages_by_year:
            total_pages += analyzer.pages_by_year[year]
            for newspaper in analyzer.data:
                if year in analyzer.data[newspaper]:
                    newspapers_active.add(newspaper)
                    total_issues += len(analyzer.issues_by_year[newspaper][year])
    
    print(f"Total pages: {total_pages}")
    print(f"Total issues: {total_issues}")
    print(f"Newspapers active: {len(newspapers_active)}")
    print(f"Newspapers: {', '.join(sorted(newspapers_active))}")
    print()


def example_missing_issues_estimate(corpus_path, newspaper_code):
    """Example 5: Calculate missing issues for a newspaper"""
    print("=" * 80)
    print(f"EXAMPLE 5: Missing Issues Estimate ({newspaper_code})")
    print("=" * 80)
    
    from datetime import datetime
    
    analyzer = NewspaperCorpusAnalyzer(corpus_path)
    analyzer.scan_corpus()
    
    if newspaper_code not in analyzer.issues:
        print(f"Newspaper {newspaper_code} not found in corpus")
        return
    
    dates = sorted(analyzer.issues[newspaper_code])
    date_objects = [datetime.strptime(d, '%Y-%m-%d') for d in dates]
    
    # Calculate average gap
    gaps = [(date_objects[i+1] - date_objects[i]).days 
           for i in range(len(date_objects)-1)]
    avg_gap = sum(gaps) / len(gaps) if gaps else 0
    
    # Determine frequency
    if avg_gap <= 1.5:
        freq = "Daily"
        expected_gap = 1
    elif avg_gap <= 8:
        freq = "Weekly"
        expected_gap = 7
    else:
        freq = "Monthly/Irregular"
        expected_gap = 30
    
    # Count significant gaps and estimate missing
    significant_gaps = 0
    estimated_missing = 0
    
    for i in range(len(date_objects) - 1):
        gap_days = (date_objects[i + 1] - date_objects[i]).days
        if gap_days > expected_gap * 2:
            significant_gaps += 1
            estimated_missing += max(0, int(gap_days / expected_gap) - 1)
    
    print(f"Issues in corpus: {len(dates)}")
    print(f"Estimated frequency: {freq}")
    print(f"Average gap: {avg_gap:.1f} days")
    print(f"Significant gaps: {significant_gaps}")
    print(f"Estimated missing issues: {estimated_missing}")
    
    if estimated_missing > 0:
        completeness = len(dates) / (len(dates) + estimated_missing) * 100
        print(f"Estimated completeness: {completeness:.1f}%")
    print()


def example_cross_library_comparison(corpus_path):
    """Example 6: Compare holdings across libraries"""
    print("=" * 80)
    print("EXAMPLE 6: Cross-Library Comparison")
    print("=" * 80)
    
    analyzer = NewspaperCorpusAnalyzer(corpus_path)
    analyzer.scan_corpus()
    
    # Find newspapers held by multiple libraries
    newspaper_library_count = {}
    for newspaper in analyzer.data:
        libraries = [lib for lib in analyzer.libraries 
                    if newspaper in analyzer.libraries[lib]]
        newspaper_library_count[newspaper] = len(libraries)
    
    print("Newspapers by number of source libraries:")
    for count in sorted(set(newspaper_library_count.values()), reverse=True):
        newspapers = [np for np, c in newspaper_library_count.items() if c == count]
        if newspapers:
            print(f"\n{count} {'library' if count == 1 else 'libraries'}:")
            for newspaper in sorted(newspapers):
                print(f"  {newspaper}: {NEWSPAPER_NAMES.get(newspaper, newspaper)}")
    print()


def example_custom_export(corpus_path):
    """Example 7: Create custom export for specific needs"""
    print("=" * 80)
    print("EXAMPLE 7: Custom Export - Tibet Daily by Year")
    print("=" * 80)
    
    import csv
    
    analyzer = NewspaperCorpusAnalyzer(corpus_path)
    analyzer.scan_corpus()
    
    newspaper = 'TID'  # Tibet Daily
    
    if newspaper not in analyzer.data:
        print(f"{newspaper} not found")
        return
    
    # Create custom CSV
    output_file = 'tibet_daily_by_year.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Year', 'Issues', 'Pages', 'Avg_Pages_Per_Issue'])
        
        for year in sorted(analyzer.data[newspaper].keys()):
            issues = len(analyzer.issues_by_year[newspaper][year])
            pages = analyzer.pages_by_newspaper_year[newspaper][year]
            avg_pages = pages / issues if issues > 0 else 0
            
            writer.writerow([year, issues, pages, f"{avg_pages:.1f}"])
    
    print(f"Custom export created: {output_file}")
    print()


def main():
    """Run all examples"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python example_usage.py <corpus_root_directory>")
        print("\nThis script demonstrates various ways to use the corpus analyzer")
        print("programmatically for custom analysis tasks.")
        sys.exit(1)
    
    corpus_path = sys.argv[1]
    
    print("\n" + "=" * 80)
    print("CORPUS ANALYSIS EXAMPLES")
    print("=" * 80 + "\n")
    
    # Run examples
    example_basic_usage(corpus_path)
    example_newspaper_query(corpus_path, 'TID')  # Tibet Daily
    example_library_query(corpus_path, 'SB')  # Staatsbibliothek zu Berlin
    example_year_range_query(corpus_path, 1960, 1965)
    example_missing_issues_estimate(corpus_path, 'QTN')  # Qinghai Tibetan News
    example_cross_library_comparison(corpus_path)
    example_custom_export(corpus_path)
    
    print("=" * 80)
    print("All examples completed!")
    print("=" * 80)


if __name__ == '__main__':
    main()
