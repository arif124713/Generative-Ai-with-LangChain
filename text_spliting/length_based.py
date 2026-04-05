from langchain_text_splitters import CharacterTextSplitter
from unnsessary_text import text

splitter= CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
result= splitter.split_text(text)
print(result)
# print(len(result))