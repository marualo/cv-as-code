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
Write a professional cover letter based ONLY on the information provided below:

CV:
{cv}

Job Description:
{job_description}

Company Information:
{company_info}

Before writing the cover letter:

1. Identify the most important requirements from the job description.
2. Identify the candidate's most relevant skills and experiences from the CV.
3. Determine the strongest matches between the candidate and the role.
4. Use those matches to build a tailored cover letter.

Requirements:
- Write a complete cover letter with greeting, body, and a professional closing and signature
- Keep the cover letter between 150 and 200 words and limit it to 3 paragraphs maximum
- Do not use placeholders such as [Your Name] or [Company Name]
- Be professional, concise and focused with a formal business tone, but not overly formal
- Avoid generic statements and clichés
- Avoid repeating information unnecessarily and repetitive phrases
- Avoid listing skills in a sequence
- Show evidence of skills through examples, prioritize evidence over self-description
- Prefer concrete examples over summaries
- Do not include information that is not present in the CV, job description, or company information
- Do not invent skills, experience, achievements, technologies, or qualifications
- Highlight relevant skills by referring to specific projects or experiences instead of listing technologies
- Focus on the strongest matches between the candidate profile and the role
- Support claims with examples from the candidate's experience when possible
- Mention the company naturally and explain why the role is appealing
- Use a natural and varied opening sentence
- The final paragraph must thank the reader and include a professional sign-off.
- The cover letter should feel personalized and written by a human, not like a generic template

Return only the final cover letter.
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