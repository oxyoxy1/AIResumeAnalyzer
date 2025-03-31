import textract
from pathlib import Path


class ResumeParser:
    """Class to parse resumes from PDF or DOCX files."""

    SUPPORTED_FORMATS = ('.pdf', '.docx')

    def __init__(self, file_path: str):
        """
        Initialize the ResumeParser.

        Args:
            file_path (str): Path to the resume file.
        """
        self.file_path = Path(file_path)
        self.validate_file()

    def validate_file(self):
        """Validate the file format."""
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")
        if self.file_path.suffix.lower() not in self.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported file format: {self.file_path.suffix}. "
                f"Supported formats: {', '.join(self.SUPPORTED_FORMATS)}"
            )

    def extract_text(self) -> str:
        """
        Extract text from the resume file.

        Returns:
            str: Extracted text.
        """
        try:
            text = textract.process(str(self.file_path))
            return text.decode('utf-8').strip()
        except Exception as e:
            raise RuntimeError(f"Failed to extract text from {self.file_path}: {e}")


# Example usage
if __name__ == "__main__":
    # Example: Replace 'resume.pdf' with your actual resume file
    file_path = "data/sample_resumes/resume.pdf"
    parser = ResumeParser(file_path)

    try:
        text = parser.extract_text()
        print(f"Extracted text from {file_path}:\n{text[:500]}")  # Print first 500 characters
    except Exception as e:
        print(f"Error: {e}")