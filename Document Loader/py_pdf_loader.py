from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader("F:/download/memora ai.pdf")
docs= loader.load()
print(docs)
