# API Reference

Complete API documentation for DD Corpus Tools.

## Core Classes

### NewspaperCorpusAnalyzer

Main class for corpus analysis.

```python
from dd_corpus_tools import NewspaperCorpusAnalyzer

analyzer = NewspaperCorpusAnalyzer(corpus_root)
```

**Parameters:**
- `corpus_root` (str or Path): Path to the corpus directory

**Attributes:**
- `corpus_root`: Path to corpus
- `data`: Dictionary of newspaper data by year
- `issues`: Dictionary of issue dates by newspaper
- `pages_by_newspaper`: Total pages per newspaper
- `pages_by_year`: Total pages per year
- `libraries`: Library holdings dictionary
- `library_issues`: Issues per library per newspaper
- `library_years`: Years covered per library per newspaper

**Methods:**

#### scan_corpus()
Scan the corpus directory and extract metadata.

```python
analyzer.scan_corpus()
```

#### print_summary_statistics()
Print overall corpus statistics.

#### print_newspaper_list()
Print complete list of newspapers with details.

#### print_newspaper_statistics()
Print statistics for each newspaper.

#### print_yearly_statistics()
Print statistics by year.

#### print_library_statistics()
Print library holdings summary.

#### analyze_missing_issues()
Analyze and report missing issues.

#### export_to_json(output_file='corpus_statistics.json')
Export all statistics to JSON.

**Parameters:**
- `output_file` (str): Output filename

---

### AdvancedCorpusAnalyzer

Extended analyzer with additional analysis capabilities.

```python
from dd_corpus_tools import AdvancedCorpusAnalyzer

analyzer = AdvancedCorpusAnalyzer(corpus_root)
```

Inherits from `NewspaperCorpusAnalyzer`.

**Additional Methods:**

#### check_issue_completeness()
Check for issues with missing or duplicate pages.

#### find_temporal_gaps()
Identify temporal gaps in newspaper coverage.

#### export_detailed_csv(output_file='corpus_detailed.csv')
Export page-level data to CSV.

#### export_issues_csv(output_file='corpus_issues.csv')
Export issue-level summaries to CSV.

#### export_library_holdings_csv(output_file='library_holdings.csv')
Export library holdings to CSV.

#### export_missing_issues_csv(output_file='missing_issues.csv')
Export missing issues analysis to CSV.

---

### ConsolidatedExporter

Excel-optimized exporter for pivot table analysis.

```python
from dd_corpus_tools import ConsolidatedExporter

exporter = ConsolidatedExporter(corpus_root)
```

Inherits from `NewspaperCorpusAnalyzer`.

**Methods:**

#### export_consolidated_csv(output_file='corpus_pivot_table_data.csv')
Export consolidated CSV for pivot tables.

**Returns:** Path to created file

#### export_excel_workbook(output_file='corpus_analysis_workbook.xlsx')
Export multi-sheet Excel workbook.

Requires `openpyxl` to be installed.

**Returns:** Path to created file or None if openpyxl not available

#### export_all()
Export both CSV and Excel workbook.

---

### LibraryHoldingsReporter

Generates detailed text reports on library holdings and missing issues.

```python
from dd_corpus_tools import LibraryHoldingsReporter

reporter = LibraryHoldingsReporter(corpus_root)
```

Inherits from `NewspaperCorpusAnalyzer`.

**Methods:**

#### generate_library_holdings_report(output_file='library_holdings_report.txt')
Generate detailed library holdings report.

**Returns:** Path to created file

#### generate_missing_issues_report(output_file='missing_issues_report.txt')
Generate detailed missing issues report.

**Returns:** Path to created file

#### generate_combined_report()
Generate both holdings and missing issues reports.

---

## Utility Functions

### validate_filename(filename)

Validate if a filename matches the expected pattern.

```python
from dd_corpus_tools.utilities import validate_filename

is_valid, message = validate_filename("TID_1964_01_09_001_SB.jpg")
```

**Parameters:**
- `filename` (str): Filename to validate

**Returns:**
- `tuple`: (is_valid: bool, error_message: str)

---

### generate_filename(newspaper_code, year, month, day, page, library_code, shelfmark='', extension='.jpg')

Generate a properly formatted filename.

