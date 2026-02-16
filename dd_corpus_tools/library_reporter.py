#!/usr/bin/env python3
"""
Library Holdings and Missing Issues Reporter
Generates detailed reports on library holdings and missing issues in the corpus
"""

import os
from pathlib import Path
from datetime import datetime
import csv

from .analyzer import NewspaperCorpusAnalyzer
from .constants import NEWSPAPER_NAMES, LIBRARY_CODES


class LibraryHoldingsReporter(NewspaperCorpusAnalyzer):
    """Specialized reporter for library holdings and missing issues"""
    
    def generate_library_holdings_report(self, output_file='library_holdings_report.txt'):
        """Generate a detailed text report on library holdings"""
        output_path = Path(output_file)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("LIBRARY HOLDINGS REPORT\n")
            f.write("Divergent Discourses Corpus\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Corpus location: {self.corpus_root}\n\n")
            
            # Summary by library
            f.write("=" * 80 + "\n")
            f.write("SUMMARY BY LIBRARY\n")
            f.write("=" * 80 + "\n\n")
            
            for library in sorted(self.libraries.keys()):
                library_name = LIBRARY_CODES.get(library, library)
                total_newspapers = len(self.libraries[library])
                total_issues = sum(len(self.library_issues[library][np]) 
                                 for np in self.library_issues[library])
                total_pages = sum(self.libraries[library].values())
                
                f.write(f"{library} - {library_name}\n")
                f.write(f"  Newspapers: {total_newspapers}\n")
                f.write(f"  Issues: {total_issues}\n")
                f.write(f"  Pages: {total_pages}\n\n")
            
            # Detailed holdings by library
            f.write("\n" + "=" * 80 + "\n")
            f.write("DETAILED HOLDINGS BY LIBRARY\n")
            f.write("=" * 80 + "\n\n")
            
            for library in sorted(self.libraries.keys()):
                library_name = LIBRARY_CODES.get(library, library)
                f.write(f"\n{library} - {library_name}\n")
                f.write("-" * 80 + "\n\n")
                
                for newspaper in sorted(self.libraries[library].keys()):
                    name = NEWSPAPER_NAMES.get(newspaper, newspaper)
                    issues = len(self.library_issues[library][newspaper])
                    pages = self.libraries[library][newspaper]
                    years = sorted(self.library_years[library][newspaper])
                    
                    f.write(f"{newspaper} - {name}\n")
                    f.write(f"  Issues: {issues}\n")
                    f.write(f"  Pages: {pages}\n")
                    f.write(f"  Years: {', '.join(map(str, years))}\n")
                    f.write(f"  Coverage: {min(years)}-{max(years)}\n")
                    
                    # Show shelfmarks if available
                    shelfmarks = sorted(self.shelfmarks[library][newspaper])
                    if shelfmarks:
                        f.write(f"  Shelfmarks: {', '.join(shelfmarks)}\n")
                    
                    # Year-by-year breakdown
                    f.write(f"  Year-by-year:\n")
                    for year in years:
                        year_issues = [d for d in self.library_issues[library][newspaper] 
                                      if d.startswith(str(year))]
                        year_pages = sum(1 for page in self.data[newspaper][year] 
                                       if page['library'] == library)
                        f.write(f"    {year}: {len(year_issues)} issues, {year_pages} pages\n")
                    f.write("\n")
            
            # Holdings by newspaper across libraries
            f.write("\n" + "=" * 80 + "\n")
            f.write("HOLDINGS BY NEWSPAPER (ACROSS ALL LIBRARIES)\n")
            f.write("=" * 80 + "\n\n")
            
            for newspaper in sorted(self.data.keys()):
                name = NEWSPAPER_NAMES.get(newspaper, newspaper)
                f.write(f"\n{newspaper} - {name}\n")
                f.write("-" * 80 + "\n")
                
                # Find all libraries holding this newspaper
                holding_libraries = [lib for lib in self.libraries 
                                   if newspaper in self.libraries[lib]]
                
                library_names = [f"{lib} ({LIBRARY_CODES.get(lib, lib)})" for lib in sorted(holding_libraries)]
                f.write(f"Held by {len(holding_libraries)} {'library' if len(holding_libraries) == 1 else 'libraries'}: {', '.join(library_names)}\n\n")
                
                for library in sorted(holding_libraries):
                    library_name = LIBRARY_CODES.get(library, library)
                    issues = len(self.library_issues[library][newspaper])
                    pages = self.libraries[library][newspaper]
                    years = sorted(self.library_years[library][newspaper])
                    
                    f.write(f"  {library} - {library_name}:\n")
                    f.write(f"    Issues: {issues}\n")
                    f.write(f"    Pages: {pages}\n")
                    f.write(f"    Years: {', '.join(map(str, years))}\n")
                    
                    # Show shelfmarks if available
                    shelfmarks = sorted(self.shelfmarks[library][newspaper])
                    if shelfmarks:
                        f.write(f"    Shelfmarks: {', '.join(shelfmarks)}\n")
                    f.write("\n")
        
        print(f"Library holdings report saved to: {output_path.absolute()}")
        return output_path
    
    def generate_missing_issues_report(self, output_file='missing_issues_report.txt'):
        """Generate a detailed text report on missing issues"""
        output_path = Path(output_file)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("MISSING ISSUES ANALYSIS REPORT\n")
            f.write("Divergent Discourses Corpus\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Corpus location: {self.corpus_root}\n\n")
            
            f.write("This report analyzes gaps in the newspaper collection and estimates\n")
            f.write("missing issues based on inferred publication frequency.\n\n")
            
            # Analysis for each newspaper
            for newspaper in sorted(self.data.keys()):
                name = NEWSPAPER_NAMES.get(newspaper, newspaper)
                dates = sorted(self.issues[newspaper])
                
                if len(dates) < 2:
                    continue
                
                f.write("\n" + "=" * 80 + "\n")
                f.write(f"{newspaper} - {name}\n")
                f.write("=" * 80 + "\n\n")
                
                date_objects = [datetime.strptime(d, '%Y-%m-%d') for d in dates]
                
                # Calculate gaps
                gaps = [(date_objects[i+1] - date_objects[i]).days 
                       for i in range(len(date_objects)-1)]
                avg_gap = sum(gaps) / len(gaps) if gaps else 0
                min_gap = min(gaps) if gaps else 0
                max_gap = max(gaps) if gaps else 0
                
                # Determine frequency
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
                
                f.write(f"Collection Overview:\n")
                f.write(f"  Issues in corpus: {len(dates)}\n")
                f.write(f"  Date range: {dates[0]} to {dates[-1]}\n")
                f.write(f"  Estimated frequency: {freq}\n")
                f.write(f"  Average gap: {avg_gap:.1f} days\n")
                f.write(f"  Minimum gap: {min_gap} days\n")
                f.write(f"  Maximum gap: {max_gap} days\n\n")
                
                # Identify significant gaps
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
                    
                    f.write(f"Gap Analysis:\n")
                    f.write(f"  Number of significant gaps: {len(significant_gaps)}\n")
                    f.write(f"  Estimated missing issues: {total_estimated_missing}\n")
                    f.write(f"  Estimated collection completeness: "
                           f"{len(dates) / (len(dates) + total_estimated_missing) * 100:.1f}%\n\n")
                    
                    f.write(f"Significant Gaps (>{expected_gap * 2} days):\n\n")
                    
                    for idx, gap in enumerate(significant_gaps, 1):
                        f.write(f"  Gap #{idx}:\n")
                        f.write(f"    From: {gap['from']}\n")
                        f.write(f"    To: {gap['to']}\n")
                        f.write(f"    Duration: {gap['days']} days\n")
                        f.write(f"    Estimated missing: ~{gap['estimated_missing']} issues\n\n")
                else:
                    f.write(f"Gap Analysis:\n")
                    f.write(f"  No significant gaps detected\n")
                    f.write(f"  Collection appears relatively complete\n\n")
                
                # Year-by-year coverage
                f.write(f"Year-by-Year Coverage:\n\n")
                years_data = {}
                for date in dates:
                    year = int(date[:4])
                    years_data[year] = years_data.get(year, 0) + 1
                
                for year in sorted(years_data.keys()):
                    f.write(f"  {year}: {years_data[year]} issues\n")
                
                f.write("\n")
        
        print(f"Missing issues report saved to: {output_path.absolute()}")
        return output_path
    
    def generate_combined_report(self):
        """Generate all reports"""
        print("Generating comprehensive reports...")
        print("=" * 80)
        
        self.scan_corpus()
        
        holdings_report = self.generate_library_holdings_report()
        missing_report = self.generate_missing_issues_report()
        
        print("\nReports generated successfully!")
        print(f"  - {holdings_report}")
        print(f"  - {missing_report}")


if __name__ == '__main__':
    # For testing only
    import sys
    if len(sys.argv) >= 2:
        reporter = LibraryHoldingsReporter(sys.argv[1])
        reporter.generate_combined_report()
