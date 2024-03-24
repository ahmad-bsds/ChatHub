from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
from langchain_core.runnables import  RunnableParallel, RunnablePassthrough




# Filter the empty strings:

class PdfRead():
    def __init__(self, path: str):
        # Reading document.
        self.reader = PdfReader(path)
        self.pdf_text = [p.extract_text().strip() for p in self.reader.pages]
        self.pdf_text = [text for text in self.pdf_text if text]
        # splitting text.
        self.token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=100, tokens_per_chunk=256)
        self.token_split_text = self.token_splitter.split_text('\n\n'.join(self.pdf_text))
        self.ids = [str(i) for i in range(len(self.token_split_text))]

    def doc(self) -> dict:
        """This function returns a dict which include two keys ids and text."""
        return {
            "text" : self.token_split_text,
            "id": self.ids
        }
