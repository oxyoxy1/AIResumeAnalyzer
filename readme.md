Resume Analyzer

Overview

The Resume Analyzer is an AI-powered tool that helps users analyze and improve their resumes based on job descriptions. It extracts key resume details, evaluates skill relevance, and provides recommendations for improvement.

Features

Upload resumes in PDF or DOCX format

Extracts key details (name, email, phone, skills, etc.)

Matches resume content with job descriptions

Scores resume structure and skill relevance

Provides recommendations for improvement

User-friendly Tkinter GUI

Installation

Prerequisites

Ensure you have Python 3.8+ installed. Install required dependencies with:

pip install -r requirements.txt

Running the Application

python main.py

File Structure

Resume-Analyzer/
│── app/
│   ├── parser.py         # Extracts text from resumes
│   ├── extractor.py      # Extracts key details from resumes
│   ├── scorer.py         # Scores the resume based on job descriptions
│   ├── recommender.py    # Suggests improvements for resumes
│   ├── matcher.py        # Matches resume content with job postings
│   ├── main_window.py    # GUI implementation
│── main.py               # Application entry point
│── requirements.txt      # Python dependencies
│── LICENSE               # MIT License
│── README.md             # Project documentation

Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue.

License

This project is licensed under the MIT License. See LICENSE for details.