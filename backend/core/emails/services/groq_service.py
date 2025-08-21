import os
from groq import Groq

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_cold_email(
    recipient_name,
    company,
    role,
    job_title,
    applicant_name,
    skills,
    portfolio,
    why_interested
):
    prompt = f"""
    You are a professional sales/recruitment assistant.
    Write a concise, professional cold email for a job application:
    
    Recipient Name: {recipient_name}
    Company: {company}
    Role: {role}
    Job Title: {job_title}
    Applicant Name: {applicant_name}
    Skills: {skills}
    Portfolio: {portfolio}
    Why interested: {why_interested}
    """
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content
