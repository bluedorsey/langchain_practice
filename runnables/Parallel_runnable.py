from langchain_community.chat_models import ChatLlamaCpp 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence


llm = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=2048,  # context window
    n_gpu_layers= 0,  # -1 all on gpu , all on cpu 0 
    temperature=0.5,
    max_tokens=512,
    verbose=False,
)
llm1 = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=2048,  # context window
    n_gpu_layers= 0,  # -1 all on gpu , all on cpu 0 
    temperature=0.5,
    max_tokens=512,
    verbose=False,
)




Prompt1 = PromptTemplate(
template='Wite a post regarding the topic in linkedin {topic} ',
input_variables=['topic']
)
Prompt2 = PromptTemplate(
template='Wite a post regarding the topic in Twitter {topic} ',
input_variables=['topic']
)

parser= StrOutputParser()

chain = RunnableParallel({
    'tweet': RunnableSequence(Prompt2,llm,parser),
    'linkedin': RunnableSequence(Prompt1,llm1,parser)
})
result = chain.invoke({'topic':'AI'})
print(result)