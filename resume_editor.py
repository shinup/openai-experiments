from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Define md_resume and job_description
md_resume = """
# John Doe
## Experience
- Software Engineer at XYZ Corp
- Developed various applications using Python and JavaScript
"""

job_description = """
We are looking for a Software Engineer with experience in Python and JavaScript. The ideal candidate will have a strong background in developing web applications and working with REST APIs.
"""

# prompt
prompt = f"""
I have a resume formatted in Markdown and a job description. \
Please adapt my resume to better align with the job requirements while \
maintaining a professional tone. Tailor my skills, experiences, and \
achievements to highlight the most relevant points for the position. \
Ensure that my resume still reflects my unique qualifications and strengths \
but emphasizes the skills and experiences that match the job description.

### Here is my resume in Markdown:
{md_resume}

### Here is the job description:
{job_description}

Please modify the resume to:
- Use keywords and phrases from the job description.
- Adjust the bullet points under each role to emphasize relevant skills and achievements.
- Make sure my experiences are presented in a way that matches the required qualifications.
- Maintain clarity, conciseness, and professionalism throughout.

Return the updated resume in Markdown format.

"""
    
# make api call
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ], 
    temperature=0.25
)
    
# extract response
resume = response.choices[0].message.content

print(resume)