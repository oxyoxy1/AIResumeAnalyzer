# data/__init__.py

import json

def load_job_keywords(file_path="data/job_keywords.json"):
    """Load job keywords from the JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)

def load_stopwords(file_path="data/stopwords.txt"):
    """Load stopwords from the stopwords.txt file."""
    with open(file_path, "r") as file:
        return set(file.read().splitlines())

__all__ = ["load_job_keywords", "load_stopwords"]