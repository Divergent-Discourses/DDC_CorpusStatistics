"""
Divergent Discourses Corpus Analysis Tools

A comprehensive toolkit for analyzing the Divergent Discourses Tibetan Newspaper
Corpus from the 1950s and 1960s.

This package provides tools for:
- Extracting metadata from standardized newspaper filenames
- Generating comprehensive statistics on newspapers, issues, and pages
- Analyzing library holdings and provenance
- Detecting missing issues and coverage gaps
- Exporting data in multiple formats (JSON, CSV, Excel)
"""

__version__ = "1.0.0"
__author__ = "Divergent Discourses Project"
__license__ = "MIT"

from .analyzer import NewspaperCorpusAnalyzer
from .advanced_analyzer import AdvancedCorpusAnalyzer
from .excel_exporter import ConsolidatedExporter
from .library_reporter import LibraryHoldingsReporter
from .constants import NEWSPAPER_NAMES, NEWSPAPER_METADATA

__all__ = [
    "NewspaperCorpusAnalyzer",
    "AdvancedCorpusAnalyzer",
    "ConsolidatedExporter",
    "LibraryHoldingsReporter",
    "NEWSPAPER_NAMES",
    "NEWSPAPER_METADATA",
]
