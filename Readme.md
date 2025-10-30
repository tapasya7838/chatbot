#  Aurora Skies Airways Chatbot (RAG + Groq)

This is a Retrieval-Augmented Generation (RAG) chatbot built with Streamlit that answers airline FAQs using Groq’s `llama-3.1-8b-instant` model.

##  Features

- Loads FAQs from a CSV file
- Uses TF-IDF + cosine similarity to retrieve        relevant answers
- Sends context + query to Groq API for accurate responses
- Simple Streamlit UI in one Python file

##  Requirements

- streamlit
- requests
- python-dotenv
- pandas
- sentence_transformers
- sklearn

# 1. Create .env file In the same folder as your chatbot script

GROQ_API_KEY=your_actual_groq_api_key

# 2. Run the chatbot

streamlit run chatbot.py

