from typing import Dict, List, Any, Sequence, Mapping

import chromadb
import chromadb.utils.embedding_functions as embedding_functions
import uuid
from chromadb import Documents, EmbeddingFunction, Embeddings, QueryResult
from numpy import ndarray, dtype, unsignedinteger, signedinteger, floating

from pdfReader import PdfRead


class ChromaClass:
    def __init__(self, file_path: str):
        self.chroma_client = chromadb.Client()
        self.file = file_path
        self.pdf = PdfRead(self.file)
        self.doc = self.pdf.doc()

    def __call__(self) -> None:
        self.embedding_func = embedding_functions.GooglePalmEmbeddingFunction(
            api_key="AIzaSyBnOXear5WrP2FWdZ14tQATdy4_2i6aM-8"
        )
        self.collection = self.chroma_client.create_collection(name=f"{uuid.uuid1()}",
                                                               embedding_function=self.embedding_func)
        self.collection.add(documents=self.doc["text"], ids=self.doc["id"])

    def query(self, query_text: str, n_results: int | None = 1, where: str | None = None):
        """This function is used to query the string from document, and it returns a dict containing query and
        context."""
        results = self.collection.query(query_texts=query_text, n_results=n_results, where=where)
        return {
            "query": query_text,
            "context": results
        }


c = ChromaClass("./Doc/deepLearning.pdf")
c.__call__()
result = c.query("Where I can learn deep learning?")
print(result)
