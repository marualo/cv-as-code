# This file is responsible for generating PDF files from generated cover letters.

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# ReportLab classes for creating PDF documents, adding formatted text paragraphs, and inserting blank spaces between elements
from reportlab.lib.styles import getSampleStyleSheet
# Loads ReportLab's built-in text styles

# Creates a PDF file from cover letter text
def create_pdf(text, filename):

    # Create a PDF document with the given filename
    pdf = SimpleDocTemplate(filename)

    # Load default ReportLab styles
    styles = getSampleStyleSheet()

    # List that will contain all PDF elements
    content = []

    # Convert Windows line endings to standard newlines
    text = text.replace("\r\n", "\n")

    # Split the text into paragraphs using blank lines
    for paragraph in text.split("\n"):

        # Convert text into a Paragraph object and add it to the content list
        content.append(
            Paragraph(paragraph, styles["BodyText"])
        )
    
        # Add vertical space between paragraphs
        content.append(
            Spacer(1, 12)
        )

    # Build and save the PDF file
    pdf.build(content)