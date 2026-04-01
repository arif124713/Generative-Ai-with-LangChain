from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embed= GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=32)
response= embed.embed_query("My name is Arif Hussain")
print(str(response))