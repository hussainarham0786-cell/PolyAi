import streamlit as st
from google import genai

st.title("PolyAI Chatbot")

# Initialize the AI client
if "client" not in st.session_state:
    try:
        st.session_state.client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
        st.session_state.chat = st.session_state.client.chats.create(model="gemini-1.5-flash-002")
    except Exception as e:
        st.error(f"Setup Error: {e}")
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask PolyAI something..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"API Error: {e}") # This will show the real problem
