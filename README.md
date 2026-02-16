# Divergent Discourses Corpus Analysis Tools

[![GitHub release](https://img.shields.io/github/v/release/Divergent-Discourses/DDC_CorpusStatistics)](https://github.com/Divergent-Discourses/DDC_CorpusStatistics/releases)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)

Comprehensive analysis tools for the Divergent Discourses Tibetan Newspaper Corpus (1950-1965).

## About the Project

The [Divergent Discourses project](https://research.uni-leipzig.de/diverge/) studies the role of narrative and discourse in the perpetuation of antagonisms in the Tibet-China dispute during the formative period of the 1950s and 1960s. These tools analyze a corpus of 16,718 pages from 16 Tibetan-language newspapers published between 1950 and 1965.

## Features

✨ **Complete Corpus Analysis**
- Automatic extraction of metadata from standardized filenames
- Comprehensive statistics on newspapers, issues, and pages
- Year-by-year coverage analysis

📊 **Excel-Ready Exports**
- Single consolidated CSV optimized for pivot tables
- Multi-sheet Excel workbook with pre-formatted data
- 23 comprehensive columns for flexible analysis

🏛️ **Library Holdings Tracking**
- Detailed provenance information
- Holdings by library, newspaper, and year
- Multi-source issue identification

📉 **Missing Issues Analysis**
- Automatic publication frequency detection
- Gap identification and quantification
- Completeness percentage estimates

📈 **Multiple Output Formats**
- JSON for programmatic access
- CSV for spreadsheet analysis
- Text reports for documentation
- Excel workbooks for visualization

## Quick Start

### Installation

```bash
pip install git+https://github.com/Divergent-Discourses/DDC_CorpusStatistics.git
```

Or install from source:

```bash
git clone https://github.com/Divergent-Discourses/DDC_CorpusStatistics.git
cd DDC_CorpusStatistics
pip install -e .
```

### Basic Usage

```bash
# Complete analysis with all statistics
dd-analyze /path/to/corpus

# Export for Excel pivot tables (recommended!)
dd-excel-export /path/to/corpus

# Generate detailed reports
dd-reports /path/to/corpus
```

### Python API

```python
from dd_corpus_tools import NewspaperCorpusAnalyzer

analyzer = NewspaperCorpusAnalyzer('/path/to/corpus')
analyzer.scan_corpus()
analyzer.print_summary_statistics()
analyzer.export_to_json('statistics.json')
```

## File Naming Convention

The tools expect files to follow this pattern:

```
XXX_YYYY_MM_DD_ppp_LL_abcd.ext
```

Where:
- `XXX`: 3-letter newspaper code (e.g., TID, QTN, TIM)
- `YYYY_MM_DD`: Publication date
- `ppp`: Page number (3 digits with leading zeros)
- `LL`: 2-letter library code
- `abcd`: Optional shelfmark
- `.ext`: File extension (.jpg, .png, .tif, .pdf)

Example: `TID_1964_01_09_001_SB_Zsn128162MR.jpg`

## Documentation

- **[User Guide](https://github.com/Divergent-Discourses/DDC_CorpusStatistics/blob/main/docs/USER_GUIDE.md)** - Comprehensive usage instructions
- **[Excel Pivot Tables Guide](https://github.com/Divergent-Discourses/DDC_CorpusStatistics/blob/main/docs/EXCEL_PIVOT_TABLES_GUIDE.md)** - Detailed Excel analysis tutorial
- **[API Reference](https://github.com/Divergent-Discourses/DDC_CorpusStatistics/blob/main/docs/API_REFERENCE.md)** - Python API documentation
- **[Quick Reference](https://github.com/Divergent-Discourses/DDC_CorpusStatistics/blob/main/docs/QUICK_REFERENCE.md)** - Quick command reference
- **[Installation Guide](https://github.com/Divergent-Discourses/DDC_CorpusStatistics/blob/main/INSTALL.md)** - Detailed installation instructions

## Newspaper Codes

| Code | Newspaper |
|------|-----------|
| CWN | Central Weekly News |
| DTF | Defend Tibet's Freedom |
| FRD | Freedom |
| GDN | Ganze Daily |
| GTN | Gyantse News |
| KDN | Kangding News |
| MJN | Minjiang News |
| NIB | News in Brief |
| QTN | Qinghai Tibetan News |
| SGN | South Gansu News |
| TDP | Tibet Daily Pictorial |
| TID | Tibet Daily |
| TIF | Tibetan Freedom |
| TIM | Tibet Mirror |
| XNX | South-West Institute for Nationalities |
| ZYX | Central Institute for Nationalities |

## Command-Line Tools

### dd-analyze
Complete corpus analysis with detailed statistics.

```bash
dd-analyze /path/to/corpus
```

**Generates:**
- Console output with complete statistics
- `corpus_statistics.json` - All statistics in JSON format

**Features:**
- Complete newspaper list with sources
- Library holdings by newspaper, year, and issue
- Missing issues estimates
- Year-by-year coverage
- Statistical summaries

### dd-excel-export
Excel-optimized export for pivot table analysis.

```bash
dd-excel-export /path/to/corpus
```

**Generates:**
- `corpus_pivot_table_data.csv` - Single CSV with all data (23 columns)
- `corpus_analysis_workbook.xlsx` - Multi-sheet Excel workbook (requires openpyxl)

**Perfect for:**
- Creating pivot tables and charts in Excel
- Interactive data exploration
- Custom cross-tabulations
- Data visualization

See the [Excel Pivot Tables Guide](https://github.com/Divergent-Discourses/DDC_CorpusStatistics/blob/main/docs/EXCEL_PIVOT_TABLES_GUIDE.md) for detailed usage.

### dd-analyze-advanced
Extended analysis with additional exports and checks.

```bash
dd-analyze-advanced /path/to/corpus
```

**Generates:**
- `corpus_statistics.json` - Complete statistics
- `corpus_detailed.csv` - Page-level data
- `corpus_issues.csv` - Issue-level data
- `library_holdings.csv` - Library holdings
- `missing_issues.csv` - Missing issues summary

**Additional Features:**
- Page-level completeness checking
- Duplicate page detection
- Monthly statistics
- Temporal gap analysis (>60 days)

### dd-reports
Generate detailed text reports.

```bash
dd-reports /path/to/corpus
```

**Generates:**
- `library_holdings_report.txt` - Comprehensive library holdings
- `missing_issues_report.txt` - Detailed missing issues analysis

**Use Cases:**
- Documentation
- Sharing with non-technical collaborators
- Detailed provenance tracking

### dd-validate
Validate filename compliance.

```bash
dd-validate /path/to/corpus
```

**Features:**
- Checks all files against expected pattern
- Reports invalid filenames with specific errors
- Suggests corrections for common issues

## Output Files

### Consolidated Export (Recommended for Excel)
```bash
dd-excel-export /path/to/corpus
```

Generates:
- **corpus_pivot_table_data.csv** - Single CSV with 23 columns including:
  - Date, Year, Month, Day, Quarter, Decade
  - Newspaper_Code, Newspaper_Name, Region, Publisher_Type
  - Administrative_Level, Province, Publication_Type
  - Pages_In_Issue, Completeness_Pct
  - Has_Missing_Pages, Has_Duplicate_Pages, Is_Complete_Issue
  - Primary_Library, All_Libraries, Num_Libraries
  - Estimated_Frequency, Avg_Gap_Days

- **corpus_analysis_workbook.xlsx** - Multi-sheet Excel workbook with:
  - Issues_Data (main pivot table sheet)
  - Newspapers_Summary
  - Library_Holdings
  - Yearly_Statistics
  - Missing_Issues
  - Issue_Completeness

### Advanced Analysis
```bash
dd-analyze-advanced /path/to/corpus
```

Generates:
- `corpus_statistics.json` - Complete statistics in JSON
- `corpus_detailed.csv` - Every page with metadata
- `corpus_issues.csv` - Every issue with completeness flags
- `library_holdings.csv` - Library holdings in tabular format
- `missing_issues.csv` - Missing issues estimates by newspaper

### Text Reports
```bash
dd-reports /path/to/corpus
```

Generates:
- `library_holdings_report.txt` - Detailed holdings breakdown
- `missing_issues_report.txt` - Gap analysis with estimates

## Requirements

- Python 3.6 or higher
- No required dependencies for basic functionality
- Optional: `openpyxl` for Excel export (`.xlsx` files)

```bash
pip install openpyxl  # Optional, for Excel export
```

## Python API Examples

### Basic Statistics

```python
from dd_corpus_tools import NewspaperCorpusAnalyzer

analyzer = NewspaperCorpusAnalyzer('/path/to/corpus')
analyzer.scan_corpus()

# Get totals
total_newspapers = len(analyzer.data)
total_issues = sum(len(dates) for dates in analyzer.issues.values())
total_pages = sum(analyzer.pages_by_newspaper.values())

print(f"Newspapers: {total_newspapers}")
print(f"Issues: {total_issues}")
print(f"Pages: {total_pages}")
```

### Query Specific Newspaper

```python
newspaper = 'TID'  # Tibet Daily

if newspaper in analyzer.data:
    issues = len(analyzer.issues[newspaper])
    pages = analyzer.pages_by_newspaper[newspaper]
    years = sorted(analyzer.data[newspaper].keys())
    
    print(f"{newspaper}:")
    print(f"  Issues: {issues}")
    print(f"  Pages: {pages}")
    print(f"  Years: {min(years)}-{max(years)}")
```

### Library Holdings

```python
for library in sorted(analyzer.libraries.keys()):
    total_pages = sum(analyzer.libraries[library].values())
    total_issues = sum(len(analyzer.library_issues[library][np]) 
                      for np in analyzer.library_issues[library])
    newspapers = len(analyzer.libraries[library])
    
    print(f"{library}: {newspapers} newspapers, {total_issues} issues, {total_pages} pages")
```

### Export Everything

```python
from dd_corpus_tools import ConsolidatedExporter

exporter = ConsolidatedExporter('/path/to/corpus')
exporter.scan_corpus()
exporter.export_all()  # Creates CSV + Excel workbook
```

More examples in [examples/example_usage.py](https://github.com/Divergent-Discourses/DDC_CorpusStatistics/blob/main/examples/example_usage.py).

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](https://github.com/Divergent-Discourses/DDC_CorpusStatistics/blob/main/CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Clone repository
git clone https://github.com/Divergent-Discourses/DDC_CorpusStatistics.git
cd DDC_CorpusStatistics

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e .[dev,excel]

# Run tests
pytest

# Format code
black dd_corpus_tools/
```

## Citation

If you use these tools in your research, please cite:

```bibtex
@software{dd_corpus_tools,
  title = {Divergent Discourses Corpus Analysis Tools},
  author = {{Divergent Discourses Project}},
  year = {2025},
  url = {https://github.com/Divergent-Discourses/DDC_CorpusStatistics},
  note = {Tools for analyzing Tibetan newspaper corpus (1950-1965)}
}
```

For the corpus itself:

```bibtex
@article{erhard2025divergent,
  title = {The Divergent Discourses Corpus: A Digital Collection of Early Tibetan Newspapers from the 1950s and 1960s},
  author = {Erhard, Franz Xaver},
  journal = {Revue d'Etudes Tibétaines},
  number = {74},
  pages = {44--80},
  year = {2025},
  month = {February}
}
```

## Acknowledgments

This project is part of the Divergent Discourses research project, funded by:
- Deutsche Forschungsgemeinschaft (DFG) - Project number 508232945
- Arts and Humanities Research Council (AHRC) - Project reference AH/X001504/1

## Contact

- **Project Website**: https://research.uni-leipzig.de/diverge/
- **GitHub Issues**: https://github.com/Divergent-Discourses/DDC_CorpusStatistics/issues

## Related Projects

- [Divergent Discourses Corpus](https://crossasia.org/) - Access the digitized newspapers
- [Divergent Discourses Project](https://research.uni-leipzig.de/diverge/) - Main research project

## Version History

See [CHANGELOG.md](https://github.com/Divergent-Discourses/DDC_CorpusStatistics/blob/main/CHANGELOG.md) for detailed version history.

## Support

- **Documentation**: https://github.com/Divergent-Discourses/DDC_CorpusStatistics/tree/main/docs
- **Examples**: https://github.com/Divergent-Discourses/DDC_CorpusStatistics/tree/main/examples
- **Issues**: https://github.com/Divergent-Discourses/DDC_CorpusStatistics/issues
- **Discussions**: Use GitHub Issues for questions and discussions
