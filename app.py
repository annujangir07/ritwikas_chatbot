import streamlit as st
from modules.query_handler import handle_query

st.set_page_config(page_title="🛍️ Ritwika Chatbot", layout="centered")

# 🛍️ Title
st.title("🛍️ Ask Your Product Questions")

# ✅ Text input for product question
user_query = st.text_input("Ask something about your products:")

if user_query:
    results = handle_query(user_query)

    if results:
        for product in results:
            with st.container():
                st.image(product['image'], width=250)
                st.markdown(f"**🖼️ {product['title']}**")
                st.markdown(f"**💲 Price:** {product['price']}")
                st.markdown(f"[🔗 View Product]({product['link']})")
                st.markdown("---")
    else:
        st.warning("No matching products found. Please try a different query.")
