```python
from dd_corpus_tools.utilities import generate_filename

filename = generate_filename(
    newspaper_code='TID',
    year=1964,
    month=1,
    day=9,
    page=1,
    library_code='SB',
    shelfmark='Zsn128162MR'
)
# Returns: "TID_1964_01_09_001_SB_Zsn128162MR.jpg"
```

**Parameters:**
- `newspaper_code` (str): 3-letter newspaper code
- `year` (int): 4-digit year
- `month` (int): Month (1-12)
- `day` (int): Day (1-31)
- `page` (int): Page number (1-999)
- `library_code` (str): 2-letter library code
- `shelfmark` (str, optional): Shelfmark identifier
- `extension` (str, optional): File extension (default: '.jpg')

**Returns:**
- `str`: Formatted filename

**Raises:**
- `ValueError`: If parameters are invalid

---

### batch_validate_files(directory, fix_minor_errors=False)

Validate all files in a directory.

```python
from dd_corpus_tools.utilities import batch_validate_files

results = batch_validate_files('/path/to/corpus')
print(f"Valid: {len(results['valid'])}")
print(f"Invalid: {len(results['invalid'])}")
```

**Parameters:**
- `directory` (str or Path): Directory to validate
- `fix_minor_errors` (bool): Whether to suggest corrections (default: False)

**Returns:**
- `dict`: Dictionary with 'valid', 'invalid', and 'suggestions' keys

---

## Constants

### NEWSPAPER_NAMES

Dictionary mapping newspaper codes to full names.

```python
from dd_corpus_tools import NEWSPAPER_NAMES

print(NEWSPAPER_NAMES['TID'])
# Output: "Tibet Daily (bod ljongs nyin re'i gsar 'gyur)"
```

---

### NEWSPAPER_METADATA

Dictionary mapping newspaper codes to metadata.

```python
from dd_corpus_tools import NEWSPAPER_METADATA

metadata = NEWSPAPER_METADATA['TID']
print(metadata['region'])  # "PRC"
print(metadata['publisher'])  # "State"
print(metadata['level'])  # "Provincial"
```

**Metadata Fields:**
- `region`: Geographic region (PRC, India, Nepal)
- `publisher`: Publisher type (State, CTA, Independent, etc.)
- `type`: Publication type (General, Pictorial, etc.)
- `level`: Administrative level (Provincial, Prefectural, County, Institutional)
- `province`: Province or region (for PRC newspapers)

---

## Examples

### Example 1: Basic Statistics

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

### Example 2: Query Specific Newspaper

```python
newspaper = 'TID'

if newspaper in analyzer.data:
    issues = len(analyzer.issues[newspaper])
    pages = analyzer.pages_by_newspaper[newspaper]
    years = sorted(analyzer.data[newspaper].keys())
    
    print(f"{newspaper}:")
    print(f"  Issues: {issues}")
    print(f"  Pages: {pages}")
    print(f"  Years: {min(years)}-{max(years)}")
```

### Example 3: Library Holdings

```python
for library in sorted(analyzer.libraries.keys()):
    total_pages = sum(analyzer.libraries[library].values())
    newspapers = len(analyzer.libraries[library])
    
    print(f"{library}: {newspapers} newspapers, {total_pages} pages")
```

### Example 4: Year Range Analysis

```python
start_year, end_year = 1960, 1965

for year in range(start_year, end_year + 1):
    if year in analyzer.pages_by_year:
        pages = analyzer.pages_by_year[year]
        print(f"{year}: {pages} pages")
```

### Example 5: Export Everything

```python
from dd_corpus_tools import ConsolidatedExporter

exporter = ConsolidatedExporter('/path/to/corpus')
exporter.scan_corpus()
exporter.export_all()
```

---

## Error Handling

All methods that perform file operations may raise:

- `FileNotFoundError`: If corpus directory doesn't exist
- `PermissionError`: If unable to write output files
- `ValueError`: If invalid parameters are provided

Example with error handling:

```python
from dd_corpus_tools import NewspaperCorpusAnalyzer
from pathlib import Path

try:
    corpus_path = Path('/path/to/corpus')
    if not corpus_path.exists():
        raise FileNotFoundError(f"Corpus not found: {corpus_path}")
    
    analyzer = NewspaperCorpusAnalyzer(corpus_path)
    analyzer.scan_corpus()
    analyzer.export_to_json('output.json')
    
except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Permission denied: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

For more examples, see the [examples/](../examples/) directory.
