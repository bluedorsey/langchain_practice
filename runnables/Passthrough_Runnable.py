from langchain_community.chat_models import ChatLlamaCpp 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough



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

Prompt = PromptTemplate(
template='write a joke about {topic}',
input_variables=['topic']
)

Prompt1 = PromptTemplate(
template='Explain the following Joke - {joke}',
input_variables=['joke']
)

parser= StrOutputParser()

joke_generator_chain = RunnableSequence(Prompt,llm,parser)

Parallel_chain = RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'explain':RunnableSequence(Prompt1,llm,parser)
    }
)

Final_chain = RunnableSequence(joke_generator_chain,Parallel_chain)

result = Final_chain.invoke({'topic':'AI'})
print(result)