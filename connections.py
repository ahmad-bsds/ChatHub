from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from chroma import ChromaClass
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

TEMPLATE = """
Answer the question based on the context below. If you can't 
answer the question, reply "I don't know please, rephrase the question.".

Context: {context}

Question: {question}
"""


class Connection:
    def __init__(self):
        self.chroma = ChromaClass()
        self.model = GoogleGenerativeAI(model="gemini-pro", google_api_key='API_KEY_HERE')
        self.parser = StrOutputParser()
        self.prompt = ChatPromptTemplate.from_template(TEMPLATE)

    def response(self, prompt: str):
        retriever = self.chroma.retriever
        setup = RunnableParallel(context=retriever, question=RunnablePassthrough())
        chain = setup | self.prompt | self.model | self.parser
        return chain.invoke(prompt)

# c = Connection()
# print(c.response("What is deep Learning?"))
