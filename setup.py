"""Setup script for DD Corpus Tools (backward compatibility)"""

from setuptools import setup

# Read the long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dd-corpus-tools",
    use_scm_version=False,
    version="1.0.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
