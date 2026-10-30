from flask import Flask,render_template, request, send_file
from ranker import extract_text, rank_resumes
from pathlib import Path
import pandas as pd
import io

app = Flask(__name__)

ALLOWED_EXTENSIONS = {"pdf"}


@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    error = None

    #if request.method == "POST":
        #job_description = request.form.get(
           # "job_description", ""
        #).strip()

       # files = request.files.getlist("resumes")

       # if not job_description:
           # error = "Please enter a job description."

       # elif not any(f.filename for f in files):
           # error = "Please upload at least one PDF resume."

        #else:
           # resumes = []

           # for file in files:
               # if not file.filename:
                   # continue

               # if Path(file.filename).suffix.lower() != ".pdf":
                   # error = "Only PDF resumes are allowed."
                   # break

               # try:
                  #  pdf_bytes = file.read()

                   # with io.BytesIO(pdf_bytes) as pdf_stream:
                       # text = extract_text(pdf_stream)

                    #if text.strip():
                        #resumes.append(
                           # (Path(file.filename).name, text)
                       # )

               # except Exception:
                   # error = "A PDF could not be read. Please check your files."
                   # break

           # if not error and not resumes:
              #  error = "No readable text was found in the uploaded PDFs."

           # if not error:
               # results = rank_resumes(
                   # job_description, resumes
               # )

    return render_template(
        "index.html",
        results=results,
        error=error
    )


@app.route("/download", methods=["POST"])
def download():
    import json

    results_json = request.form.get("results", "[]")

    try:
        results = json.loads(results_json)
        df = pd.DataFrame(results)

        output = io.BytesIO()
        df.to_csv(output, index=False)
        output.seek(0)

        return send_file(
            output,
            mimetype="text/csv",
            as_attachment=True,
            download_name="resume_ranking_report.csv"
        )

    except (ValueError, TypeError):
        return "Invalid report data.", 400


if __name__ == "__main__":
    app.run(debug=True)

