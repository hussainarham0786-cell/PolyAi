from google import genai
from google.colab import userdata

# 1. SETUP
client = genai.Client(api_key=userdata.get('GOOGLE_API_KEY'))
model_id = "gemini-3.1-flash-lite"
chat = client.chats.create(model=model_id)

print(f"✅ Successfully connected to {model_id}!")
print("--- Type 'quit' to exit the chat ---")

# 2. PERSISTENT CHAT LOOP
while True:
    try:
        user_input = input("\nYou: ")
        
        # Check if user wants to stop
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
            
        # Send message and get response
        response = chat.send_message(user_input)
        print(f"AI: {response.text}")
        
    except Exception as e:
        print(f"\n❌ Loop Error: {e}")
        break
