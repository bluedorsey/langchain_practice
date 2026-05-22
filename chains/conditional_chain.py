from langchain_community.chat_models import ChatLlamaCpp 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda , RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

llm = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=2048,  # context window
    n_gpu_layers= 0,  # -1 all on gpu , all on cpu 0 
    temperature=0.5,
    max_tokens=512,
    verbose=False,
)
messgae_input = input('feedback form:')

class Feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description='Give the sentiment of the feedback')

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
template='Classify the sentiment of the following feedback text into positive or negative \n {feedback},{formate_instruction}',
    input_variables=['feedback'],
    partial_variables={'formate_instruction': parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template='Write an Appropiate respose to this positive feedback \n {feedback} ',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an Appropiate respose to this negative feedback \n {feedback} ',
    input_variables=['feedback']
)

parser = StrOutputParser()

classfier_chain = prompt1 | llm | parser2
chain_pos= prompt2 | llm |parser
chain_neg= prompt3 | llm | parser

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', chain_pos),
    (lambda x:x.sentiment == 'negative', chain_neg),
    RunnableLambda(lambda x:'couldnt find sentiment')
)

final = classfier_chain | branch_chain

for chunk in final.stream({'feedback': messgae_input}):
    print(chunk,end='',flush=True)



