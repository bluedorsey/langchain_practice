from langchain_community.chat_models import ChatLlamaCpp 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


llm = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=2048,  # context window
    n_gpu_layers= 0,  # -1 all on gpu , all on cpu 0 
    temperature=0.5,
    max_tokens=512,
    verbose=False,
)

Prompt = PromptTemplate(
template='write a joke about {topic}',
input_variables=['topic']
)

Prompt1 = PromptTemplate(
template='Explain the following Joke - {joke}',
input_variables=['joke']
)

parser= StrOutputParser()

chain = RunnableSequence(Prompt,llm,parser,Prompt1,llm,parser)
result = chain.invoke({'topic':'AI'})
print(result)