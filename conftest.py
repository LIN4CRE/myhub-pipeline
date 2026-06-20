"""conftest.py — pytest root configuration."""
import sys
import pathlib

# Add project root to sys.path so test files can import src.* without hacks
sys.path.insert(0, str(pathlib.Path(__file__).parent))
