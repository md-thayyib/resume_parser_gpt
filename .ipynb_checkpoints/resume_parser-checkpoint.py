import os

from dotenv import load_dotenv
from langchain.llms import OpenAI
from PyPDF2 import PdfReader

import openai

load_dotenv()

llm = OpenAI(temperature=0.9)

# Read the PDF file and convert it to plain text
resume_file = "Aboobackert_dr (2).pdf"
with open(resume_file, "rb") as f:
    reader = PdfReader(f)
    resume_text = ""
    for page in range(len(reader.pages)):
        resume_text += reader.pages[page].extract_text()

# Set up OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the GPT-3 model and parameters


model_engine = "text-davinci-003"
prompt = (f"Parse the following resume{resume_text}\n\n like Name: in json format",)
max_tokens = 700
temperature = 0.2

response = openai.Completion.create(
    model=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    n=1,
    stop=None,
    temperature=temperature,
)
print(response.choices[0].text)
print(response)
