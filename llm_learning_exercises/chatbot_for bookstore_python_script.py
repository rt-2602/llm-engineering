# imports
import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

# Load environment variables in a file called .env
# Print the key prefixes to help with any debugging

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
	

# Initialize

openai = OpenAI()
MODEL = 'gpt-4.1-mini'



system_message = "You are a helpful assistant in a book store. You should try to gently encourage \
the customer to try items that are on sale. Non-fiction books are 60% off, and most other items are 50% off. \
For example, if the customer says 'I'm looking to buy a Non-fiction books', \
you could reply something like, 'Wonderful - we have lots of Non-fiction books - including several that are part of our sales event.'\
Encourage the customer to buy Non-fiction books if they are unsure what to get."


system_message += "\nIf the customer asks for fiction books, you should respond that fiction books are not on sale today, \
but remind the customer to look at Non-fiction books!"


def chat(message, history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    relevant_system_message = system_message
    if 'magazine' in message.lower():
        relevant_system_message += " The store does not sell magazines; if you are asked for magazines, be sure to point out other items on sale."
    
    messages = [{"role": "system", "content": relevant_system_message}] + history + [{"role": "user", "content": message}]

    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response
		
		
gr.ChatInterface(fn=chat, type="messages").launch()

