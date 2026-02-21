import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from source.app import app

__all__ = ["app"]