"""
Vercel FastAPI entry point.
Vercel auto-detects this file as a recognized FastAPI entry point.
"""
from source.app import app

__all__ = ["app"]
