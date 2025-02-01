import streamlit as st
import getpass
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()
st.set_page_config(layout="wide", page_title="LanguageBridge ")
st.markdown("<h1 style='text-align:center;color:blue;'>LanguageBridge </h1>",unsafe_allow_html=True)
col1, col2,col3 = st.columns([2,1,2])

def Training():
    llm=ChatOllama(temperature=0.3,model="llama3.2")

    prompt = ChatPromptTemplate.from_template(
        """You are a helpful assistant that translates {input_language} to {output_language}. and translate this sentence :{input}
         Only return the Translated sentence!"""
    )
    chain = prompt | llm
    st.session_state["model"]=chain

with col1:
    language_input=st.selectbox( "Select Input Language:",options=[
    "English", "Mandarin Chinese", "Hindi", "Spanish", "French", "Arabic", "Bengali",
    "Portuguese", "Russian", "Urdu", "German", "Japanese", "Punjabi", "Korean",
    "Italian", "Turkish", "Vietnamese", "Persian (Farsi)", "Swahili", "Dutch",
    "Tamil", "Telugu", "Marathi", "Gujarati", "Polish", "Ukrainian", "Malay",
    "Thai", "Hebrew", "Greek", "Basque", "Ainu", "Manx", "Cornish", "Chamicuro"
])

with col2:
    st.markdown("<h2 style='text-align: center;'>⇄</h2>", unsafe_allow_html=True)
with col3:
    language_output=st.selectbox("Select Output Language:",options=[
        "English", "Hindi", "Spanish", "French", "Arabic", "Bengali","Mandarin Chinese",
        "Portuguese", "Russian", "Urdu", "German", "Japanese", "Punjabi", "Korean",
        "Italian", "Turkish", "Vietnamese", "Persian (Farsi)", "Swahili", "Dutch",
        "Tamil", "Telugu", "Marathi", "Gujarati", "Polish", "Ukrainian", "Malay",
        "Thai", "Hebrew", "Greek", "Basque", "Ainu", "Manx", "Cornish", "Chamicuro"
    ])
    translation_container = st.container()
Training()
with col1:
    input_text = st.text_area("Enter the Sentence:")
with col3:
    output_container = st.empty()
    output_text = ""
    with output_container:
        translated_text = st.text_area("Translated Sentence:", value=output_text, height=100)
with col2:
    st.markdown("<br><br><br><br><br><br>",unsafe_allow_html=True)
    submitted=st.button("Translate",use_container_width=True)
if submitted:
    if "model" in st.session_state and input_text:
        chain = st.session_state["model"]
        output_text = chain.invoke(
            {"input_language": language_input, "output_language": language_output, "input": input_text})

        with col3:
            with translation_container:
                output_container.text_area("",value=output_text.content)
    else:
        st.warning("Please enter a sentence to translate.")

