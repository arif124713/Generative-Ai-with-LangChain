from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

prompt= PromptTemplate(
    template='generate 5 intreseting fact about {topic}',input_variables=['topic'],validate_template=True
)
model= ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",api_key=api_key)
parser=StrOutputParser()

chain= prompt | model|parser
result=chain.invoke({'topic':'Black Hole'})
print(result)
chain.get_graph().print_ascii()