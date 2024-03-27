import PyPDF2
import streamlit as st
from connections import Connection
from dotenv import load_dotenv
from PyPDF2 import PdfFileReader
import os

load_dotenv()

USER_AVATAR = "♥️"
BOT_AVATAR = "💬"
# Streamlit Page Configuration
st.set_page_config(
    page_title="ChatHub",
    page_icon="./avatar.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "https://github.com/AdieLaine/Streamly",
        "Report a bug": "https://github.com/AdieLaine/Streamly",
        "About": """
            ## ChatHub AI assistant for your documents.

            **Techs used**
            - PalmAI
            - Langchain
            - Python 
        """
    }
)

# Streamlit Updates and Expanders
st.title("Streamly Streamlit Assistant")

# Creating a chat session:
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Sidebar:
with st.sidebar:
    st.write("Chat file upload here!")
    st.write("File less than 2mb is recommended. Responses may be slow ⚠️")
    uploaded_files = st.file_uploader("Upload", accept_multiple_files=False, type=["pdf"])
    if uploaded_files is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_files)
        # Create a new PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Add pages from the original PDF to the writer object
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        # Save the writer object to a new PDF file
        with open("./Doc/data.pdf", "wb") as output_pdf:
            pdf_writer.write(output_pdf)
        # setting up connection if file is uploaded.
        conn = Connection()

for message in st.session_state["messages"]:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.write(message["content"])

if prompt := st.chat_input("Upload a file to start!"):  # := means if prompt isn't none.
    if uploaded_files is not None:
        response = conn.response(prompt)
    else:
        response = "Please upload a file first to start!"

    # store user message in session.
    st.session_state["messages"].append(

        {
            "role": "user",
            "content": prompt
        }
    )
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        final_response = response
        # print message.
        st.markdown(final_response)
        # store this bot response in session as assistant.
        st.session_state["messages"].append(
            {
                "role": "assistant",
                "content": final_response
            }
        )
