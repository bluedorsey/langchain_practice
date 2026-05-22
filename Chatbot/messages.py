from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

messages=[
    SystemMessage(content='You are a help full assistant'),
    HumanMessage(content='tell me about langchain')
]

result = model.invoke(messages)
messages.append(AIMessage(result.content))
print(messages)