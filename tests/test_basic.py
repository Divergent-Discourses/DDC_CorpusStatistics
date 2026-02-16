"""Tests for DD Corpus Tools"""

import pytest
from pathlib import Path
import tempfile
import os

from dd_corpus_tools import NewspaperCorpusAnalyzer
from dd_corpus_tools.constants import NEWSPAPER_NAMES, NEWSPAPER_METADATA
from dd_corpus_tools.utilities import validate_filename, generate_filename


class TestFilenameValidation:
    """Test filename validation and generation"""
    
    def test_valid_filename(self):
        """Test validation of a valid filename"""
        is_valid, msg = validate_filename("TID_1964_01_09_001_SB_Zsn128162MR.jpg")
        assert is_valid is True
        assert msg == "Valid"
    
    def test_invalid_newspaper_code(self):
        """Test validation with invalid newspaper code"""
        is_valid, msg = validate_filename("ABCD_1964_01_09_001_SB.jpg")
        assert is_valid is False
        assert "newspaper code" in msg.lower()
    
    def test_invalid_year(self):
        """Test validation with invalid year"""
        is_valid, msg = validate_filename("TID_64_01_09_001_SB.jpg")
        assert is_valid is False
        assert "year" in msg.lower()
    
    def test_generate_filename(self):
        """Test filename generation"""
        filename = generate_filename(
            newspaper_code='TID',
            year=1964,
            month=1,
            day=9,
            page=1,
            library_code='SB',
            shelfmark='Zsn128162MR',
            extension='.jpg'
        )
        assert filename == "TID_1964_01_09_001_SB_Zsn128162MR.jpg"
        is_valid, _ = validate_filename(filename)
        assert is_valid is True


class TestConstants:
    """Test constants are properly defined"""
    
    def test_newspaper_names_exist(self):
        """Test that newspaper names are defined"""
        assert len(NEWSPAPER_NAMES) > 0
        assert 'TID' in NEWSPAPER_NAMES
        assert 'QTN' in NEWSPAPER_NAMES
    
    def test_newspaper_metadata_exists(self):
        """Test that newspaper metadata is defined"""
        assert len(NEWSPAPER_METADATA) > 0
        assert 'TID' in NEWSPAPER_METADATA
        assert 'region' in NEWSPAPER_METADATA['TID']


class TestCorpusAnalyzer:
    """Test corpus analyzer with sample data"""
    
    @pytest.fixture
    def sample_corpus(self, tmp_path):
        """Create a sample corpus for testing"""
        # Create sample directory structure
        corpus_dir = tmp_path / "corpus"
        corpus_dir.mkdir()
        
        # Create sample newspaper pages
        files = [
            "TID_1964_01_09_001_SB.jpg",
            "TID_1964_01_09_002_SB.jpg",
            "QTN_1965_05_15_001_CU.jpg",
        ]
        
        for filename in files:
            (corpus_dir / filename).touch()
        
        return corpus_dir
    
    def test_analyzer_scan(self, sample_corpus):
        """Test that analyzer can scan a corpus"""
        analyzer = NewspaperCorpusAnalyzer(sample_corpus)
        analyzer.scan_corpus()
        
        # Should find 3 pages
        total_pages = sum(analyzer.pages_by_newspaper.values())
        assert total_pages == 3
        
        # Should find 2 newspapers
        assert len(analyzer.data) == 2
        assert 'TID' in analyzer.data
        assert 'QTN' in analyzer.data
    
    def test_parse_filename(self, sample_corpus):
        """Test filename parsing"""
        analyzer = NewspaperCorpusAnalyzer(sample_corpus)
        
        parsed = analyzer.parse_filename("TID_1964_01_09_001_SB_Zsn128162MR.jpg")
        
        assert parsed is not None
        assert parsed['newspaper'] == 'TID'
        assert parsed['year'] == 1964
        assert parsed['month'] == 1
        assert parsed['day'] == 9
        assert parsed['page'] == 1
        assert parsed['library'] == 'SB'
        assert parsed['shelfmark'] == 'Zsn128162MR'


if __name__ == '__main__':
    pytest.main([__file__])
