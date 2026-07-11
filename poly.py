import streamlit as st
from google import genai
import os

# Set page configuration
st.set_page_config(page_title="PolyAI Chatbot", page_icon="🤖")

st.title("PolyAI Chatbot")

# 1. Initialize the AI client securely
if "client" not in st.session_state:
    try:
        # Pulls the key from your Streamlit Secrets settings
        api_key = st.secrets["GOOGLE_API_KEY"]
        st.session_state.client = genai.Client(api_key=api_key)
        
        # Initialize chat session
        # If this model name gives an error, use the one you saw in your list earlier
        st.session_state.chat = st.session_state.client.chats.create(model="gemini-1.5-flash-latest")

    except Exception as e:
        st.error(f"Configuration Error: {e}")
        st.stop()

# 2. Keep track of chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle user input
if prompt := st.chat_input("Ask PolyAI something..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get AI response
    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"API Error: {e}")
