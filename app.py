import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint

import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '...'

def load_answer(query) -> str:
    llm = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-v0.1")
    response = llm.invoke(query,
                          temperature=0.5, 
                          max_new_tokens=50)
    return response


st.set_page_config(page_title="Simple Chatbot", page_icon=":robot_face:")
st.title("Simple Chatbot with HuggingFace Endpoint")
st.write("Ask me anything!")


def get_user_input():
    input =  st.text_input("You:",key='input')
    return input


user_input = get_user_input()

submit = st.button("Submit")

if submit and user_input:
    st.write(f"You: {user_input}")
    st.spinner("Generating response...")
    answer = load_answer(user_input)
    st.text_area("Chatbot:", value=answer, height=200)