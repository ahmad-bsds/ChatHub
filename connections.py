# from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai


class Connection:
    def __init__(self):
        genai.configure(api_key='AIzaSyBnOXear5WrP2FWdZ14tQATdy4_2i6aM-8')
        self.model = genai.GenerativeModel('gemini-pro')

    def response(self, prompt: str):
        return self.model.generate_content(prompt).text
