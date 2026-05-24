from langchain_community.document_loaders import WebBaseLoader 
 # for generally static website for dynamic or heavy js oriented code use SeleniumURLLoader
from langchain_community.chat_models import ChatLlamaCpp 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')


llm = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=8048,  # context window
    n_gpu_layers= -1,  # -1 all on gpu , all on cpu 0 
    temperature=0.5,
    max_tokens=512,
    verbose=False,
)
messgae_input = input('feedback form:')


parser2=StrOutputParser()

prompt = PromptTemplate(
template='Answer the Following question \n {question} from the following {text}',
    input_variables=['question','text']
)

url = 'https://superstarapp.in/'
loader = WebBaseLoader(
    web_path = url
)

docs = loader.load()

Chain = prompt | model | parser2

result = Chain.invoke({'question':messgae_input,'text':docs[0].page_content})
print(result)