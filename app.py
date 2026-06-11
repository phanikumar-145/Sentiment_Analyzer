import streamlit as st
import requests

st.title(
    "AI Product Review Sentiment Analyzer"
)

review = st.text_area(
    "Enter Product Review"
)

if st.button("Analyze"):

    response = requests.post(
        "http://127.0.0.1:8000/analyze-review",
        json={
            "review": review
        }
    )

    st.write(
        response.json()
    )