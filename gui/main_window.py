import tkinter as tk
from tkinter import filedialog, messagebox
from app.parser import ResumeParser
from app.extractor import ResumeExtractor
from app.scorer import ResumeScorer
from app.recommender import ResumeRecommender
from app.matcher import ResumeMatcher


class ResumeAnalyzerApp:
    """Main application window for the Resume Analyzer."""

    def __init__(self, root):
        """
        Initialize the main window.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("AI-Powered Resume Analyzer")
        self.root.geometry("800x600")

        # File path and job description variables
        self.resume_path = None
        self.job_description = None

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange UI components."""
        # File upload button
        self.upload_button = tk.Button(self.root, text="Upload Resume", command=self.upload_resume, width=20)
        self.upload_button.pack(pady=20)

        # Job description input
        self.job_desc_label = tk.Label(self.root, text="Enter Job Description:")
        self.job_desc_label.pack(pady=10)
        self.job_desc_text = tk.Text(self.root, height=10, width=60)
        self.job_desc_text.pack(pady=10)

        # Analyze button
        self.analyze_button = tk.Button(self.root, text="Analyze", command=self.analyze_resume, width=20)
        self.analyze_button.pack(pady=20)

        # Results display
        self.results_label = tk.Label(self.root, text="Results:", font=("Arial", 14))
        self.results_label.pack(pady=10)
        self.results_text = tk.Text(self.root, height=15, width=80, state="disabled")
        self.results_text.pack(pady=10)

    def upload_resume(self):
        """Handle resume file upload."""
        file_path = filedialog.askopenfilename(
            title="Select Resume",
            filetypes=(("PDF Files", "*.pdf"), ("DOCX Files", "*.docx"))
        )
        if file_path:
            self.resume_path = file_path
            messagebox.showinfo("Resume Uploaded", f"Resume uploaded: {file_path}")

    def analyze_resume(self):
        """Analyze the uploaded resume and job description."""
        if not self.resume_path:
            messagebox.showerror("Error", "Please upload a resume.")
            return

        self.job_description = self.job_desc_text.get("1.0", "end").strip()
        if not self.job_description:
            messagebox.showerror("Error", "Please enter a job description.")
            return

        try:
            # Parse and extract resume data
            parser = ResumeParser(self.resume_path)
            resume_text = parser.extract_text()
            extractor = ResumeExtractor(resume_text)
            extracted_data = {
                "name": extractor.extract_name(),
                "email": extractor.extract_email(),
                "phone": extractor.extract_phone(),
                "skills": extractor.extract_skills(skill_keywords=["Python", "Machine Learning", "Data Analysis", "NLP"])
            }

            # Score and recommend improvements
            scorer = ResumeScorer(extracted_data, self.job_description)
            recommender = ResumeRecommender(extracted_data, self.job_description)
            matcher = ResumeMatcher(extracted_data, self.job_description)

            skill_score = scorer.score_skills()
            structure_score = scorer.score_structure()
            total_score = scorer.calculate_total_score()
            recommendations = recommender.get_recommendations()
            match_score = matcher.calculate_total_match_score()

            # Display results
            self.results_text.config(state="normal")
            self.results_text.delete("1.0", "end")
            self.results_text.insert("end", f"Name: {extracted_data.get('name')}\n")
            self.results_text.insert("end", f"Email: {extracted_data.get('email')}\n")
            self.results_text.insert("end", f"Phone: {extracted_data.get('phone')}\n")
            self.results_text.insert("end", f"Skills: {', '.join(extracted_data.get('skills', []))}\n")
            self.results_text.insert("end", f"\nSkill Score: {skill_score:.2f}")
            self.results_text.insert("end", f"\nStructure Score: {structure_score:.2f}")
            self.results_text.insert("end", f"\nTotal Score: {total_score:.2f}")
            self.results_text.insert("end", f"\nMatch Score: {match_score:.2f}")
            self.results_text.insert("end", "\n\nRecommendations:\n")
            self.results_text.insert("end", f"Missing Sections: {', '.join(recommendations['missing_sections'])}\n")
            self.results_text.insert("end", f"Skills to Add: {', '.join(recommendations['skills_to_add'])}\n")
            self.results_text.insert("end", f"Formatting Tips: {' '.join(recommendations['formatting_tips'])}\n")
            self.results_text.config(state="disabled")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeAnalyzerApp(root)
    root.mainloop()