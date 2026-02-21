import sys
import os

# Add the project root to sys.path so that "source.*" imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from source.app import app

__all__ = ["app"]
