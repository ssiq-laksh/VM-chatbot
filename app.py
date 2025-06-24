import streamlit as st
import requests

st.set_page_config(page_title="VM Chatbot")
st.title("VM Chatbot - Ask About Your VM Data")

API_URL = "http://localhost:8000/chat"

question = st.text_input("Ask a question about your VM data:")

if st.button("Ask") and question:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(API_URL, params={"question": question})
            if response.status_code == 200:
                st.success("Answer:")
                st.write(response.json().get("response", "No response returned."))
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Could not reach API: {e}")
