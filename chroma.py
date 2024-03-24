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
    def __init__(self, file_path: str):
        self.chroma_client = chromadb.PersistentClient(path="./Collections/")
        # self.file = file_path
        pdf = PdfRead()
        pdf.read(file_path)
        pdf.split()
        self.doc = pdf.doc()
        print("File read successfully!")

    def __call__(self) -> None:
        self.embedding_func = embedding_functions.GooglePalmEmbeddingFunction(
            api_key="AIzaSyBnOXear5WrP2FWdZ14tQATdy4_2i6aM-8"
        )
        self.collection = self.chroma_client.create_collection(name=f"{uuid.uuid1()}",
                                                               embedding_function=self.embedding_func)
        self.collection.add(documents=self.doc["text"], ids=self.doc["id"])
        print("Collection Created Successfully!")

    def query(self, query_text: str, n_results: int | None = 1, where: str | None = None):
        """This function is used to query the string from document, and it returns a dict containing query and
        context."""
        results = self.collection.query(query_texts=query_text, n_results=n_results, where=where)
        print("Data queried!")
        return {
            "query": query_text,
            "context": results
        }

    def __delete__(self):
        self.collection.delete(ids=self.doc["id"])
        self.chroma_client.reset()


# c = ChromaClass("./Doc/deepLearning.pdf")
# c.__call__()
# result = c.query("Where I can learn deep learning?", n_results=20)
# print(result)
# c.__delete__()
