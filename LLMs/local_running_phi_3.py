from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=4096,  # context window
    n_gpu_layers= 0,  # -1 all on gpu , all on cpu 0 
    temperature=0.5,
    max_tokens=512,
    verbose=False,
)



message =[
    SystemMessage(content="You are personal assistance that help in teaching gen-ai concept in very esy words."),
    HumanMessage(content="Explain RAG in 3 sentences.")
]
for chunk in llm.stream(message):
    print(chunk.content , end ='', flush=True)

print()