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
    page_icon="../avatar.png",
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
    st.write("Chat 💬")
    uploaded_files = st.file_uploader("Upload", accept_multiple_files=False, type=["pdf"])

    conn = Connection()
    # pdf_reader = PyPDF2.PdfReader(uploaded_files)
    # count = len(pdf_reader.pages)
    # all_page_text = ""
    # for page_num in range(count):
    #     page = pdf_reader.pages[page_num]
    #     all_page_text += page.extract_text()
    # with open("./Doc/doc", "wb") as f:
    #     f.write(all_page_text.encode())
    if uploaded_files is not None and uploaded_files.close():
        os.remove("./Doc/doc.pdf")

for message in st.session_state["messages"]:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.write(message["content"])

if prompt := st.chat_input("How I can help you?"):  # := means if prompt isn't none.
    response = conn.response(prompt)

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
