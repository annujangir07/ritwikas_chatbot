import streamlit as st
from bot_logic import ask_bot

# Streamlit Page Config
st.set_page_config(page_title="Ritwika's Smart Chatbot", page_icon="✨")

# Title
st.title("✨ Welcome to Ritwika's Smart Chatbot!")
st.caption("Ask about products, stock, delivery, offers, sizes, and more.")

# Input: User Name
name = st.text_input("Enter your name to begin:")

if name:
    st.success(f"Hi {name}! How can I assist you today? 😊")

    # Input: User Question
    user_question = st.text_input("Type your question here:")

    if user_question:
        ask_bot(user_question, st)

# Footer
st.caption("Ritwika's")
