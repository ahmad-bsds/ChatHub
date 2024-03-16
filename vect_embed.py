import chromadb
import chromadb.utils.embedding_functions as embedding_functions
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitterI

# TODO: Split documents.

# TODO: Embeddings.
palm_embedding = embedding_functions.GooglePalmEmbeddingFunction(
    api_key='AIzaSyBnOXear5WrP2FWdZ14tQATdy4_2i6aM-8', model='gemini-pro')

# TODO: Store Embeddings into chroma db.
chroma_client = chromadb.Client()
# Creating collections.
collection = chroma_client.create_collection(name="text_collection")

