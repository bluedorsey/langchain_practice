from pydantic import BaseModel, Field
from typing import Annotated,Optional,Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#schema 
class Review(BaseModel):
    key_theme:list[str]=Field(description="Describe the key field of the reiview")
    summary: str=Field(description='A breif sumarry of the review')
    sentiment : Literal['positive', 'Negative','neutral']=Field(description='Write the Sentiment of the given review')
    pros : Optional[list[str]]=Field(description='Write the pros of the given review')
    cons : Optional[list[str]]=Field(description='Write the pros of the given review')
    name : Optional[str]=Field(description='Write the name of the reviewer')

review="""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3
processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily
lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me
away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x
actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with
bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard
pill to swallow.
Bulky and heavy-not great for one-handed use
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Bloatware still exists in One UI
Long battery life with fast charging
S-Pen support is unique and useful
Expensive compared to competitors

"""
structure_model = model.with_structured_output(Review)

for chunk in structure_model.stream(review):
    print(chunk )

print()