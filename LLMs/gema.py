from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(
model='google/gemma-2-2b-it',
task='text-generation')

model = ChatHuggingFace(llm=llm)
result = model.invoke('Hi how are You')
print(result)
