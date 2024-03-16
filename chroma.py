import chromadb
import chromadb.utils.embedding_functions as embedding_functions
from chromadb import Documents, EmbeddingFunction, Embeddings



# Chroma client:
chroma_client = chromadb.Client()

class ChromaClass(EmbeddingFunction):
    def __init__(self):
        self.embedding_func = embedding_functions.GooglePalmEmbeddingFunction(
                                 api_key="'AIzaSyBnOXear5WrP2FWdZ14tQATdy4_2i6aM-8'",
                                 model='gemini-pro'
        )
        self.client = chromadb.Client()
        self.collection = chroma_client.create_collection(name="my_collection", embedding_function=self.embedding_func)


# Add some text documents to the collection:
# collection.add(
#     documents=["This is a document", "This is another document"],
#     metadatas=[{"source": "my_source"}, {"source": "my_source"}],
#     ids=["id1", "id2"]
# )

# collection.add(
#     embeddings=[[1.2, 2.3, 4.5], [6.7, 8.2, 9.2]],
#     documents=["This is a document", "This is another document"],
#     metadatas=[{"source": "my_source"}, {"source": "my_source"}],
#     ids=["id1", "id2"]
# )

# Query collection:
# You can query the collection with a list of query texts,
# and Chroma will return the n most similar results. It's that easy!

# results = collection.query(
#     query_texts=["This is a query document"],
#     n_results=2
# )

"""
By default data stored in Chroma is ephemeral making it easy
to prototype scripts.
It's easy to make Chroma persistent so you can reuse
every collection you create and add more documents to it later.
It will load your data automatically when you start the client,
and save it automatically when you close it.
"""

