import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


system_prompt = """"You are a helpful assistant. Ensure you respond to user in a concise and clear manner. If you don't know the answer, say 'I don't know'."""
messages = [{"role": "system", "content": system_prompt}]

def continous_chat():
    while True: 
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat...")
            break

        messages.append({"role": "user", "content": user_input})
        chat_completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages
        )

        print("Assistant:", chat_completion.choices[0].message.content)


continous_chat()


