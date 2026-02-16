# Excel Pivot Tables Guide
## Using the Consolidated Export for Analysis

This guide shows you how to use the consolidated export files in Excel for powerful data analysis.

---

## Quick Start

### 1. Generate the Files
```bash
python consolidated_excel_export.py /path/to/your/corpus
```

This creates:
- **`corpus_pivot_table_data.csv`** - Single flat file, perfect for pivot tables
- **`corpus_analysis_workbook.xlsx`** - Multi-sheet workbook (requires `pip install openpyxl`)

### 2. Open in Excel
- For CSV: Open `corpus_pivot_table_data.csv` in Excel
- For Excel: Open `corpus_analysis_workbook.xlsx` (recommended - has multiple sheets)

---

## Understanding the Data

### Main Sheet: Issues_Data

Each row represents **one issue** of a newspaper with these columns:

| Column | Description | Use in Pivot Tables |
|--------|-------------|-------------------|
| **Date** | Issue date (YYYY-MM-DD) | Timeline analysis |
| **Year** | Year (e.g., 1960) | Filter, rows, columns |
| **Month** | Month number (1-12) | Seasonal patterns |
| **Quarter** | Q1, Q2, Q3, Q4 | Quarterly analysis |
| **Decade** | 1950s, 1960s, etc. | Long-term trends |
| **Newspaper_Code** | 3-letter code (TID, QTN, etc.) | Filter, rows, columns |
| **Newspaper_Name** | Full name | Labels |
| **Region** | PRC or India | Regional comparisons |
| **Publisher_Type** | State, CTA, Independent, etc. | Categorical analysis |
| **Administrative_Level** | Provincial, Prefectural, County | Hierarchy analysis |
| **Province** | Qinghai, TAR, Sichuan, etc. | Geographic analysis |
| **Publication_Type** | General, Pictorial, etc. | Type comparisons |
| **Pages_In_Issue** | Number of pages | **Sum/Average** |
| **Has_Missing_Pages** | Yes/No | Filter quality |
| **Has_Duplicate_Pages** | Yes/No | Filter quality |
| **Primary_Library** | Main source library | Provenance |
| **All_Libraries** | All contributing libraries | Multi-source analysis |
| **Num_Libraries** | Count of libraries | Source diversity |
| **Estimated_Frequency** | Daily, Weekly, etc. | Publication patterns |
| **Is_Complete_Issue** | Yes/No | Quality filter |
| **Completeness_Pct** | 0-100% | **Average** quality |

---

## Example Pivot Tables

### 1. Issues and Pages by Year and Newspaper

**Setup:**
- **Rows:** Year
- **Columns:** Newspaper_Code
- **Values:** Count of Date (for issues), Sum of Pages_In_Issue (for pages)

**Result:** See how many issues and pages each newspaper published each year

**Excel Steps:**
1. Select any cell in your data
2. Insert → PivotTable
3. Drag "Year" to Rows
4. Drag "Newspaper_Code" to Columns
5. Drag "Date" to Values (should auto-count)
6. Drag "Pages_In_Issue" to Values (should auto-sum)

---

### 2. Coverage by Region and Decade

**Setup:**
- **Rows:** Region, Decade
- **Values:** Count of Date (issues), Sum of Pages_In_Issue (pages)

**Result:** Compare PRC vs India coverage over time

**Use filters to drill down:**
- Filter by Newspaper_Code
- Filter by Administrative_Level
- Filter by Is_Complete_Issue = "Yes"

---

### 3. Library Contributions

**Setup:**
- **Rows:** Primary_Library
- **Columns:** Newspaper_Code
- **Values:** Count of Date

**Result:** See which libraries contributed which newspapers

---

### 4. Publication Frequency Analysis

**Setup:**
- **Rows:** Newspaper_Code, Estimated_Frequency
- **Values:** Count of Date, Average of Completeness_Pct

**Result:** Compare different publication frequencies and their completeness

---

### 5. Quality Analysis

**Setup:**
- **Rows:** Newspaper_Code
- **Filters:** Has_Missing_Pages, Has_Duplicate_Pages
- **Values:** 
  - Count of Date
  - Count where Is_Complete_Issue = "Yes" (use filter)
  - Average of Completeness_Pct

**Result:** Quality metrics for each newspaper

---

### 6. Temporal Coverage by Province

**Setup:**
- **Rows:** Province, Year
- **Values:** Count of Date, Sum of Pages_In_Issue

**Result:** Year-by-year coverage for each province/region

---

### 7. Publisher Type Comparison

**Setup:**
- **Rows:** Publisher_Type, Administrative_Level
- **Values:** Count of Date, Sum of Pages_In_Issue
- **Filters:** Region

**Result:** Compare state vs independent vs CTA publications

---

## Advanced Filtering

### Example 1: Complete Daily Newspapers Only
**Filters:**
- Estimated_Frequency = "Daily"
- Is_Complete_Issue = "Yes"

### Example 2: Provincial-Level Publications 1960-1965
**Filters:**
- Administrative_Level = "Provincial"
- Year >= 1960
- Year <= 1965

