#!/usr/bin/env python3
"""
Divergent Discourses Corpus Analyzer
Analyzes Tibetan newspaper corpus folder structure and generates statistics
"""

import os
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
import json

from .constants import NEWSPAPER_NAMES, VALID_EXTENSIONS, FILENAME_PATTERN

class NewspaperCorpusAnalyzer:
    """Analyzer for the Divergent Discourses newspaper corpus"""
    
    def __init__(self, corpus_root):
        self.corpus_root = Path(corpus_root)
        self.data = defaultdict(lambda: defaultdict(list))
        self.issues = defaultdict(set)  # newspaper -> set of dates
        self.pages_by_newspaper = defaultdict(int)
        self.pages_by_year = defaultdict(int)
        self.pages_by_newspaper_year = defaultdict(lambda: defaultdict(int))
        self.issues_by_year = defaultdict(lambda: defaultdict(set))
        self.libraries = defaultdict(lambda: defaultdict(int))  # library -> newspaper -> count
        self.library_issues = defaultdict(lambda: defaultdict(set))  # library -> newspaper -> set of dates
        self.library_years = defaultdict(lambda: defaultdict(set))  # library -> newspaper -> set of years
        
    def parse_filename(self, filename):
        """
        Parse filename in format: XXX_YYYY_MM_DD_ppp_LL_abcd
        Returns dict with parsed information or None if invalid
        """
        # Remove file extension
        name = filename.stem if isinstance(filename, Path) else Path(filename).stem
        
        # Use pattern from constants
        match = re.match(FILENAME_PATTERN, name)
        
        if match:
            newspaper, year, month, day, page, library, shelfmark = match.groups()
            return {
                'newspaper': newspaper,
                'newspaper_name': NEWSPAPER_NAMES.get(newspaper, f'Unknown ({newspaper})'),
                'year': int(year),
                'month': int(month),
                'day': int(day),
                'date': f'{year}-{month}-{day}',
                'page': int(page),
                'library': library,
                'shelfmark': shelfmark or ''
            }
        return None
    
    def scan_corpus(self):
        """Scan the entire corpus directory structure"""
        print(f"Scanning corpus at: {self.corpus_root}")
        print("=" * 80)
        
        total_files = 0
        valid_files = 0
        invalid_files = []
        
        # Walk through all image files
        for img_file in self.corpus_root.rglob('*'):
            # Skip directories and non-image files
            if not img_file.is_file():
                continue
            if img_file.suffix.lower() not in VALID_EXTENSIONS:
                continue
                
            total_files += 1
            
            # Parse the filename
            parsed = self.parse_filename(img_file)
            
            if parsed:
                valid_files += 1
                newspaper = parsed['newspaper']
                year = parsed['year']
                date = parsed['date']
                library = parsed['library']
                
                # Store the data
                self.data[newspaper][year].append(parsed)
                self.issues[newspaper].add(date)
                self.pages_by_newspaper[newspaper] += 1
                self.pages_by_year[year] += 1
                self.pages_by_newspaper_year[newspaper][year] += 1
                self.issues_by_year[newspaper][year].add(date)
                self.libraries[library][newspaper] += 1
                self.library_issues[library][newspaper].add(date)
                self.library_years[library][newspaper].add(year)
            else:
                invalid_files.append(str(img_file.name))
        
        print(f"Total files scanned: {total_files}")
        print(f"Valid newspaper pages: {valid_files}")
        print(f"Invalid/unparseable files: {len(invalid_files)}")
        
        if invalid_files and len(invalid_files) <= 20:
            print("\nInvalid filenames:")
            for fname in invalid_files[:20]:
                print(f"  - {fname}")
        
        print("=" * 80)
        print()
    
    def print_summary_statistics(self):
        """Print overall corpus statistics"""
        print("CORPUS SUMMARY STATISTICS")
        print("=" * 80)
        
        total_pages = sum(self.pages_by_newspaper.values())
        total_issues = sum(len(dates) for dates in self.issues.values())
        total_newspapers = len(self.data)
        
        print(f"Total newspapers in corpus: {total_newspapers}")
        print(f"Total issues in corpus: {total_issues}")
        print(f"Total pages in corpus: {total_pages}")
        
        if total_pages > 0:
            print(f"Average pages per issue: {total_pages / total_issues:.1f}")
        
        years = sorted(self.pages_by_year.keys())
        if years:
            print(f"Year range: {min(years)} - {max(years)}")
        
        print()
    
    def print_newspaper_statistics(self):
        """Print statistics for each newspaper"""
        print("STATISTICS BY NEWSPAPER")
        print("=" * 80)
        
        # Sort newspapers by code
        for newspaper in sorted(self.data.keys()):
            name = NEWSPAPER_NAMES.get(newspaper, f'Unknown ({newspaper})')
            total_issues = len(self.issues[newspaper])
            total_pages = self.pages_by_newspaper[newspaper]
            years = sorted(self.data[newspaper].keys())
            
            print(f"\n{newspaper} - {name}")
            print("-" * 80)
            print(f"  Total issues: {total_issues}")
            print(f"  Total pages: {total_pages}")
            if total_issues > 0:
                print(f"  Average pages per issue: {total_pages / total_issues:.1f}")
            print(f"  Year range: {min(years)} - {max(years)}")
            print(f"  Years covered: {', '.join(map(str, years))}")
        
        print()
    
    def print_yearly_statistics(self):
        """Print statistics by year"""
        print("STATISTICS BY YEAR")
        print("=" * 80)
        
        years = sorted(self.pages_by_year.keys())
        
        print(f"\n{'Year':<6} {'Pages':<8} {'Issues':<8} {'Newspapers':<12}")
        print("-" * 80)
        
        for year in years:
            total_pages = self.pages_by_year[year]
            # Count total issues for this year across all newspapers
            total_issues = sum(len(dates) for dates in self.issues_by_year.values() 
                             for y, dates in dates.items() if y == year)
            # Count newspapers active in this year
            newspapers_active = sum(1 for np in self.data if year in self.data[np])
            
            print(f"{year:<6} {total_pages:<8} {total_issues:<8} {newspapers_active:<12}")
        
        print()
    
    def print_newspaper_year_matrix(self):
        """Print a matrix showing pages per newspaper per year"""
        print("PAGES BY NEWSPAPER AND YEAR")
        print("=" * 80)
        
        newspapers = sorted(self.data.keys())
        all_years = sorted(set(year for np_data in self.data.values() for year in np_data.keys()))
        
        # Print header
        print(f"\n{'Code':<6}", end='')
        for year in all_years:
            print(f"{year:<7}", end='')
        print("Total")
        print("-" * (6 + 7 * len(all_years) + 7))
        
        # Print data for each newspaper
        for newspaper in newspapers:
            print(f"{newspaper:<6}", end='')
            for year in all_years:
                pages = self.pages_by_newspaper_year[newspaper].get(year, 0)
                if pages > 0:
                    print(f"{pages:<7}", end='')
                else:
                    print(f"{'—':<7}", end='')
            print(f"{self.pages_by_newspaper[newspaper]:<7}")
        
        # Print totals
        print("-" * (6 + 7 * len(all_years) + 7))
        print(f"{'Total':<6}", end='')
        for year in all_years:
            print(f"{self.pages_by_year[year]:<7}", end='')
        print(f"{sum(self.pages_by_newspaper.values()):<7}")
        
        print()
    
    def print_library_statistics(self):
        """Print statistics by library source"""
        print("STATISTICS BY LIBRARY/SOURCE")
        print("=" * 80)
        
        for library in sorted(self.libraries.keys()):
            total_pages = sum(self.libraries[library].values())
            total_issues = sum(len(self.library_issues[library][np]) for np in self.library_issues[library])
            newspapers_count = len(self.libraries[library])
            
            print(f"\n{library} - Total: {newspapers_count} newspapers, {total_issues} issues, {total_pages} pages")
            print("-" * 80)
            
            for newspaper in sorted(self.libraries[library].keys()):
                pages = self.libraries[library][newspaper]
                issues = len(self.library_issues[library][newspaper])
                years = sorted(self.library_years[library][newspaper])
                year_range = f"{min(years)}-{max(years)}" if len(years) > 1 else str(years[0])
                
                print(f"  {newspaper}: {issues} issues, {pages} pages ({year_range})")
        
        print()
    
    def print_detailed_library_holdings(self):
        """Print detailed library holdings by newspaper and year"""
        print("DETAILED LIBRARY HOLDINGS")
        print("=" * 80)
        
        for library in sorted(self.libraries.keys()):
            print(f"\n{library}")
            print("-" * 80)
            
            for newspaper in sorted(self.libraries[library].keys()):
                name = NEWSPAPER_NAMES.get(newspaper, newspaper)
                print(f"\n  {newspaper} - {name}")
                
                # Get all years for this newspaper from this library
                years = sorted(self.library_years[library][newspaper])
                
                for year in years:
                    # Count issues in this year from this library
                    issues_this_year = [date for date in self.library_issues[library][newspaper] 
                                       if date.startswith(str(year))]
                    pages_this_year = sum(1 for page in self.data[newspaper][year] 
                                        if page['library'] == library)
                    
                    print(f"    {year}: {len(issues_this_year)} issues, {pages_this_year} pages")
        
        print()
    
    def print_newspaper_list(self):
        """Print comprehensive list of newspapers in the corpus"""
        print("COMPLETE NEWSPAPER LIST")
        print("=" * 80)
        print()
        
        for idx, newspaper in enumerate(sorted(self.data.keys()), 1):
            name = NEWSPAPER_NAMES.get(newspaper, f'Unknown ({newspaper})')
            total_issues = len(self.issues[newspaper])
            total_pages = self.pages_by_newspaper[newspaper]
            years = sorted(self.data[newspaper].keys())
            year_range = f"{min(years)}-{max(years)}" if len(years) > 1 else str(years[0])
            
            # Get libraries that hold this newspaper
            libraries_with_this = [lib for lib in self.libraries 
                                  if newspaper in self.libraries[lib]]
            
            print(f"{idx}. {newspaper} - {name}")
            print(f"   Total: {total_issues} issues, {total_pages} pages")
            print(f"   Coverage: {year_range} ({len(years)} years)")
            print(f"   Sources: {', '.join(sorted(libraries_with_this))}")
            print()
        
        print()
    
    def analyze_missing_issues(self):
        """Analyze and report missing issues for each newspaper"""
        print("MISSING ISSUES ANALYSIS")
        print("=" * 80)
        print()
        
        from datetime import datetime, timedelta
        
        for newspaper in sorted(self.data.keys()):
            name = NEWSPAPER_NAMES.get(newspaper, newspaper)
            dates = sorted(self.issues[newspaper])
            
            if len(dates) < 2:
                continue
            
            print(f"{newspaper} - {name}")
            print("-" * 80)
            
            date_objects = [datetime.strptime(d, '%Y-%m-%d') for d in dates]
            
            # Determine likely publication frequency
            gaps = [(date_objects[i+1] - date_objects[i]).days 
                   for i in range(len(date_objects)-1)]
            avg_gap = sum(gaps) / len(gaps) if gaps else 0
            
            # Estimate publication frequency
            if avg_gap <= 1.5:
                freq = "Daily"
                expected_gap = 1
            elif avg_gap <= 4:
                freq = "2-3 times per week"
                expected_gap = 3
            elif avg_gap <= 8:
                freq = "Weekly"
                expected_gap = 7
            elif avg_gap <= 16:
                freq = "Bi-weekly"
                expected_gap = 14
            else:
                freq = "Monthly or irregular"
                expected_gap = 30
            
            print(f"  Estimated frequency: {freq} (avg gap: {avg_gap:.1f} days)")
            print(f"  Total issues in corpus: {len(dates)}")
            
            # Count significant gaps (more than 2x expected gap)
            significant_gaps = []
            for i in range(len(date_objects) - 1):
                gap_days = (date_objects[i + 1] - date_objects[i]).days
                if gap_days > expected_gap * 2:
                    missing_estimate = max(0, int(gap_days / expected_gap) - 1)
                    significant_gaps.append({
                        'from': dates[i],
                        'to': dates[i + 1],
                        'days': gap_days,
                        'estimated_missing': missing_estimate
                    })
            
            if significant_gaps:
                total_estimated_missing = sum(g['estimated_missing'] for g in significant_gaps)
                print(f"  Significant gaps: {len(significant_gaps)}")
                print(f"  Estimated missing issues: ~{total_estimated_missing}")
                print(f"  Missing issues detail:")
                
                for gap in significant_gaps[:10]:  # Show first 10
                    print(f"    {gap['from']} to {gap['to']}: "
                          f"{gap['days']} days (~{gap['estimated_missing']} issues)")
                
                if len(significant_gaps) > 10:
                    remaining = len(significant_gaps) - 10
                    remaining_missing = sum(g['estimated_missing'] for g in significant_gaps[10:])
                    print(f"    ... and {remaining} more gaps (~{remaining_missing} issues)")
            else:
                print(f"  No significant gaps detected")
            
            print()
        
        print()
    
    def export_to_json(self, output_file='corpus_statistics.json'):
        """Export all statistics to a JSON file"""
        from datetime import datetime
        
        output = {
            'summary': {
                'total_newspapers': len(self.data),
                'total_issues': sum(len(dates) for dates in self.issues.values()),
                'total_pages': sum(self.pages_by_newspaper.values()),
                'year_range': {
                    'min': min(self.pages_by_year.keys()) if self.pages_by_year else None,
                    'max': max(self.pages_by_year.keys()) if self.pages_by_year else None
                }
            },
            'newspapers': {},
            'by_year': dict(self.pages_by_year),
            'libraries': {}
        }
        
        # Add newspaper details
        for newspaper in self.data:
            years = sorted(self.data[newspaper].keys())
            
            # Calculate missing issues estimate
            dates = sorted(self.issues[newspaper])
            date_objects = [datetime.strptime(d, '%Y-%m-%d') for d in dates]
            gaps = [(date_objects[i+1] - date_objects[i]).days 
                   for i in range(len(date_objects)-1)] if len(date_objects) > 1 else []
            avg_gap = sum(gaps) / len(gaps) if gaps else 0
            
            output['newspapers'][newspaper] = {
                'name': NEWSPAPER_NAMES.get(newspaper, f'Unknown ({newspaper})'),
                'total_issues': len(self.issues[newspaper]),
                'total_pages': self.pages_by_newspaper[newspaper],
                'year_range': {
                    'min': min(years),
                    'max': max(years)
                },
                'years': years,
                'pages_by_year': dict(self.pages_by_newspaper_year[newspaper]),
                'average_gap_days': round(avg_gap, 2) if avg_gap else None
            }
        
        # Add detailed library holdings
        for library in self.libraries:
            output['libraries'][library] = {
                'total_pages': sum(self.libraries[library].values()),
                'total_issues': sum(len(self.library_issues[library][np]) 
                                  for np in self.library_issues[library]),
                'newspapers': {}
            }
            
            for newspaper in self.libraries[library]:
                years = sorted(self.library_years[library][newspaper])
                output['libraries'][library]['newspapers'][newspaper] = {
                    'issues': len(self.library_issues[library][newspaper]),
                    'pages': self.libraries[library][newspaper],
                    'years': years,
                    'year_range': {
                        'min': min(years),
                        'max': max(years)
                    } if years else None
                }
        
        output_path = Path(output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        
        print(f"Statistics exported to: {output_path.absolute()}")
        print()
    
    def run_full_analysis(self, export_json=True):
        """Run complete analysis and print all statistics"""
        self.scan_corpus()
        self.print_summary_statistics()
        self.print_newspaper_list()
        self.print_newspaper_statistics()
        self.print_yearly_statistics()
        self.print_newspaper_year_matrix()
        self.print_library_statistics()
        self.print_detailed_library_holdings()
        self.analyze_missing_issues()
        
        if export_json:
            self.export_to_json()


if __name__ == '__main__':
    # For testing only
    import sys
    if len(sys.argv) >= 2:
        analyzer = NewspaperCorpusAnalyzer(sys.argv[1])
        analyzer.run_full_analysis()
