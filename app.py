from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        cv = request.form["cv"]
        job_description = request.form["job_description"]
        company_info = request.form["company_info"]

        return f"""
        <h1>Data Received</h1>

        <h2>CV</h2>
        <p>{cv}</p>

        <h2>Job Description</h2>
        <p>{job_description}</p>

        <h2>Company Info</h2>
        <p>{company_info}</p>
        """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)