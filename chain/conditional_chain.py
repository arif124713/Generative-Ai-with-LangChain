
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from unnsessary_text import text

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
model= ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",api_key=api_key)

parser= StrOutputParser()
prompt1= PromptTemplate(
    template="classify the sentiment of the following text positive or negative. if positive reply only positive  or if negative reply negative one word just. nothing else. \n {feedback} ",
    input_variables=['feedback'], validate_template= True
)
prompt2= PromptTemplate(
    template="write a short and simple response in 2 line for this positive feedback \n {feedback}",
    input_variables=['feedback'], validate_template=True
)
prompt3= PromptTemplate(
    template="write a short and simple response for this negative feedback \n {feedback}",
    input_variables=['feedback'], validate_template=True
)

classifier_chain= prompt1|model|parser

branch_chain= RunnableBranch(
    (lambda x:x=='positive', prompt2|model|parser),
    (lambda x:x=='negative', prompt3|model|parser),
    RunnableLambda(lambda x: "couldn't find sentiment")
)

chain= classifier_chain|branch_chain

result= chain.invoke({'feedback':"this is a very good Phone"})
print(result)
chain.get_graph().print_ascii()