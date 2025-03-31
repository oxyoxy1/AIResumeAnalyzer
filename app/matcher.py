class ResumeMatcher:
    """Class to match resumes to job descriptions and calculate compatibility scores."""

    def __init__(self, extracted_data: dict, job_description: str):
        """
        Initialize the ResumeMatcher.

        Args:
            extracted_data (dict): Extracted information from the resume.
            job_description (str): Text of the job description.
        """
        self.extracted_data = extracted_data
        self.job_description = job_description

    def calculate_skill_match_score(self) -> float:
        """
        Calculate a compatibility score based on skill matching.

        Returns:
            float: Skill match score (0 to 1).
        """
        resume_skills = set(self.extracted_data.get("skills", []))
        job_skills = set(self.extract_keywords(self.job_description))
        
        if not job_skills:
            return 0.0
        
        matched_skills = resume_skills.intersection(job_skills)
        return len(matched_skills) / len(job_skills)

    def calculate_keyword_match_score(self) -> float:
        """
        Calculate a keyword match score between the resume text and job description.

        Returns:
            float: Keyword match score (0 to 1).
        """
        resume_text = self.extracted_data.get("text", "").lower()
        job_keywords = self.extract_keywords(self.job_description)

        if not job_keywords:
            return 0.0

        matched_keywords = [kw for kw in job_keywords if kw in resume_text]
        return len(matched_keywords) / len(job_keywords)

    def calculate_total_match_score(self, skill_weight=0.7, keyword_weight=0.3) -> float:
        """
        Calculate the total compatibility score.

        Args:
            skill_weight (float): Weight for skill matching (default: 0.7).
            keyword_weight (float): Weight for keyword matching (default: 0.3).

        Returns:
            float: Total match score (0 to 1).
        """
        skill_match_score = self.calculate_skill_match_score()
        keyword_match_score = self.calculate_keyword_match_score()

        total_score = (skill_weight * skill_match_score) + (keyword_weight * keyword_match_score)
        return round(total_score, 2)

    @staticmethod
    def extract_keywords(text: str) -> list:
        """
        Extract keywords from a given text.

        Args:
            text (str): Input text.

        Returns:
            list: List of keywords.
        """
        return [word.strip().lower() for word in text.split() if len(word) > 2]


# Example usage
if __name__ == "__main__":
    # Sample extracted data
    extracted_data = {
        "text": """
        John Doe is skilled in Python, Machine Learning, and Data Analysis.
        He has experience in NLP and Deep Learning.
        """,
        "skills": ["Python", "Machine Learning", "Data Analysis", "NLP"]
    }

    # Sample job description
    job_description = """
    We are looking for a Data Scientist with skills in Python, Machine Learning, and Deep Learning.
    Experience with data analysis and NLP is a plus.
    """

    matcher = ResumeMatcher(extracted_data, job_description)

    print("Skill Match Score:", matcher.calculate_skill_match_score())
    print("Keyword Match Score:", matcher.calculate_keyword_match_score())
    print("Total Match Score:", matcher.calculate_total_match_score())