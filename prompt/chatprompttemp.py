from langchain_core.prompts import ChatPromptTemplate

chat_temp= ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','exaplain in simple term , what is {topic}')
])

prompt = chat_temp.invoke({'domain':'cricket','topic':'batting rules'})
print(prompt)