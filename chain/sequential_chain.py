from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

prompt1= PromptTemplate(
    template="generate a detailed report on {topic}", input_variables=['topic'], validate_template=True
)
model= ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",api_key=api_key)
parser= StrOutputParser()
prompt2= PromptTemplate(
    template="summarize the text \n {text}", input_variables=['text'], validate_template=True
)

chain= prompt1 | model | parser | prompt2 | model| parser
result= chain.invoke({'topic': "Computer Vision"})
print(result)
chain.get_graph().print_ascii()