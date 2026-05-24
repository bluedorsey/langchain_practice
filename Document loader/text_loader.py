from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatLlamaCpp

llm = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=4096,  # context window
    n_gpu_layers= 0,  # -1 all on gpu , all on cpu 0 
    temperature=0.5,
    max_tokens=512,
    verbose=False,
)

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader(r'D:\Langchain\Document loader\cricket.txt', encoding='utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | llm | parser

print(chain.invoke({'poem':docs[0].page_content}))

