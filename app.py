import streamlit as st
import requests

st.title("Local LLM Chat Interface By Toseef")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask something:")

if st.button("Send"):
    if user_input:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": user_input,
                "stream": False
            }
        )
        
        answer = response.json()["response"]
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", answer))

for role, message in st.session_state.history:
    st.write(f"**{role}:** {message}")

if st.button("Reset Chat"):
    st.session_state.history = []