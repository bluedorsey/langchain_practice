from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
models=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result=models.invoke("what is the capital of india")
print(result.content)