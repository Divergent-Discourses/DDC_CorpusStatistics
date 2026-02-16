# User Guide

Complete guide to using the Divergent Discourses Corpus Analysis Tools.

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Command-Line Tools](#command-line-tools)
4. [Python API](#python-api)
5. [Output Files](#output-files)
6. [Advanced Usage](#advanced-usage)
7. [Troubleshooting](#troubleshooting)

## Installation

### From PyPI (Recommended)

```bash
pip install dd-corpus-tools
```

### From Source

```bash
git clone https://github.com/Divergent-Discourses/corpus-analysis-tools.git
cd corpus-analysis-tools
pip install -e .
```

### Optional Dependencies

For Excel export (.xlsx files):
```bash
pip install dd-corpus-tools[excel]
# or
pip install openpyxl
```

For development:
```bash
pip install dd-corpus-tools[dev]
```

## Quick Start

### Basic Analysis

```bash
dd-analyze /path/to/corpus
```

This command:
- Scans your corpus directory
- Extracts metadata from filenames
- Generates comprehensive statistics
- Exports `corpus_statistics.json`

### Excel Export (Recommended for Data Analysis)

```bash
dd-excel-export /path/to/corpus
```

This command creates:
- `corpus_pivot_table_data.csv` - Single CSV for pivot tables
- `corpus_analysis_workbook.xlsx` - Multi-sheet Excel workbook

## Command-Line Tools

### dd-analyze

Comprehensive corpus analysis with detailed statistics.

```bash
dd-analyze /path/to/corpus
```

**Output:**
- Console: Complete statistics display
- File: `corpus_statistics.json`

**Features:**
- Complete newspaper list
- Library holdings by newspaper, year, and issue
- Missing issues estimates
- Year-by-year coverage
- Statistical summaries

### dd-analyze-advanced

Extended analysis with additional exports and checks.

```bash
dd-analyze-advanced /path/to/corpus
```

**Output Files:**
- `corpus_statistics.json` - All statistics
- `corpus_detailed.csv` - Page-level data
- `corpus_issues.csv` - Issue-level summaries
- `library_holdings.csv` - Library holdings
- `missing_issues.csv` - Missing issues estimates

**Additional Features:**
- Page completeness checking
- Duplicate page detection
- Monthly statistics
- Temporal gap analysis

### dd-excel-export

Optimized export for Excel pivot table analysis.

```bash
dd-excel-export /path/to/corpus
```

**Output Files:**
- `corpus_pivot_table_data.csv` - Consolidated CSV
- `corpus_analysis_workbook.xlsx` - Excel workbook (if openpyxl installed)

**Excel Workbook Sheets:**
1. Issues_Data - Main pivot table data
2. Newspapers_Summary - Newspaper summaries
3. Library_Holdings - Library holdings
4. Yearly_Statistics - Year-by-year stats
5. Missing_Issues - Gap analysis
6. Issue_Completeness - Quality metrics

See [Excel Pivot Tables Guide](EXCEL_PIVOT_TABLES_GUIDE.md) for detailed usage.

### dd-reports

Generate detailed text reports.

```bash
dd-reports /path/to/corpus
```

**Output Files:**
- `library_holdings_report.txt` - Detailed library holdings
- `missing_issues_report.txt` - Missing issues analysis

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
- Reports invalid filenames
- Suggests corrections

## Python API

### Basic Usage

```python
from dd_corpus_tools import NewspaperCorpusAnalyzer

# Create analyzer
analyzer = NewspaperCorpusAnalyzer('/path/to/corpus')

# Scan corpus
analyzer.scan_corpus()

# Print statistics
analyzer.print_summary_statistics()
analyzer.print_newspaper_statistics()

# Export to JSON
analyzer.export_to_json('my_statistics.json')
```

### Advanced Analysis

```python
from dd_corpus_tools import AdvancedCorpusAnalyzer

analyzer = AdvancedCorpusAnalyzer('/path/to/corpus')
analyzer.scan_corpus()

# Check issue completeness
analyzer.check_issue_completeness()

# Find temporal gaps
analyzer.find_temporal_gaps()

# Export multiple formats
analyzer.export_detailed_csv('detailed.csv')
analyzer.export_issues_csv('issues.csv')
```

### Excel Export

```python
from dd_corpus_tools import ConsolidatedExporter

exporter = ConsolidatedExporter('/path/to/corpus')
exporter.scan_corpus()

# Export CSV for pivot tables
exporter.export_consolidated_csv('pivot_data.csv')

# Export Excel workbook (requires openpyxl)
exporter.export_excel_workbook('workbook.xlsx')
```

### Library Reports

```python
from dd_corpus_tools import LibraryHoldingsReporter

reporter = LibraryHoldingsReporter('/path/to/corpus')
reporter.scan_corpus()

# Generate reports
reporter.generate_library_holdings_report('holdings.txt')
reporter.generate_missing_issues_report('missing.txt')
```

### Accessing Data Programmatically

```python
analyzer = NewspaperCorpusAnalyzer('/path/to/corpus')
analyzer.scan_corpus()

# Get total statistics
total_newspapers = len(analyzer.data)
total_issues = sum(len(dates) for dates in analyzer.issues.values())
total_pages = sum(analyzer.pages_by_newspaper.values())

# Access newspaper-specific data
for newspaper in analyzer.data:
    issues = len(analyzer.issues[newspaper])
    pages = analyzer.pages_by_newspaper[newspaper]
    years = sorted(analyzer.data[newspaper].keys())
    print(f"{newspaper}: {issues} issues, {pages} pages ({min(years)}-{max(years)})")

# Access library holdings
for library in analyzer.libraries:
    for newspaper in analyzer.libraries[library]:
        issues = len(analyzer.library_issues[library][newspaper])
        pages = analyzer.libraries[library][newspaper]
        print(f"{library} - {newspaper}: {issues} issues, {pages} pages")
```

## Output Files

### JSON Format

```json
{
  "summary": {
    "total_newspapers": 16,
    "total_issues": 3489,
    "total_pages": 16718
  },
  "newspapers": {
    "TID": {
      "name": "Tibet Daily",
      "total_issues": 1980,
      "total_pages": 7641
    }
  },
  "libraries": {
    "SB": {
      "total_pages": 4890,
      "total_issues": 1245,
      "newspapers": {
        "TID": {
          "issues": 782,
          "pages": 3641
        }
      }
    }
  }
}
```

### CSV Formats

**Consolidated CSV (for pivot tables):**
23 columns including Date, Year, Newspaper_Code, Region, Publisher_Type, Pages_In_Issue, etc.

**Detailed CSV:**
Page-level data with metadata for each page

**Issues CSV:**
Issue-level summaries with completeness flags

**Library Holdings CSV:**
Library × Newspaper combinations with year ranges

## Advanced Usage

### Custom Analysis

```python
analyzer = NewspaperCorpusAnalyzer('/path/to/corpus')
analyzer.scan_corpus()

# Find issues from a specific year range
def get_issues_by_year_range(analyzer, newspaper, start_year, end_year):
    issues = []
    for year in range(start_year, end_year + 1):
        if year in analyzer.issues_by_year[newspaper]:
            issues.extend(sorted(analyzer.issues_by_year[newspaper][year]))
    return issues

tid_1960s = get_issues_by_year_range(analyzer, 'TID', 1960, 1969)
print(f"TID issues in 1960s: {len(tid_1960s)}")
```

### Filtering and Analysis

```python
# Find newspapers with >1000 pages
large_newspapers = {
    np: analyzer.pages_by_newspaper[np]
    for np in analyzer.data
    if analyzer.pages_by_newspaper[np] > 1000
}

# Find most complete collections
completeness = {}
for newspaper in analyzer.data:
    dates = sorted(analyzer.issues[newspaper])
    if len(dates) > 1:
        # Calculate based on frequency
        completeness[newspaper] = len(dates)

# Find multi-source newspapers
multi_source = {}
for newspaper in analyzer.data:
    libraries = [lib for lib in analyzer.libraries 
                if newspaper in analyzer.libraries[lib]]
    if len(libraries) > 1:
        multi_source[newspaper] = libraries
```

## Troubleshooting

### Common Issues

**Issue:** "No files found"
- **Solution:** Verify corpus path is correct
- Check that files have valid extensions (.jpg, .png, .tif, .pdf)

**Issue:** "Invalid filenames reported"
- **Solution:** Run `dd-validate` to identify problems
- Ensure filenames match pattern: `XXX_YYYY_MM_DD_ppp_LL_abcd.ext`

**Issue:** "Excel file won't open"
- **Solution:** Install openpyxl: `pip install openpyxl`
- CSV will still work without openpyxl

**Issue:** "Memory error with large corpus"
- **Solution:** Process in batches or increase system memory
- Use CSV exports instead of loading all data in memory

### Getting Help

- Check the [Quick Reference](QUICK_REFERENCE.md)
- See [Excel Pivot Tables Guide](EXCEL_PIVOT_TABLES_GUIDE.md) for Excel usage
- Open an issue on GitHub
- Contact project maintainers

## Next Steps

- See [Excel Pivot Tables Guide](EXCEL_PIVOT_TABLES_GUIDE.md) for data analysis
- Check [examples/](../examples/) for code samples
- Read [API Reference](API_REFERENCE.md) for detailed API documentation
- Visit [Contributing Guidelines](../CONTRIBUTING.md) to contribute