### Example 3: Multi-Source Issues
**Filters:**
- Num_Libraries > 1

---

## Creating Charts

After creating a pivot table:

1. Click on the pivot table
2. Insert → PivotChart
3. Choose chart type:
   - **Column chart**: Compare issues/pages across newspapers or years
   - **Line chart**: Show trends over time
   - **Stacked bar**: Show composition by region/type
   - **Pie chart**: Show distribution

### Recommended Charts

**1. Issues Over Time by Region**
- Line chart
- Rows: Year
- Lines: Region
- Values: Count of Date

**2. Pages by Administrative Level**
- Column chart
- Rows: Administrative_Level
- Values: Sum of Pages_In_Issue

**3. Completeness by Newspaper**
- Bar chart (sorted)
- Rows: Newspaper_Code
- Values: Average of Completeness_Pct

---

## Using the Multi-Sheet Workbook

If you have the Excel workbook (`corpus_analysis_workbook.xlsx`), you get 6 pre-formatted sheets:

### Sheet 1: Issues_Data
Main data for pivot tables (described above)

### Sheet 2: Newspapers_Summary
One row per newspaper with totals
- Use for: Quick newspaper comparisons
- No pivot needed: Already summarized

### Sheet 3: Library_Holdings
Each library-newspaper combination
- Use for: Library contribution analysis
- Pivot by: Library_Code or Newspaper_Code

### Sheet 4: Yearly_Statistics
One row per year with totals
- Use for: Temporal overview
- No pivot needed: Already summarized

### Sheet 5: Missing_Issues
Estimated missing issues by newspaper
- Use for: Completeness assessment
- Sort by: Estimated_Missing or Completeness_Pct

### Sheet 6: Issue_Completeness
Page-level completeness by newspaper
- Use for: Quality comparison
- Sort by: Complete_Issues_Pct

---

## Tips for Best Results

### 1. Use Slicers (Excel 2010+)
Slicers make filtering visual and easy:
1. Click on pivot table
2. Insert → Slicer
3. Choose: Region, Decade, Publisher_Type, etc.
4. Click to filter instantly

### 2. Conditional Formatting
Highlight important data:
- High completeness percentages (green)
- Low completeness percentages (red)
- Large page counts (gradient)

### 3. Calculated Fields
Add custom calculations:
- **PivotTable Tools → Analyze → Fields, Items & Sets → Calculated Field**
- Examples:
  - `Average Pages = Pages_In_Issue / Count of Date`
  - `Completeness_Category = IF(Completeness_Pct > 90, "High", "Low")`

### 4. Grouping Dates
Right-click on a date field → Group:
- Group by Months, Quarters, Years
- Useful for aggregating daily data

### 5. Show Values As
Change how numbers display:
- **% of Grand Total**: See proportions
- **% of Column Total**: Compare within groups
- **Running Total**: Cumulative view
- **Difference From**: Year-over-year changes

---

## Common Analysis Scenarios

### Scenario 1: "How complete is our Tibet Daily collection?"

**Steps:**
1. Filter: Newspaper_Code = "TID"
2. Create pivot: Year (rows) vs Count of Date (values)
3. Add: Average of Completeness_Pct
4. Add: Count where Is_Complete_Issue = "Yes"
5. Create line chart showing completeness trend

### Scenario 2: "Which libraries contributed most to which regions?"

**Steps:**
1. Create pivot: Primary_Library (rows), Region (columns)
2. Values: Count of Date
3. Add: Sum of Pages_In_Issue
4. Create clustered bar chart

### Scenario 3: "Compare publication patterns in PRC vs India"

**Steps:**
1. Create pivot: Estimated_Frequency (rows), Region (columns)
2. Values: Count of Date
3. Format as % of column total
4. Create 100% stacked bar chart

### Scenario 4: "Yearly growth in corpus"

**Steps:**
1. Create pivot: Year (rows)
2. Values: Count of Date
3. Show values as: Running Total
4. Create line chart

---

## Troubleshooting

**Problem:** Dates showing as numbers
- **Solution:** Right-click column → Format Cells → Date

**Problem:** Can't create pivot table
- **Solution:** Ensure data range is selected, no blank columns

**Problem:** Numbers not summing correctly
- **Solution:** Check that Values field is set to "Sum" not "Count"

**Problem:** Excel file won't open
- **Solution:** Make sure `openpyxl` is installed: `pip install openpyxl`

**Problem:** Too much data, Excel is slow
- **Solution:** Use filters first to reduce dataset before creating pivots

---

## Next Steps

1. **Start Simple**: Try the basic year × newspaper pivot first
2. **Add Complexity**: Gradually add more fields
3. **Save Templates**: Save useful pivot configurations
4. **Refresh Data**: If corpus changes, regenerate files and refresh pivot tables
5. **Share Insights**: Export pivot table results for reports

---

## Additional Resources

- Microsoft Excel Pivot Tables Documentation
- YouTube: "Excel Pivot Tables Tutorial"
- Use the consolidated CSV for compatibility with Google Sheets
- Consider Power BI for very large datasets

---

**Questions?** Check the main README.md or visit:
https://research.uni-leipzig.de/diverge/
