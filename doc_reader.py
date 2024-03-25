# from langchain.document_loaders import PyPDFLoader
# loader = PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf")
# pages = loader.load()

prompt = "Hello"
parse = "Hi"
model = "How"
chin = prompt | parse | model

print(chin)