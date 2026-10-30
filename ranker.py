import re
import pymupdf
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def extract_text(pdf_file):
    """Read text from a PDF resume."""
    text = ""

    with pymupdf.open(pdf_file) as pdf:
        for page in pdf:
            text += page.get_text()

    return text

def preprocess_text(text):
    """Clean and process text using spaCy."""
    text = re.sub(r"[^a-zA-Z0-9+#.\s]"," ", text)

    doc = nlp(text.lower())
    words = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and not token.is_space
    ]
    return " ".join(words)

def rank_resumes(job_description, resumes):
    """Compare resumes with the job description."""

    documents = [
        preprocess_text(job_description)
    ]

    documents += [
        preprocess_text(resume_text)
        for _, resume_text in resumes
    ]

    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    vectors = vectorizer.fit_transform(documents)

    scores = cosine_similarity(
        vectors[1:],
        vectors[0:1]
    ).flatten()

    results = []

    for i, (filename, resume_text) in enumerate(resumes):
        results.append({
            "filename": filename,
            "score": round(float(scores[i]) * 100, 2)
             })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    for rank, result in enumerate(results, start=1):
        result["rank"] = rank

    return results