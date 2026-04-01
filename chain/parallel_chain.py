from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from unnsessary_text import text

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
model= ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",api_key=api_key)
parser= StrOutputParser()
prompt1= PromptTemplate(
    template="generate a detailed notes on {topic}", input_variables=['topic'], validate_template=True
)
prompt2= PromptTemplate(
    template="generate a quiz from {topic}", input_variables=['topic'], validate_template=True
)
prompt3= PromptTemplate(
    template="combined the provided notes and quiz into a single document \n notes-> {notes}, quiz-> {quiz}", input_variables=['notes','quiz'], validate_template=True
)
parallel_chain=RunnableParallel({
    'notes': prompt1| model | parser ,
    'quiz':prompt2|model|parser
})
merge_chain= prompt3|model|parser
chain = parallel_chain|merge_chain
result= chain.invoke({'topic':text})
print(result)
chain.get_graph().print_ascii()
