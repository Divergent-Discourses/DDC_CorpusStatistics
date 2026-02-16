# Quick Reference Guide
## Divergent Discourses Corpus Analysis Tools

### Three Analysis Options

#### 1. Basic Analysis (Recommended for most users)
```bash
python newspaper_corpus_analyzer.py /path/to/corpus
```
**Outputs:**
- Console: Complete statistics display
- `corpus_statistics.json`: All statistics in JSON format

**What you get:**
- Complete newspaper list with sources
- Library holdings (by newspaper, year, issues)
- Missing issues estimates
- Year-by-year coverage
- Statistical summaries

---

#### 2. Advanced Analysis (For detailed research)
```bash
python advanced_corpus_analyzer.py /path/to/corpus
```
**Outputs:**
- Everything from basic analysis PLUS:
- `corpus_detailed.csv`: Every page with metadata
- `corpus_issues.csv`: Every issue with completeness flags
- `library_holdings.csv`: Library holdings in tabular format
- `missing_issues.csv`: Missing issues summary

**Additional features:**
- Page-level completeness checking
- Duplicate page detection
- Monthly statistics
- Temporal gap analysis (>60 days)

---

#### 3. **NEW: Consolidated Excel Export (Recommended for Excel users!)**
```bash
python consolidated_excel_export.py /path/to/corpus
```
**Outputs:**
- `corpus_pivot_table_data.csv`: **Single comprehensive CSV**
- `corpus_analysis_workbook.xlsx`: Multi-sheet Excel workbook

**What you get:**
- All data in one place, ready for pivot tables
- Pre-formatted Excel sheets
- Optimized for data analysis and visualization
- 23 columns including: Date, Year, Quarter, Decade, Region, Publisher, Province, Completeness, etc.

**See EXCEL_PIVOT_TABLES_GUIDE.md for detailed usage**

---

#### 4. Library Holdings Reporter (For detailed text reports)
```bash
python library_holdings_reporter.py /path/to/corpus
```
**Outputs:**
- `library_holdings_report.txt`: Comprehensive library holdings
- `missing_issues_report.txt`: Detailed gap analysis

**What you get:**
- Human-readable detailed reports
- Library-by-library breakdown
- Newspaper-by-newspaper breakdown
- Year-by-year coverage details
- Gap-by-gap analysis with estimates

---

### Quick Command Reference

| Task | Command |
|------|---------|
| Get overall statistics | `python newspaper_corpus_analyzer.py /path/to/corpus` |
| **Export for Excel pivot tables** | `python consolidated_excel_export.py /path/to/corpus` |
| Export to CSV for analysis | `python advanced_corpus_analyzer.py /path/to/corpus` |
| Generate readable reports | `python library_holdings_reporter.py /path/to/corpus` |
| Validate filenames | `python corpus_utilities.py /path/to/corpus` |

**Recommended for Excel users:** Use `consolidated_excel_export.py` - it creates a single CSV/Excel file optimized for pivot tables!

---

### Understanding the Output

#### Newspaper Codes
```
CWN = Central Weekly News
DTF = Defend Tibet's Freedom
FRD = Freedom
GDN = Ganze Daily
GTN = Gyantse News
KDN = Kangding News
MJN = Minjiang News
NIB = News in Brief
QTN = Qinghai Tibetan News
SGN = South Gansu News
TDP = Tibet Daily Pictorial
TID = Tibet Daily
TIF = Tibetan Freedom
TIM = Tibet Mirror
XNX = South-West Institute for Nationalities
ZYX = Central Institute for Nationalities
```

#### Library Codes
```
BD = Bodleian Library, Oxford
BL = British Library, London
CF = Collège de France, Paris
CU = Columbia University, New York
IT = University of Vienna
LT = Library of Tibetan Works and Archives
MV = Grassi Museum für Völkerkunde, Leipzig
NC = National Chengchi University, Taipei
OI = Oriental Institute, Prague
RB = Private Collection (Robbie Barnett)
SB = Staatsbibliothek zu Berlin
TL = LTWA, Dharamshala
TM = Tibet Museum
TS = Private Collection (Tenzin Sonam)
UW = University of Washington
```

