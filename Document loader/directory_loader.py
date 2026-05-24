from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
loader = DirectoryLoader(
    path=r'D:\Langchain\Document loader\books',
    glob='*.pdf' ,         #pattern   
    loader_cls=PyPDFLoader
#      which type of your document is their 
#     (**/*.txt)  - all .txt format data
#     (*.pdf)     - all .pdf File
#     data/*.csv  - all csv file formated 
#     **/*        - very file in directory 
#       **          - recursive go with subfolder 
)

docs = list(loader.lazy_load())
#print(docs[325].page_content)
#print(docs[325].metadata)

for doc in docs:
    print(doc.metadata)

# load 
# Put every doc in ram 

#lazy load
#put only required doc page in ram 