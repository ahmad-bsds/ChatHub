from typing import Dict, List, Any, Sequence, Mapping

import chromadb
import chromadb.utils.embedding_functions as embedding_functions
import uuid
from chromadb import Documents, EmbeddingFunction, Embeddings, QueryResult
from numpy import ndarray, dtype, unsignedinteger, signedinteger, floating

import os

os.environ["ALLOW_RESET"] = "True"

from pdfReader import PdfRead


class ChromaClass:
    def __init__(self):
        self.doc = {}
        self.collection = None
        self.chroma_client = chromadb.PersistentClient("./Collections")
        self.read = False

    def __call__(self) -> None:
        self.embedding_func = embedding_functions.GooglePalmEmbeddingFunction(
            api_key="AIzaSyBnOXear5WrP2FWdZ14tQATdy4_2i6aM-8"
        )

    def read_file(self, file_path: str):
        pdf = PdfRead()
        pdf.read(file_path)
        pdf.split()
        self.doc = pdf.doc()
        print("File read successfully!")

    def create_collection(self):
        self.collection = self.chroma_client.get_or_create_collection(name=f"{uuid.uuid1()}",
                                                                      embedding_function=self.embedding_func)
        self.collection.add(documents=self.doc["text"], ids=self.doc["id"])
        print("Collection Created Successfully!")
        self.chroma_client.heartbeat()

    def query(self, query_text: str, n_results: int | None = 3, where: str | None = None):
        """This function is used to query the string from document, and it returns a dict containing query and
        context."""
        collection = self.chroma_client.get_collection(name=f"{uuid.uuid1()}")
        results = collection.query(query_texts=query_text, n_results=n_results, where=where)
        print("Data queried!")
        return {
            "query": query_text,
            "context": results
        }

    def delete(self):
        self.collection.delete(ids=self.doc["id"])
        self.chroma_client.reset()


c = ChromaClass()
c.__call__()
c.read_file("./Doc/deepLearning.pdf")
c.create_collection()
result = c.query("Where I can learn deep learning?", n_results=20)
print(result)
