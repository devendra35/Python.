import streamlit as st
from openai import OpenAI
from pypdf import PdfReader

st.set_page_config(page_title="NoteCraft AI", page_icon="", layout="centered")

client = OpenAI(api_key="") #your api key


def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text
    def generate_notes(text):
    prompt = f"""
You are an expert teacher.
Convert the following content into clean structured notes with:
- Headings
- Bullet points
- Definitions
- Examples
- Summary at the end

CONTENT:
{text}
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


