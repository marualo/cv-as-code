# This module extracts text from uploaded PDF files.
# The extracted text is later used to generate personalized cover letters.

from pypdf import PdfReader
# Reads PDF files and allows access to their pages and text content

# Extracts text from an uploaded PDF file
def extract_text_from_pdf(pdf_file):

    # Create a PDF reader object from the uploaded file
    reader = PdfReader(pdf_file)

    # Stores all extracted text from the PDF
    text = ""

    # Iterate through every page in the PDF
    for page in reader.pages:
        page_text = page.extract_text()  # Extract text from the current page

        # Only add text if extraction was successful
        if page_text:
            text += page_text + "\n"

    # Return the complete extracted text
    return text