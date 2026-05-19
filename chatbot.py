from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended")
        break

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"system", "content":"You are a helpful AI assistant."},
        {"role":"user", "content": user_input}]
    )

    ai_reply = response.choices[0].message.content

    print("AI: ", ai_reply)
