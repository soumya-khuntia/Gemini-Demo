import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get respones

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def get_gemini_response(question):
    response =chat.send_message(question,stream=True)
    return response

#initialize our streamlit app

st.set_page_config(page_title="Gemini Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input: Enter your prompt", key="input_key")
submit=st.button("Ask the question")

# If ask button is clicked

if submit or input:
    response=get_gemini_response(input)
    st.subheader("The Response is")
    for chunk in response:
        print(st.write(chunk.text))
    
