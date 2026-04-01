from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm=GoogleGenerativeAI(model="gemini-2.5-flash-lite",api_key=api_key)
response= llm.invoke("what is the area of Bangladeshd")
print(response)