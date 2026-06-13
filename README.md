# cv-as-code

Web application built with Flask that generates personalized cover letters from a candidate's CV, job description, and company information.

This project is being developed following DevOps practices including Git version control, automated CI/CD with GitHub Actions, testing, and future cloud deployment.

## Features

* Upload a CV as a PDF file
* Automatically extract text from uploaded PDFs
* Generate personalized cover letters using Groq LLMs
* Edit generated cover letters directly in the browser
* Regenerate cover letters with additional instructions
* Copy generated cover letters to the clipboard
* Download cover letters as TXT files
* Download cover letters as PDF files
* Return to the main form while preserving entered information
* Store prompts in external template files for easier maintenance

## Project Structure

```text
cv-as-code/
│
├── app.py
├── requirements.txt
├── README.md
│
├── prompts/
│   ├── cover_letter_prompt.txt
│   └── additional_instructions_prompt.txt
│
├── services/
│   ├── cover_letter.py
│   ├── pdf_parser.py
│   └── pdf_generator.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── tests/
```

## Setup

### Clone the repository

```bash
git clone <repo-url>
cd cv-as-code
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows Git Bash:

```bash
source venv/Scripts/activate
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_api_key_here
```

### Run the application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## Technologies Used

* Python
* Flask
* Groq API
* PyPDF2
* ReportLab
* HTML
* CSS
* JavaScript
* Git
* GitHub Actions

## Current Workflow

1. Upload a CV PDF or paste CV content.
2. Enter a job description.
3. Enter company information.
4. Generate a cover letter.
5. Edit the generated cover letter if desired.
6. Regenerate with additional instructions.
7. Copy or download the final version as TXT or PDF.

## CI/CD

GitHub Actions automatically runs tests on every push and pull request to help ensure the application remains stable.

## Future Improvements

* DOCX export
* Multiple cover letter styles
* Cover letter history
* Cloud deployment
* Authentication and user profiles
* Better PDF formatting and styling