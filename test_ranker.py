
from ranker import rank_resumes

job_description = """
We need a Python developer with Machine Learning,
Flask, Natural Language Processing, and SQL skills.
"""

resumes = [
    (
        "candidate_a.pdf",
        "Python Machine Learning Flask NLP SQL developer"
    ),
    (
        "candidate_b.pdf",
        "Python Flask HTML CSS frontend developer"
    ),
    (
        "candidate_c.pdf",
        "Graphic Design Canva video editing"
    )
]

results = rank_resumes(job_description, resumes)

for candidate in results:
    print(
        f"Rank: {candidate['rank']} | "
        f"Resume: {candidate['filename']} | "
        f"Score: {candidate['score']}%"
    )
