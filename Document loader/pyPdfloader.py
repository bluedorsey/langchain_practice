from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'D:\Langchain\Document loader\dl-curriculum.pdf')
docs = loader.load()
print(docs[1].metadata)