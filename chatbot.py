import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

#load the nev variables
load_dotenv()

#Streamlit page setup
st.set_page_config(
    page_title=" 💬ChatBot",
    page_icon ="🤖",
    layout="centered",
)

st.title("💬 Generative AI ChatBot")

#creating a session history to save previous historic chats as well- just like Chat GPT do- it is kind of variable where streamlit save it object
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#llm inintiate
llm =  ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)

#input box
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    response = llm.invoke(
        input=[{"role":"system", "content": "You have a knowledge of EMEA and UK Financial Asset Management Industry."
        " You are very specific and also know what product/ strategies used in differerent region to target client"
        "you also know market sentiments and current trends"}, *st.session_state.chat_history]
    )

    assistant_response=response.content
    st.session_state.chat_history.append({"role":"assistant", "content":assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)

