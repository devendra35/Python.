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

