from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=4000,
    n_gpu_layers=0,
    verbose=False,
    temperature=0.3,
    max_tokens=1000,
)
parser = JsonOutputParser()
t1 = PromptTemplate(
    template=' Give me the name , age and city of the fictional person \n {format_instruct}',
    input_variables=[],
    partial_variables={'format_instruct': parser.get_format_instructions()}
)
chain = t1 | llm | parser

result = chain.invoke({})
print(result)