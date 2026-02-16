#!/usr/bin/env python3
"""
Advanced Newspaper Corpus Analysis
Provides detailed analysis including issue completeness, missing data detection, etc.
"""

import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timedelta
import csv

from .analyzer import NewspaperCorpusAnalyzer
from .constants import NEWSPAPER_NAMES


class AdvancedCorpusAnalyzer(NewspaperCorpusAnalyzer):
    """Extended analyzer with additional analysis capabilities"""
    
    def __init__(self, corpus_root):
        super().__init__(corpus_root)
        self.issues_detail = defaultdict(lambda: defaultdict(list))  # newspaper -> date -> list of pages
    
    def scan_corpus(self):
        """Extended scan that also tracks page numbers per issue"""
        super().scan_corpus()
        
        # Build detailed issue information
        for newspaper in self.data:
            for year in self.data[newspaper]:
                for page_info in self.data[newspaper][year]:
                    date = page_info['date']
                    self.issues_detail[newspaper][date].append(page_info['page'])
    
    def check_issue_completeness(self):
        """Check for issues with missing or duplicate pages"""
        print("ISSUE COMPLETENESS CHECK")
        print("=" * 80)
        
        issues_with_problems = 0
        
        for newspaper in sorted(self.issues_detail.keys()):
            newspaper_problems = []
            
            for date in sorted(self.issues_detail[newspaper].keys()):
                pages = sorted(self.issues_detail[newspaper][date])
                
                # Check for gaps in page numbers
                expected_pages = list(range(1, max(pages) + 1))
                missing_pages = set(expected_pages) - set(pages)
                
                # Check for duplicates
                duplicate_pages = [p for p in set(pages) if pages.count(p) > 1]
                
                if missing_pages or duplicate_pages:
                    newspaper_problems.append({
                        'date': date,
                        'total_pages': len(pages),
                        'max_page': max(pages),
                        'missing': sorted(missing_pages),
                        'duplicates': sorted(duplicate_pages)
                    })
            
            if newspaper_problems:
                issues_with_problems += len(newspaper_problems)
                name = NEWSPAPER_NAMES.get(newspaper, newspaper)
                print(f"\n{newspaper} - {name}")
                print("-" * 80)
                
                for problem in newspaper_problems[:10]:  # Show first 10
                    print(f"  Date: {problem['date']}")
                    if problem['missing']:
                        print(f"    Missing pages: {problem['missing']}")
                    if problem['duplicates']:
                        print(f"    Duplicate pages: {problem['duplicates']}")
                    print(f"    Total pages in issue: {problem['total_pages']} (max page #: {problem['max_page']})")
                
                if len(newspaper_problems) > 10:
                    print(f"  ... and {len(newspaper_problems) - 10} more issues with problems")
        
        print(f"\nTotal issues with missing/duplicate pages: {issues_with_problems}")
        print()
    
    def find_temporal_gaps(self):
        """Identify temporal gaps in newspaper coverage"""
        print("TEMPORAL COVERAGE GAPS")
        print("=" * 80)
        
        for newspaper in sorted(self.issues_detail.keys()):
            dates = sorted(self.issues_detail[newspaper].keys())
            
            if len(dates) < 2:
                continue
            
            date_objects = [datetime.strptime(d, '%Y-%m-%d') for d in dates]
            gaps = []
            
            for i in range(len(date_objects) - 1):
                gap_days = (date_objects[i + 1] - date_objects[i]).days
                
                # Report gaps longer than 60 days
                if gap_days > 60:
                    gaps.append({
                        'from': dates[i],
                        'to': dates[i + 1],
                        'days': gap_days
                    })
            
            if gaps:
                name = NEWSPAPER_NAMES.get(newspaper, newspaper)
                print(f"\n{newspaper} - {name}")
                print("-" * 80)
                
                for gap in gaps[:10]:  # Show first 10
                    print(f"  Gap: {gap['from']} to {gap['to']} ({gap['days']} days)")
                
                if len(gaps) > 10:
                    print(f"  ... and {len(gaps) - 10} more gaps")
        
        print()
    
    def generate_monthly_statistics(self):
        """Generate statistics by month"""
        print("MONTHLY STATISTICS")
        print("=" * 80)
        
        monthly_data = defaultdict(lambda: defaultdict(int))  # year-month -> newspaper -> pages
        
        for newspaper in self.data:
            for year in self.data[newspaper]:
                for page_info in self.data[newspaper][year]:
                    year_month = f"{page_info['year']}-{page_info['month']:02d}"
                    monthly_data[year_month][newspaper] += 1
        
        # Print monthly breakdown
        for year_month in sorted(monthly_data.keys())[:24]:  # Show first 24 months
            total_pages = sum(monthly_data[year_month].values())
            newspapers = len(monthly_data[year_month])
            print(f"{year_month}: {total_pages} pages from {newspapers} newspapers")
        
        print()
    
    def export_detailed_csv(self, output_file='corpus_detailed.csv'):
        """Export detailed page-level data to CSV"""
        output_path = Path(output_file)
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Newspaper_Code', 'Newspaper_Name', 'Date', 'Year', 'Month', 'Day',
                'Page', 'Library', 'Shelfmark'
            ])
            
            for newspaper in sorted(self.data.keys()):
                for year in sorted(self.data[newspaper].keys()):
                    for page_info in sorted(self.data[newspaper][year], 
                                           key=lambda x: (x['date'], x['page'])):
                        writer.writerow([
                            page_info['newspaper'],
                            page_info['newspaper_name'],
                            page_info['date'],
                            page_info['year'],
                            page_info['month'],
                            page_info['day'],
                            page_info['page'],
                            page_info['library'],
                            page_info['shelfmark']
                        ])
        
        print(f"Detailed data exported to: {output_path.absolute()}")
        print()
    
    def export_issues_csv(self, output_file='corpus_issues.csv'):
        """Export issue-level summary to CSV"""
        output_path = Path(output_file)
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Newspaper_Code', 'Newspaper_Name', 'Date', 'Year', 'Month', 'Day',
                'Total_Pages', 'Max_Page_Number', 'Has_Gaps', 'Has_Duplicates'
            ])
            
            for newspaper in sorted(self.issues_detail.keys()):
                for date in sorted(self.issues_detail[newspaper].keys()):
                    pages = sorted(self.issues_detail[newspaper][date])
                    max_page = max(pages)
                    expected_pages = set(range(1, max_page + 1))
                    has_gaps = len(expected_pages - set(pages)) > 0
                    has_duplicates = len(pages) != len(set(pages))
                    
                    year, month, day = date.split('-')
                    
                    writer.writerow([
                        newspaper,
                        NEWSPAPER_NAMES.get(newspaper, newspaper),
                        date,
                        int(year),
                        int(month),
                        int(day),
                        len(pages),
                        max_page,
                        'Yes' if has_gaps else 'No',
                        'Yes' if has_duplicates else 'No'
                    ])
        
        print(f"Issue-level data exported to: {output_path.absolute()}")
        print()
    
    def export_library_holdings_csv(self, output_file='library_holdings.csv'):
        """Export detailed library holdings to CSV"""
        output_path = Path(output_file)
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Library_Code', 'Newspaper_Code', 'Newspaper_Name',
                'Total_Issues', 'Total_Pages', 'Years_Covered',
                'First_Year', 'Last_Year'
            ])
            
            for library in sorted(self.libraries.keys()):
                for newspaper in sorted(self.libraries[library].keys()):
                    years = sorted(self.library_years[library][newspaper])
                    issues = len(self.library_issues[library][newspaper])
                    pages = self.libraries[library][newspaper]
                    
                    writer.writerow([
                        library,
                        newspaper,
                        NEWSPAPER_NAMES.get(newspaper, newspaper),
                        issues,
                        pages,
                        ', '.join(map(str, years)),
                        min(years) if years else '',
                        max(years) if years else ''
                    ])
        
        print(f"Library holdings exported to: {output_path.absolute()}")
        print()
    
    def export_missing_issues_csv(self, output_file='missing_issues.csv'):
        """Export missing issues analysis to CSV"""
        from datetime import datetime
        
        output_path = Path(output_file)
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Newspaper_Code', 'Newspaper_Name', 'Total_Issues_In_Corpus',
                'Estimated_Frequency', 'Average_Gap_Days',
                'Significant_Gaps_Count', 'Estimated_Missing_Issues'
            ])
            
            for newspaper in sorted(self.data.keys()):
                dates = sorted(self.issues[newspaper])
                
                if len(dates) < 2:
                    continue
                
                date_objects = [datetime.strptime(d, '%Y-%m-%d') for d in dates]
                gaps = [(date_objects[i+1] - date_objects[i]).days 
                       for i in range(len(date_objects)-1)]
                avg_gap = sum(gaps) / len(gaps) if gaps else 0
                
                # Determine frequency
                if avg_gap <= 1.5:
                    freq = "Daily"
                    expected_gap = 1
                elif avg_gap <= 4:
                    freq = "2-3x per week"
                    expected_gap = 3
                elif avg_gap <= 8:
                    freq = "Weekly"
                    expected_gap = 7
                elif avg_gap <= 16:
                    freq = "Bi-weekly"
                    expected_gap = 14
                else:
                    freq = "Monthly/Irregular"
                    expected_gap = 30
                
                # Count significant gaps
                significant_gaps_count = 0
                total_estimated_missing = 0
                
                for i in range(len(date_objects) - 1):
                    gap_days = (date_objects[i + 1] - date_objects[i]).days
                    if gap_days > expected_gap * 2:
                        significant_gaps_count += 1
                        missing_estimate = max(0, int(gap_days / expected_gap) - 1)
                        total_estimated_missing += missing_estimate
                
                writer.writerow([
                    newspaper,
                    NEWSPAPER_NAMES.get(newspaper, newspaper),
                    len(dates),
                    freq,
                    round(avg_gap, 2),
                    significant_gaps_count,
                    total_estimated_missing
                ])
        
        print(f"Missing issues analysis exported to: {output_path.absolute()}")
        print()
    
    def run_advanced_analysis(self):
        """Run all advanced analysis functions"""
        self.scan_corpus()
        self.print_summary_statistics()
        self.print_newspaper_list()
        self.print_newspaper_statistics()
        self.print_yearly_statistics()
        self.print_newspaper_year_matrix()
        self.print_library_statistics()
        self.print_detailed_library_holdings()
        self.analyze_missing_issues()
        self.check_issue_completeness()
        self.find_temporal_gaps()
        self.generate_monthly_statistics()
        
        # Export data
        self.export_to_json('corpus_statistics.json')
        self.export_detailed_csv('corpus_detailed.csv')
        self.export_issues_csv('corpus_issues.csv')
        self.export_library_holdings_csv('library_holdings.csv')
        self.export_missing_issues_csv('missing_issues.csv')


if __name__ == '__main__':
    # For testing only
    import sys
    if len(sys.argv) >= 2:
        analyzer = AdvancedCorpusAnalyzer(sys.argv[1])
        analyzer.run_advanced_analysis()
