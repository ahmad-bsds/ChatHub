from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


class DocToken:
    def __init__(self):
        loader = DirectoryLoader("./Doc/", glob="./*.pdf", loader_cls=PyPDFLoader)
        self.document = loader.load()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        self.texts = self.text_splitter.split_documents(self.document)

    def tokens(self):
        return self.texts

#
# c = DocToken()
# print(c.tokens())

