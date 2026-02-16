"""Setup script for DD Corpus Tools (backward compatibility)"""

from setuptools import setup

# Read the long description from README
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "Analysis tools for the Divergent Discourses Tibetan Newspaper Corpus"

setup(
    name="dd-corpus-tools",
    version="1.0.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
