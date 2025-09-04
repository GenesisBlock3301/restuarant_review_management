import os
import pandas as pd
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document


df = pd.read_csv("./realistic_restaurant_reviews.csv")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = './chrome_langchain_db'
add_documents = not os.path.exists(db_location)

if add_documents:
    document = []
    ids = []
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], 'date': row["Date"]},
        )