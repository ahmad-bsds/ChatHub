
from langchain_community.vectorstores import chroma
from pdfReader import DocToken
import os
from langchain_community.embeddings import google_palm


os.environ["ALLOW_RESET"] = "True"
os.environ["GOOGLE_API_KEY"] = "AIzaSyBnOXear5WrP2FWdZ14tQATdy4_2i6aM-8"


class ChromaClass:

    def __init__(self):
        token = DocToken()
        embed = google_palm.GooglePalmEmbeddings()
        persist_dir = "./Collections"
        self.vector_db = chroma.Chroma.from_documents(
            documents=token.tokens(),
            embedding=embed,
            persist_directory=persist_dir
        )
        self.retriever = self.vector_db.as_retriever(search_kwargs={"k": 5})
# c = ChromaClass()
# print(c.retrieve("What is deep learning?"))



