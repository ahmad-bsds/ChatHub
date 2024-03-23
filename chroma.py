from typing import Dict, List, Any, Sequence, Mapping

import chromadb
import chromadb.utils.embedding_functions as embedding_functions
from chromadb import Documents, EmbeddingFunction, Embeddings, QueryResult
from numpy import ndarray, dtype, unsignedinteger, signedinteger, floating

# Chroma client:
chroma_client = chromadb.Client()


class ChromaClass():
    def __init__(self):
        self.client = chromadb.Client()

    def __call__(self, doc: Documents, ids: list, name: str | None = "my-collections") -> None:
        self.embedding_func = embedding_functions.GooglePalmEmbeddingFunction(
            api_key="AIzaSyBnOXear5WrP2FWdZ14tQATdy4_2i6aM-8"
        )
        self.collection = chroma_client.create_collection(name=name, embedding_function=self.embedding_func)
        self.collection.add(documents=doc, ids=ids)

    def query(self, query_text: str, n_results: int | None = 1, where: str | None = None) -> QueryResult:
        results = self.collection.query(query_texts=query_text, n_results=n_results, where=where)
        return results


embed = ChromaClass()
embed.__call__(doc=["""These SQL techniques are essential from \
a data warehousing perspective, such as trend analysis, temporal analytics, managing \
sequences, unique counts, and managing processes as transactions."""], ids=["a"])
print(embed.query(query_text="SQL"))

# To get embeddings: embed.query(query_text="For what SQL techniques are  important?")["embeddings"]
