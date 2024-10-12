from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Define the resume and job description in Markdown
md_resume = """
# Jane Doe
## Professional Experience
### Senior Software Engineer, Tech Solutions Inc.
- Led the development of a microservices architecture for a high-traffic web application, improving scalability by 40%.
- Designed and implemented RESTful APIs in Python and Node.js, integrating third-party services and reducing latency by 30%.
- Collaborated with cross-functional teams to build a data pipeline using AWS Lambda and S3, automating data processing for real-time analytics.

### Software Engineer, Code Innovators
- Built a customer-facing dashboard with React.js, reducing page load times by 50% through optimization techniques.
- Contributed to backend development using Python, Flask, and PostgreSQL for a client management system, increasing performance by 20%.
"""

job_description = """
We are seeking a Senior Software Engineer with strong experience in designing scalable systems and working with cloud technologies. The ideal candidate should have expertise in Python, RESTful API development, and frontend frameworks like React.js. Experience with cloud platforms such as AWS is essential, and the candidate should be capable of leading technical teams and driving innovation.
"""

# Craft the prompt for OpenAI API
prompt = f"""
I have a resume in Markdown format and a job description. \
Please update my resume to better match the job description by \
highlighting relevant skills and achievements. Ensure the resume uses \
keywords and emphasizes leadership experience and cloud technology proficiency.

### Resume:
{md_resume}

### Job Description:
{job_description}

Please update the resume to:
- Include keywords from the job description.
- Emphasize leadership experience, cloud expertise (especially AWS), and RESTful API development.
- Ensure the resume highlights achievements related to the role.

Return the updated resume in Markdown format.
"""

# Make the API call
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a professional resume editor."},
        {"role": "user", "content": prompt}
    ], 
    temperature=0.25
)

# Extract the tailored resume
updated_resume = response.choices[0].message.content

# Print the updated resume
print(updated_resume)
