from langchain_community.document_loaders import AmazonTextractPDFLoader, DirectoryLoader, PyPDFLoader

loader= AmazonTextractPDFLoader("F:/download/memora ai.pdf")
docs= loader.load()
print(docs)


### there is also an option for directory loader to load an entire directory

loader2= DirectoryLoader(
    path='hello',
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs2=loader2.lazy_load()
print(docs2)