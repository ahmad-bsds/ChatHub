import chromadb
from langchain_community.vectorstores import chroma
from pdfReader import DocToken
import os
from langchain_community.embeddings import google_palm


os.environ["ALLOW_RESET"] = "True"
os.environ["GOOGLE_API_KEY"] = "API_KEY_HERE"


class ChromaClass:

    def __init__(self):
        token = DocToken()
        embed = google_palm.GooglePalmEmbeddings()
        persist_dir = "./Collections"
        self.vector_db = chroma.Chroma.from_documents(
            documents=token.tokens(),
            embedding=embed,
            persist_directory=persist_dir,
            client=chromadb.PersistentClient("./Collections")
        )
        self.vector_db.persist()
        self.retriever = self.vector_db.as_retriever(search_kwargs={"k": 5})

#
# c = ChromaClass()
# print(c.retriever.invoke("DL"))


