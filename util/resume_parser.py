import json
import os
import uuid

import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

import openai

load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

def set_open_api_key(OPENAI_API_KEY):
    openai.api_key = OPENAI_API_KEY

def resume_parse(resume_file):
    reader = PdfReader(resume_file)
    resume_text = ""
    for page in reader.pages:
        resume_text+=page.extract_text()
    print(resume_text)

    

    # Set up OpenAI API credentials

    # Define the GPT-3 model and parameters

    prompt = (
        f"write an about me section by using following resume details\n\n{resume_text}",
    )
    if openai.api_key is not None:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=.5,
    )
    else:
        st.error("Api key error")
    return response, resume_text



if __name__ =="__main__":
    resume_file = "/Users/thayyib/Desktop/openai/resumes/Muhammed Ishan.k.pdf"
    model = "text-davinci-003"
    max_tokens = 1000
    temperature = 0.5


    response, resume_text = resume_parse(resume_file)
    cv_dict = response.choices[0].text

    # cv_dict = json.loads(response.choices[0].text)
    print(cv_dict)
