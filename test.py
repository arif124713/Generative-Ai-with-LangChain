# from google import genai
# from dotenv import load_dotenv
#
# load_dotenv()
# client = genai.Client()
# for m in client.models.list():
#     print(m.name)
#
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
# from langchain_core.prompts import PromptTemplate, load_prompt
# import os
# from dotenv import load_dotenv
# import streamlit as st
#
# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")
# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", api_key=api_key)
#
# messages = [
#     SystemMessage(content="you are a financial advisor"),
#
# ]
# st.header("Ai chatbot")
# i=0
# j=110
# while True:
#     user_input = st.text_input("Enter your prompt", key=i)
#     if st.button("send", key=j):
#         if user_input.lower() == "exit":
#             st.stop()  # stops execution cleanly
#         else:
#             messages.append(HumanMessage(content=user_input))
#             result = model.invoke(messages)
#             messages.append(AIMessage(content=result.content))
#             st.write(result.content)
#
#     i+=1
#     j+=1

# import pydantic
# print(pydantic.__version__)

from unnsessary_text import text
print(text)
