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
            cover_letter=cover_letter
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)