def generate_cover_letter(
    cv,
    job_description,
    company_info
):
    return f"""
Dear Hiring Manager,

I am excited to apply for this opportunity.

Based on my experience:

{cv[:200]}

and the job requirements:

{job_description[:200]}

I believe I would be a strong fit for your organization.

Sincerely,
Candidate
"""