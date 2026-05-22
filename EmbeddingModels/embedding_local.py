from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
emb=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
Document=[
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query="tell me about Virat kohli"
doc_vector = emb.embed_documents(Document)
query_vector=emb.embed_query(query)

score=cosine_similarity([query_vector],doc_vector)
print(score)