from flask import Flask, render_template, request
from services.cover_letter import generate_cover_letter

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

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