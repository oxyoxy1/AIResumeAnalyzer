class ResumeScorer:
    """Class to score resumes based on predefined criteria."""

    def __init__(self, extracted_data: dict, job_description: str, skill_weight: float = 0.6, structure_weight: float = 0.4):
        """
        Initialize the ResumeScorer.

        Args:
            extracted_data (dict): Extracted information from the resume.
            job_description (str): Text of the job description for comparison.
            skill_weight (float): Weight assigned to skill matching (default: 0.6).
            structure_weight (float): Weight assigned to resume structure (default: 0.4).
        """
        self.extracted_data = extracted_data
        self.job_description = job_description
        self.skill_weight = skill_weight
        self.structure_weight = structure_weight

    def score_skills(self) -> float:
        """
        Score the resume based on skills matching the job description.

        Returns:
            float: Skill match score (0 to 1).
        """
        resume_skills = set(self.extracted_data.get("skills", []))
        job_skills = set(self.extract_keywords(self.job_description))
        
        if not job_skills:
            return 0.0
        
        matched_skills = resume_skills.intersection(job_skills)
        return len(matched_skills) / len(job_skills)

    def score_structure(self) -> float:
        """
        Score the resume based on structural completeness.

        Returns:
            float: Structural score (0 to 1).
        """
        required_sections = ["name", "email", "phone", "skills"]
        found_sections = [section for section in required_sections if self.extracted_data.get(section)]
        return len(found_sections) / len(required_sections)

    def calculate_total_score(self) -> float:
        """
        Calculate the overall score for the resume.

        Returns:
            float: Total score (0 to 1).
        """
        skill_score = self.score_skills()
        structure_score = self.score_structure()
        total_score = (self.skill_weight * skill_score) + (self.structure_weight * structure_score)
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
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "(123) 456-7890",
        "skills": ["Python", "Machine Learning", "Data Analysis"]
    }

    # Sample job description
    job_description = """
    We are looking for a Data Scientist with skills in Python, Machine Learning, and Deep Learning.
    Experience with data analysis and NLP is a plus.
    """

    scorer = ResumeScorer(extracted_data, job_description)

    print("Skill Score:", scorer.score_skills())
    print("Structure Score:", scorer.score_structure())
    print("Total Score:", scorer.calculate_total_score())