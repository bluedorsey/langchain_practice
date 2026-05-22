from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

#1st prompt
temp_1 = PromptTemplate(
    template='Write the detailed about the {topic}',
    input_variables=['topic']
)
#2nd prompt 
temp_2= PromptTemplate(
    template='Write a five line summary of the following text /n {text}',
    input_variables=['text']
)

prompt_1 = temp_1.invoke({'topic':'Black hole'})
result = model.invoke(prompt_1)

prompt_2 = temp_2.invoke({'text':result.content})
result_final=model.invoke(prompt_2)

parser = StrOutputParser() #content extractor 
chain = temp_1 | model | parser | temp_2 | model | parser

result1 = chain.invoke({'topic':'Black hole'})
print(result1)