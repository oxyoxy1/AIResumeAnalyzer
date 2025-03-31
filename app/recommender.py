class ResumeRecommender:
    """Class to provide recommendations for improving resumes."""

    def __init__(self, extracted_data: dict, job_description: str):
        """
        Initialize the ResumeRecommender.

        Args:
            extracted_data (dict): Extracted information from the resume.
            job_description (str): Text of the job description for comparison.
        """
        self.extracted_data = extracted_data
        self.job_description = job_description

    def recommend_missing_sections(self) -> list:
        """
        Recommend adding missing essential sections.

        Returns:
            list: List of missing sections.
        """
        required_sections = ["name", "email", "phone", "skills"]
        missing_sections = [section for section in required_sections if not self.extracted_data.get(section)]
        return missing_sections

    def recommend_skills(self) -> list:
        """
        Recommend skills to add based on the job description.

        Returns:
            list: List of suggested skills to add.
        """
        resume_skills = set(self.extracted_data.get("skills", []))
        job_skills = set(self.extract_keywords(self.job_description))
        missing_skills = job_skills - resume_skills
        return list(missing_skills)

    def recommend_formatting(self) -> list:
        """
        Recommend formatting improvements based on structure.

        Returns:
            list: List of formatting suggestions.
        """
        recommendations = []

        # Check if name is formatted as a single line at the beginning
        if self.extracted_data.get("name") and not self.extracted_data["name"].strip():
            recommendations.append("Ensure your name is formatted correctly and prominently at the top.")

        # Check for proper capitalization
        if self.extracted_data.get("skills"):
            for skill in self.extracted_data["skills"]:
                if skill != skill.capitalize():
                    recommendations.append(f"Capitalize the skill '{skill}' for consistency.")

        return recommendations

    def get_recommendations(self) -> dict:
        """
        Combine all recommendations into a single output.

        Returns:
            dict: Dictionary of recommendations.
        """
        return {
            "missing_sections": self.recommend_missing_sections(),
            "skills_to_add": self.recommend_skills(),
            "formatting_tips": self.recommend_formatting()
        }

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
        "phone": "",
        "skills": ["Python", "Data Analysis"]
    }

    # Sample job description
    job_description = """
    We are looking for a Data Scientist with skills in Python, Machine Learning, and Deep Learning.
    Experience with data analysis and NLP is a plus.
    """

    recommender = ResumeRecommender(extracted_data, job_description)

    recommendations = recommender.get_recommendations()
    print("Recommendations:")
    for category, tips in recommendations.items():
        print(f"\n{category.capitalize()}:")
        for tip in tips:
            print(f"- {tip}")