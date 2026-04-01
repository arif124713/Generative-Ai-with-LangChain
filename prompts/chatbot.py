from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.prompts import PromptTemplate, load_prompt
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
model= ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",api_key=api_key)

messages= [
    SystemMessage(content="you are a financial advisor"),

]

while True:
    user_input= input("You: ")
    messages.append(HumanMessage(content=user_input))
    if user_input== 'exit':
        break
    result=model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print(result.content)
