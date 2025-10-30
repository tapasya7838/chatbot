import streamlit as st
from rag_pipeline import RAGRetriever
from groq_client import generate_answer

st.title("Aurora Skies Airways Chatbot")
query = st.text_input("Please ask your question:")

if query:
    st.write("Query received:", query)
    retriever = RAGRetriever("airline_faq.csv")
    faqs = retriever.retrieve(query)
    st.write("Retrieved FAQs:", faqs)
    context = "\n".join([f"Q: {row['Question']}\nA: {row['Answer']}" for _, row in faqs.iterrows()])
    st.write("Context:", context)
    response = generate_answer(context, query)
    st.markdown("### Answer:")
    st.write(response)