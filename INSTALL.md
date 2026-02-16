# Installation Guide

Detailed installation instructions for DD Corpus Tools.

## Requirements

- Python 3.6 or higher
- pip (Python package installer)

## Installation Methods

### Method 1: Install from PyPI (Recommended)

```bash
pip install dd-corpus-tools
```

### Method 2: Install from GitHub

```bash
pip install git+https://github.com/Divergent-Discourses/corpus-analysis-tools.git
```

### Method 3: Install from Source

```bash
# Clone the repository
git clone https://github.com/Divergent-Discourses/corpus-analysis-tools.git
cd corpus-analysis-tools

# Install in normal mode
pip install .

# OR install in development mode (editable)
pip install -e .
```

## Optional Dependencies

### Excel Export Support

For Excel (.xlsx) file generation:

```bash
pip install dd-corpus-tools[excel]
# or
pip install openpyxl
```

### Development Tools

For contributing to the project:

```bash
pip install dd-corpus-tools[dev]
```

This installs:
- pytest (testing)
- black (code formatting)
- flake8 (linting)
- mypy (type checking)

### All Dependencies

Install everything:

```bash
pip install dd-corpus-tools[all]
```

## Verification

Verify the installation:

```bash
# Check version
pip show dd-corpus-tools

# Test commands
dd-analyze --help
dd-excel-export --help
```

## Virtual Environments (Recommended)

### Using venv

```bash
# Create virtual environment
python -m venv dd-env

# Activate (Linux/Mac)
source dd-env/bin/activate

# Activate (Windows)
dd-env\Scripts\activate

# Install
pip install dd-corpus-tools

# When done
deactivate
```

### Using conda

```bash
# Create environment
conda create -n dd-env python=3.9

# Activate
conda activate dd-env

# Install
pip install dd-corpus-tools

# When done
conda deactivate
```

## Platform-Specific Notes

### Windows

If you encounter permission errors:

```bash
# Run as administrator or use --user flag
pip install --user dd-corpus-tools
```

### macOS

If using system Python, consider using Homebrew Python:

```bash
# Install Homebrew Python
brew install python3

# Install package
pip3 install dd-corpus-tools
```

### Linux

Most distributions should work out of the box. If you need Python 3.6+:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```

## Upgrading

### Upgrade to Latest Version

```bash
pip install --upgrade dd-corpus-tools
```

### Upgrade with Optional Dependencies

```bash
pip install --upgrade dd-corpus-tools[excel]
```

## Uninstallation

```bash
pip uninstall dd-corpus-tools
```

## Troubleshooting

### "Command not found: dd-analyze"

**Solution:**
1. Ensure scripts directory is in PATH
2. Reinstall: `pip install --force-reinstall dd-corpus-tools`
3. Try: `python -m dd_corpus_tools.cli`

### "No module named 'dd_corpus_tools'"

**Solution:**
1. Check installation: `pip list | grep dd-corpus`
2. Verify Python version: `python --version`
3. Reinstall in correct environment

### "Permission denied" errors

**Solution:**
1. Use `--user` flag: `pip install --user dd-corpus-tools`
2. Use virtual environment (recommended)
3. Check file permissions

### openpyxl not found

**Solution:**
```bash
pip install openpyxl
# or
pip install dd-corpus-tools[excel]
```

## Development Installation

For contributors:

```bash
# Clone repository
git clone https://github.com/Divergent-Discourses/corpus-analysis-tools.git
cd corpus-analysis-tools

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e .[dev,excel]

# Run tests
pytest

# Format code
black dd_corpus_tools/
```

## Docker Installation (Advanced)

For isolated environments:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN pip install dd-corpus-tools[excel]

CMD ["dd-analyze", "/corpus"]
```

Build and run:

```bash
docker build -t dd-corpus-tools .
docker run -v /path/to/corpus:/corpus dd-corpus-tools
```

## Support

If you encounter installation issues:

1. Check [GitHub Issues](https://github.com/Divergent-Discourses/corpus-analysis-tools/issues)
2. Create a new issue with:
   - Python version (`python --version`)
   - OS and version
   - Installation method used
   - Complete error message

## Next Steps

After installation:
- Read the [User Guide](docs/USER_GUIDE.md)
- Try the [Quick Reference](docs/QUICK_REFERENCE.md)
- Run examples: `python examples/example_usage.py /path/to/corpus`
