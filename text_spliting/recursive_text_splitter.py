from langchain_text_splitters import RecursiveCharacterTextSplitter
from unnsessary_text import text

splitter= RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,

)
result= splitter.split_text(text)
print(result)
print(len(result))