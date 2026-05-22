from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=4000,
    n_gpu_layers=0,
    verbose=False,
    temperature=0.3,
    max_tokens=1000,
)

t1 = PromptTemplate(
    template="Write 7 lines about {topic}",
    input_variables=['topic']
)

t2 = PromptTemplate(
    template="Summarize the given text in 2 lines:\n{text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = (
    t1 | llm | parser | (lambda output_string: {"text": output_string}) | t2 | llm | parser
)

for chunk in chain.stream({'topic': 'rain'}):
    print(chunk, flush=True, end='')

print()