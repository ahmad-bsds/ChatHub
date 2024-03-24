from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()


class Connection:
    def __init__(self):
        self.llm = None
        os.environ['GOOGLE_API_KEY']: str = 'AIzaSyBnOXear5WrP2FWdZ14tQATdy4_2i6aM-8'

    def response(self, prompt: str):
        self.llm = GoogleGenerativeAI(model='gemini-pro')
        return self.llm.invoke(prompt)
