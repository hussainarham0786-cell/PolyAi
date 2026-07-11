import streamlit as st
from groq import Groq
from tavily import TavilyClient

# Initialize clients using secrets
groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
tavily = TavilyClient(api_key=st.secrets["TAVILY_API_KEY"])

st.title("My AI Assistant")

# Maintain chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Search web using Tavily
    search_result = tavily.search(query=prompt)
    context = "\n".join([r['content'] for r in search_result['results']])

    # Generate response using Groq
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": f"Context: {context}"},
            {"role": "user", "content": prompt}
        ]
    )
    
    ai_response = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    
    with st.chat_message("assistant"):
        st.markdown(ai_response)
