from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
from langchain_core.runnables import RunnableParallel, RunnablePassthrough



# Filter the empty strings:

class PdfRead:
    def __init__(self):
        self.pdf_text = []
        self.filename = ""
        self.token_split_text = ""
        self.ids = []

    # Reading document.
    def read(self, path: str):
        reader = PdfReader(path)
        self.pdf_text = [p.extract_text().strip() for p in reader.pages]
        self.pdf_text = [text for text in self.pdf_text if text]

    def split(self):
        # splitting text.
        token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=100, tokens_per_chunk=256)
        self.token_split_text = token_splitter.split_text('\n\n'.join(self.pdf_text))
        self.ids = [str(i) for i in range(len(self.token_split_text))]

    def doc(self) -> dict:
        """This function returns a dict which include two keys ids and text."""
        return {
            "text": self.token_split_text,
            "id": self.ids
        }
