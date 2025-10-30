import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_answer(context, query):
    prompt = f"""You are a helpful airline assistant. Use the following FAQ context to answer the question accurately.

FAQ Context:
{context}

Question:
{query}

Answer:"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
        json={
            "model": "llama-3.1-8b-instant",  
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        }
    )

    data = response.json()
    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    elif "error" in data:
        return f"Groq API Error: {data['error']['message']}"
    else:
        return "Unexpected response format from Groq API."