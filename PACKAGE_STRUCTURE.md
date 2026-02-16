# DD Corpus Tools - GitHub Package Structure

## Repository: https://github.com/Divergent-Discourses/corpus-analysis-tools

Complete Python package for analyzing the Divergent Discourses Tibetan Newspaper Corpus.

## 📁 Package Structure

```
corpus-analysis-tools/
├── .github/                    # GitHub-specific files
│   ├── ISSUE_TEMPLATE/        # Issue templates
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/             # GitHub Actions
│       └── ci.yml             # Continuous Integration
│
├── dd_corpus_tools/           # Main package
│   ├── __init__.py           # Package initialization
│   ├── analyzer.py           # Core corpus analyzer
│   ├── advanced_analyzer.py  # Advanced analysis features
│   ├── excel_exporter.py     # Excel export functionality
│   ├── library_reporter.py   # Library holdings reporter
│   ├── constants.py          # Shared constants
│   ├── utilities.py          # Utility functions
│   └── cli.py                # Command-line interface
│
├── docs/                      # Documentation
│   ├── USER_GUIDE.md         # Complete user guide
│   ├── API_REFERENCE.md      # API documentation
│   ├── EXCEL_PIVOT_TABLES_GUIDE.md  # Excel tutorial
│   └── QUICK_REFERENCE.md    # Quick reference
│
├── examples/                  # Example code
│   └── example_usage.py      # Usage examples
│
├── tests/                     # Test suite
│   ├── __init__.py
│   └── test_basic.py         # Basic tests
│
├── .gitignore                # Git ignore rules
├── CHANGELOG.md              # Version history
├── CONTRIBUTING.md           # Contribution guidelines
├── INSTALL.md                # Installation guide
├── LICENSE                   # MIT License
├── MANIFEST.in               # Package manifest
├── README.md                 # Main README
├── pyproject.toml            # Modern Python packaging
├── requirements.txt          # Dependencies
└── setup.py                  # Setup script (backward compat)
```

## 🚀 Installation

```bash
pip install dd-corpus-tools
```

## 📝 Command-Line Tools

The package installs 5 command-line tools:

1. **dd-analyze** - Comprehensive corpus analysis
2. **dd-analyze-advanced** - Advanced analysis with additional exports
3. **dd-excel-export** - Excel-optimized export for pivot tables
4. **dd-reports** - Generate detailed text reports
5. **dd-validate** - Validate filename compliance

## 🐍 Python API

```python
from dd_corpus_tools import NewspaperCorpusAnalyzer

analyzer = NewspaperCorpusAnalyzer('/path/to/corpus')
analyzer.scan_corpus()
analyzer.print_summary_statistics()
```

## 📦 Package Distribution

### PyPI

Package is ready for upload to PyPI:

```bash
# Build distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*
```

### GitHub Releases

1. Tag the release: `git tag v1.0.0`
2. Push tags: `git push --tags`
3. Create release on GitHub with changelog

## 🔧 Development Setup

```bash
git clone https://github.com/Divergent-Discourses/corpus-analysis-tools.git
cd corpus-analysis-tools
pip install -e .[dev,excel]
pytest
```

## 📚 Documentation

Complete documentation in `docs/`:
- **USER_GUIDE.md** - Comprehensive usage guide
- **API_REFERENCE.md** - Complete API documentation
- **EXCEL_PIVOT_TABLES_GUIDE.md** - Excel analysis tutorial
- **QUICK_REFERENCE.md** - Quick command reference

## ✅ Quality Assurance

- **Tests**: pytest test suite in `tests/`
- **CI/CD**: GitHub Actions for automated testing
- **Code Style**: Black formatting, flake8 linting
- **Type Hints**: mypy type checking
- **Documentation**: Comprehensive guides and examples

## 📄 License

MIT License - see LICENSE file

## 🤝 Contributing

See CONTRIBUTING.md for guidelines

## 🎯 Features

✨ **Comprehensive Analysis**
- Automatic metadata extraction from filenames
- Complete newspaper catalog with provenance
- Library holdings by newspaper, year, and issue
- Missing issues estimation with frequency detection

📊 **Multiple Export Formats**
- JSON for programmatic access
- CSV for spreadsheet analysis
- Excel workbooks with multiple sheets
- Text reports for documentation

🏛️ **Detailed Tracking**
- Library holdings and provenance
- Multi-source issue identification
- Year-by-year coverage analysis
- Quality metrics and completeness checks

📈 **Excel-Optimized**
- Single consolidated CSV for pivot tables
- 23 comprehensive columns
- Pre-formatted Excel workbooks with 6 sheets
- Ready for data visualization

## 🔗 Links

- **Homepage**: https://research.uni-leipzig.de/diverge/
- **GitHub**: https://github.com/Divergent-Discourses/corpus-analysis-tools
- **Documentation**: https://github.com/Divergent-Discourses/corpus-analysis-tools/tree/main/docs
- **Issues**: https://github.com/Divergent-Discourses/corpus-analysis-tools/issues
- **PyPI**: https://pypi.org/project/dd-corpus-tools/ (pending upload)

## 📞 Contact

- Project Website: https://research.uni-leipzig.de/diverge/
- Email: diverge@uni-leipzig.de
- GitHub Issues: For bug reports and feature requests

---

**Ready for publication on GitHub and PyPI! 🎉**
