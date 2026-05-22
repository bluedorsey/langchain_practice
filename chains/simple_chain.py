from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=4096,  # context window
    n_gpu_layers= 0,  # -1 all on gpu , all on cpu 0 
    temperature=0.5,
    max_tokens=512,
    verbose=False,
)

temp = PromptTemplate(
    template='Generate 5 Interesting fact about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = temp | llm | parser

result = chain.invoke({'topic':'cricket'})
print(result)