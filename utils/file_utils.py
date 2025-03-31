import os
from typing import Optional


class FileUtils:
    """Utility class for handling file operations."""

    @staticmethod
    def read_file(file_path: str) -> Optional[str]:
        """
        Read the contents of a file.

        Args:
            file_path (str): Path to the file.

        Returns:
            str: Contents of the file, or None if an error occurs.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    @staticmethod
    def write_file(file_path: str, content: str) -> bool:
        """
        Write content to a file.

        Args:
            file_path (str): Path to the file.
            content (str): Content to write.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            return True
        except Exception as e:
            print(f"Error writing file: {e}")
            return False

    @staticmethod
    def is_valid_file(file_path: str, extensions: Optional[list] = None) -> bool:
        """
        Check if the file exists and has a valid extension.

        Args:
            file_path (str): Path to the file.
            extensions (list, optional): List of valid file extensions.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not os.path.isfile(file_path):
            return False

        if extensions:
            file_extension = os.path.splitext(file_path)[1].lower()
            return file_extension in extensions

        return True

    @staticmethod
    def save_results_to_file(results: dict, file_path: str) -> bool:
        """
        Save analysis results to a file in a readable format.

        Args:
            results (dict): Results dictionary.
            file_path (str): Path to save the file.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            content = "\n".join([f"{key.capitalize()}:\n{value}\n" for key, value in results.items()])
            return FileUtils.write_file(file_path, content)
        except Exception as e:
            print(f"Error saving results: {e}")
            return False

    @staticmethod
    def get_file_extension(file_path: str) -> str:
        """
        Get the extension of a file.

        Args:
            file_path (str): Path to the file.

        Returns:
            str: File extension.
        """
        return os.path.splitext(file_path)[1].lower()


# Example usage
if __name__ == "__main__":
    # Test file utilities
    content = FileUtils.read_file("sample.txt")
    if content:
        print("File content read successfully:")
        print(content)

    success = FileUtils.write_file("output.txt", "This is a test output.")
    if success:
        print("File written successfully.")

    is_valid = FileUtils.is_valid_file("sample.pdf", extensions=[".pdf", ".docx"])
    print(f"File is valid: {is_valid}")

    results = {
        "name": "John Doe",
        "skills": "Python, Machine Learning",
        "score": "85%"
    }
    save_success = FileUtils.save_results_to_file(results, "analysis_results.txt")
    print(f"Results saved successfully: {save_success}")