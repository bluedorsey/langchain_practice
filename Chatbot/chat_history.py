from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

#chat template
chat_temp=ChatPromptTemplate([
    ('system','You are a helpfull ai assistant for an customer service '),
    MessagesPlaceholder(variable_name = 'chat_history'),
    ('human','{query}')
    ])
#load historty
chat_history=[]
with open('Chatbot/chat_history.txt') as f:
    chat_history.extend(f.readlines())

#create prompt
prompt = chat_temp.invoke({
    'chat_history':chat_history,
    'query':'where is my refund'}
)
print(prompt)