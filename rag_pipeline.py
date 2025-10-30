import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class RAGRetriever:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = self.model.encode(self.df['Question'].tolist(), convert_to_numpy=True)

    def retrieve(self, query, top_k=3):
        query_vec = self.model.encode([query], convert_to_numpy=True)
        similarities = cosine_similarity(query_vec, self.embeddings)[0]
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        return self.df.iloc[top_indices]