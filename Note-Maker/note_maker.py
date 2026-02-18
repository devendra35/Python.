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
    st.title(" Smart Note Maker")
st.caption("Upload text or PDF → Get clean study notes instantly")

input_method = st.radio("Choose input method:", ["Paste Text", "Upload PDF"])
if input_method == "Paste Text":
    content = st.text_area("Paste your content here:", height=250)
else:
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        content = read_pdf(uploaded_file)

if st.button(" Generate Notes"):
    if not content.strip():
        st.warning("Please provide some content.")
    else:
        with st.spinner("Generating smart notes..."):
            notes = generate_notes(content)
            st.success("Done!")
            st.text_area(" Your Notes:", notes, height=350)
            st.download_button(" Download Notes", notes, file_name="notes.txt")

st.markdown("---")
st.caption("Built by Deven.")




