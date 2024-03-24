import streamlit as st
from connections import Connection
from chroma import ChromaClass
from dotenv import load_dotenv

load_dotenv()

conn = Connection()

chroma = ChromaClass(file_path="./Doc/deepLearning.pdf")
chroma.__call__()


def main():
    USER_AVATAR = "♥️"
    BOT_AVATAR = "💬"
    # Streamlit Page Configuration
    st.set_page_config(
        page_title="ChatHub",
        page_icon="imgs/avatar_streamly.png",
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
        # uploaded_files = st.file_uploader("Upload", accept_multiple_files=False)


    for message in st.session_state["messages"]:
        avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
        with st.chat_message(message["role"], avatar=avatar):
            st.write(message["content"])

    if prompt := st.chat_input("How I can help you?"):  # := means if prompt isn't none.
        result = chroma.query(prompt)
        response = conn.response(f"""Answer the query: {result["query"]} from {result["context"]["documents"]} with the\
         help of your advance reasoning,\
         pattren mining and decision making ability.""")

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


# Code to run the main Streamlit app
if __name__ == "__main__":
    main()

chroma.__delete__()
