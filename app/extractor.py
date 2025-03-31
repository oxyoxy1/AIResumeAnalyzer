import spacy
import re


class ResumeExtractor:
    """Class to extract key information from resume text."""

    def __init__(self, text: str):
        """
        Initialize the ResumeExtractor.

        Args:
            text (str): The raw text extracted from a resume.
        """
        self.text = text
        self.nlp = spacy.load("en_core_web_sm")

    def extract_name(self) -> str:
        """
        Extract the name from the resume text.

        Returns:
            str: The extracted name, or None if not found.
        """
        doc = self.nlp(self.text)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text
        return None

    def extract_email(self) -> str:
        """
        Extract the email address from the resume text.

        Returns:
            str: The extracted email address, or None if not found.
        """
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        match = re.search(email_pattern, self.text)
        return match.group() if match else None

    def extract_phone(self) -> str:
        """
        Extract the phone number from the resume text.

        Returns:
            str: The extracted phone number, or None if not found.
        """
        phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
        match = re.search(phone_pattern, self.text)
        return match.group() if match else None

    def extract_skills(self, skill_keywords: list) -> list:
        """
        Extract skills from the resume text based on a predefined list.

        Args:
            skill_keywords (list): A list of skill keywords to match.

        Returns:
            list: A list of extracted skills found in the resume.
        """
        skills_found = []
        for skill in skill_keywords:
            if re.search(rf"\b{re.escape(skill)}\b", self.text, re.IGNORECASE):
                skills_found.append(skill)
        return skills_found


# Example usage
if __name__ == "__main__":
    # Sample text for testing
    sample_text = """
    John Doe
    Email: johndoe@example.com
    Phone: (123) 456-7890
    Skills: Python, Machine Learning, Data Analysis, NLP
    """

    # Sample skill list
    skill_keywords = ["Python", "Machine Learning", "Data Analysis", "NLP", "Deep Learning"]

    extractor = ResumeExtractor(sample_text)

    print("Name:", extractor.extract_name())
    print("Email:", extractor.extract_email())
    print("Phone:", extractor.extract_phone())
    print("Skills:", extractor.extract_skills(skill_keywords))