# This module contains the main logic for generating a cover letter using the Groq LLM API.
# It takes the user's input to create a prompt that is sent to the LLM, which then generates a personalized cover letter.

from groq import Groq
# Groq SDK used to send prompts to the LLM
from dotenv import load_dotenv
# Loads variables from the .env file
import os
# Provides access to operating system features like env variables

load_dotenv()
# Makes variables from .env available through os.getenv()

# Generates a cover letter using the candidate's CV, job description, company information,
# and optional additional instructions provided by the user.
def generate_cover_letter(
    cv,
    job_description,
    company_info,
    additional_instructions=""
):
    # Creates an authenticated Groq client using the API key stored in the env variables
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    # Load the main cover letter prompt template
    with open(
        "prompts/cover_letter_prompt.txt",
        "r",  # Read mode
        encoding="utf-8"  # Ensures proper handling of special characters
    ) as file:
        prompt_template = file.read()
    
    # Replace template placeholders with the user's data
    prompt = prompt_template.replace(
        "{{cv}}",
        cv
    )

    prompt = prompt.replace(
        "{{job_description}}",
        job_description
    )

    prompt = prompt.replace(
        "{{company_info}}",
        company_info
    )

    if additional_instructions:

        # Load the optional additional instructions template
        with open(
            "prompts/additional_instructions_prompt.txt",
            "r",
            encoding="utf-8"
        ) as file:
            additional_prompt = file.read()

        additional_prompt = additional_prompt.replace(
            "{{additional_instructions}}",
            additional_instructions
        )

        prompt += additional_prompt

    try:
        # Send the completed prompt to the LLM and generate a cover letter
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # A LLM model from Groq
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content  # Extracts and returns the generated cover letter from the API response

    # Return a failure message if the API request fails
    except Exception as error:

        print(f"Error generating cover letter: {error}")
        
        return """
Sorry, we couldn't generate your cover letter right now.

Please try again later.
"""