# app/__init__.py

# Import key modules for easy access when the app package is imported
from .parser import ResumeParser
from .extractor import ResumeExtractor
from .scorer import ResumeScorer
from .recommender import ResumeRecommender
from .matcher import ResumeMatcher

# Optionally, initialize common functionality for the app package