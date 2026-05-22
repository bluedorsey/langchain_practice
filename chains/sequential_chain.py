from langchain_community.chat_models import ChatLlamaCpp
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=4096,  # context window
    n_gpu_layers= 0,  # -1 all on gpu , all on cpu 0 
    temperature=0.5,
    max_tokens=512,
    verbose=False,
)

llm2 = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

temp = PromptTemplate(
    template='Generate 5 Interesting fact about {topic}',
    input_variables=['topic']
)

temp1 = PromptTemplate(
    template='Generate the breif summary about 3 lines of the given text \n {text}',
    input_variables=['text']
)
temp2 = PromptTemplate(
    template='add the autobiography as a fictional Charector name Mahinda she is female \n here is the template \n {sum}',
    input_variables=['sum']
)

parser = StrOutputParser()

chain = temp | llm | parser | temp1 | llm2 | parser | temp2 | llm | parser

result = chain.invoke({'topic':'cricket'})
print(result)