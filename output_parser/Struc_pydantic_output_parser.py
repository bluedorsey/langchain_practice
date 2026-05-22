from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field

llm = ChatLlamaCpp(
    model_path="Phi-3.5-mini-instruct-Q4_K_M.gguf",
    n_ctx=4000,
    n_gpu_layers=0,
    verbose=False,
    temperature=0.3,
    max_tokens=1000,
)

class Person(BaseModel) :
    Name : str = Field(description="name of the person")
    age : int = Field(gt=18,description='Age of the person')
    city : str = Field(description='Name of the City the person belogns to ')

parser = PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(template="Generate the name , age and City of a fictional person {instruction_formate}",
               input_variables=[],
               partial_variables={"instruction_formate":parser.get_format_instructions()})

chain = template | llm | parser
result = chain.invoke({})

print(result)