# AI-Powered-Resume-Ranker
An AI-powered resume screening application using Python, NLP, TF-IDF, Scikit-learn, and Flask to rank candidates based on job description similarity.

# AI-Powered Resume Ranker

An AI-powered resume screening application that analyzes PDF resumes and ranks candidates based on their similarity to a given job description.

## Features
- Upload multiple PDF resumes.
- Extract text from PDF documents.
- Preprocess text using spaCy.
- Convert text into numerical features using TF-IDF.
- Calculate similarity scores using cosine similarity.
- Rank candidates automatically.
- Display candidate rankings through a Flask web interface.
- Download candidate ranking reports in CSV format.

## Technologies Used
- Python
- Flask
- spaCy
- Scikit-learn
- TF-IDF
- PyMuPDF
- Pandas
- HTML and CSS



1. Open `http://127.0.0.1:5000/` in your browser.

## How It Works
The application extracts resume text, processes it using NLP techniques, and compares it with the job description using TF-IDF and cosine similarity. Candidates are ranked according to their text similarity scores.

## Disclaimer
This project is an educational prototype. Similarity scores are not measures of candidate ability or hiring suitability. Final recruitment decisions should always involve human review.
