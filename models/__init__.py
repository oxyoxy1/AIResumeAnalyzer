# models/spacy_model/__init__.py

# Optionally, load your spaCy model here or expose an interface for using the model
import spacy

def load_spacy_model(model_name="en_core_web_sm"):
    """Load and return a spaCy model."""
    return spacy.load(model_name)

__all__ = ["load_spacy_model"]