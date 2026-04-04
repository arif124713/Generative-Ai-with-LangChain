from langchain_community.document_loaders import TextLoader
loader= TextLoader("F:/download/langchain/texxxt.txt")
docs= loader.load()
print(docs)