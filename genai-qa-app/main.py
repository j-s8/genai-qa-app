import streamlit as st
import requests

st.title("Ask Me Anything – Powered by Gemini")
prompt = st.text_input("Ask a question:")

if prompt:
    api_key = st.secrets["GEMINI_API_KEY"]
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    res = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
        headers=headers, params={"key": api_key}, json=data)

    if res.ok:
        st.write(res.json()["candidates"][0]["content"]["parts"][0]["text"])
    else:
        st.error("Something went wrong.")
