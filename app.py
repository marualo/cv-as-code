from flask import Flask, render_template, request
from services.cover_letter import generate_cover_letter
from services.pdf_parser import extract_text_from_pdf

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        
        action = request.form.get("action")

        if action == "load_pdf":

            pdf_file = request.files.get("cv_file")

            cv = ""

            if pdf_file:
                cv = extract_text_from_pdf(pdf_file)

            return render_template(
                "index.html",
                cv=cv,
                job_description=request.form.get(
                    "job_description",
                    ""
                ),
                company_info=request.form.get(
                    "company_info",
                    ""
                )
            )

        cv = request.form["cv"]
        job_description = request.form["job_description"]
        company_info = request.form["company_info"]
        
        cover_letter = generate_cover_letter(
            cv,
            job_description,
            company_info
        )

        return render_template(
            "result.html",
            cover_letter=cover_letter,
            cv=cv,
            job_description=job_description,
            company_info=company_info
        )

    return render_template("index.html")

@app.route("/regenerate", methods=["POST"])
def regenerate():

    cv = request.form["cv"]
    job_description = request.form["job_description"]
    company_info = request.form["company_info"]

    additional_instructions = request.form.get(
        "additional_instructions",
        ""
    )

    cover_letter = generate_cover_letter(
        cv,
        job_description,
        company_info,
        additional_instructions
    )

    return render_template(
        "result.html",
        cover_letter=cover_letter,
        cv=cv,
        job_description=job_description,
        company_info=company_info,
        additional_instructions=additional_instructions
    )

if __name__ == "__main__":
    app.run(debug=True)