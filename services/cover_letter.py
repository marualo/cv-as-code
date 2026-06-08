from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def generate_cover_letter(
    cv,
    job_description,
    company_info
):

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    prompt = f"""
Write a professional cover letter based on the following information.

CV:
{cv}

Job Description:
{job_description}

Company Information:
{company_info}

Requirements:
- Be professional
- Be concise
- Highlight relevant skills
- Use a formal business tone
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content

    except Exception as e:

        print(f"Error generating cover letter: {e}")
        
        return """
Sorry, we couldn't generate your cover letter right now.

Please try again later.
"""