---

### Interpreting Statistics

#### Complete Newspaper List
Shows every newspaper with:
- Total issues and pages in corpus
- Year range of coverage
- Which libraries hold copies

#### Library Holdings
Shows what each library contributed:
- **Summary level**: Total newspapers, issues, pages
- **By newspaper**: Which newspapers each library has
- **By year**: Year-by-year breakdown

#### Missing Issues
Estimates based on publication frequency:
- **Daily**: Expected ~1 day between issues
- **Weekly**: Expected ~7 days between issues
- **Monthly**: Expected ~30 days between issues

A "significant gap" is >2x the expected frequency.

---

### Common Use Cases

#### 1. "What do we have for Tibet Daily?"
```bash
python newspaper_corpus_analyzer.py /corpus
# Look in "COMPLETE NEWSPAPER LIST" section for TID
```

#### 2. "What did Columbia University contribute?"
```bash
python newspaper_corpus_analyzer.py /corpus
# Look in "STATISTICS BY LIBRARY/SOURCE" section for CU
```

#### 3. "How complete is our Qinghai Tibetan News collection?"
```bash
python library_holdings_reporter.py /corpus
# Check missing_issues_report.txt for QTN analysis
```

#### 4. "Export everything to Excel"
```bash
python advanced_corpus_analyzer.py /corpus
# Open corpus_detailed.csv in Excel
```

#### 5. "Export everything to Excel"
```bash
python consolidated_excel_export.py /corpus
# Open corpus_pivot_table_data.csv in Excel
# OR open corpus_analysis_workbook.xlsx (if you have openpyxl)
# Create pivot tables for any analysis you need!
```

---

### Using Excel Pivot Tables

After running `consolidated_excel_export.py`, you can create powerful pivot tables in Excel:

**Example Analyses:**
1. **Issues by Year and Newspaper**: See publication patterns
2. **Pages by Region and Decade**: Compare PRC vs India over time  
3. **Library Contributions**: Which libraries hold which newspapers
4. **Completeness Analysis**: Quality metrics by newspaper
5. **Temporal Gaps**: Find coverage gaps

**Quick Start in Excel:**
1. Open `corpus_pivot_table_data.csv` or `corpus_analysis_workbook.xlsx`
2. Click any cell in the data
3. Insert → PivotTable
4. Drag fields to create your analysis:
   - **Rows**: Year, Newspaper_Code, Region, etc.
   - **Columns**: Any categorical field
   - **Values**: Count of Date (for issues), Sum of Pages_In_Issue (for pages)

**See `EXCEL_PIVOT_TABLES_GUIDE.md` for detailed instructions and examples!**

---

### Additional Common Use Cases

#### "Which years have the best coverage?"
```bash
python newspaper_corpus_analyzer.py /corpus
# Look at "STATISTICS BY YEAR" section
# Or check the matrix view
```

---

### Tips

1. **Run basic analysis first** to get an overview
2. **Use advanced analysis** when you need CSV exports
3. **Generate text reports** for sharing with non-technical collaborators
4. **JSON output** is best for programmatic analysis
5. **Missing issues estimates** are approximations based on inferred frequency
6. **Library holdings** show the provenance of materials

---

### Troubleshooting

**Problem:** "No files found"
- Check that you're pointing to the correct directory
- Verify files have image extensions (.jpg, .png, .tif, .pdf)

**Problem:** "Invalid filenames reported"
- Check filename format: `XXX_YYYY_MM_DD_ppp_LL_abcd`
- Newspaper code must be exactly 3 uppercase letters
- Date format must be YYYY_MM_DD with underscores
- Page must be exactly 3 digits (use leading zeros)
- Library code must be exactly 2 uppercase letters

**Problem:** "Missing issues seem wrong"
- Estimates are based on inferred publication frequency
- Irregular publications may show inflated estimates
- Check the actual gap details in the report

---

### Support

For questions about the Divergent Discourses project:
https://research.uni-leipzig.de/diverge/
