from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda,RunnableSequence, RunnablePassthrough

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
model= ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",api_key=api_key)

parser= StrOutputParser()
prompt1= PromptTemplate(
    template="write a joke about {topic}",
    input_variables=['topic'], validate_template= True
)
prompt2= PromptTemplate(
    template="explain the  \n {text}",
    input_variables=['text'], validate_template=True
)



joke_generation_chain= RunnableSequence(prompt1,model,parser)
parallel_chain= RunnableParallel({
    'joke':RunnablePassthrough(),
    'explain': RunnableSequence(prompt2,model,parser)
}
)
chain= RunnableSequence(joke_generation_chain,parallel_chain)
result=chain.invoke({'topic': 'Ai'})
print(result)
