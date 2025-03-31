import tkinter as tk
from gui.main_window import ResumeAnalyzerApp


def main():
    """Main function to run the Resume Analyzer application."""
    root = tk.Tk()
    app = ResumeAnalyzerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()