# imports
import os
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from openai import OpenAI

# constants
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj-') and len(api_key)>10:
    print("API key looks good so far")
else:
    print("There might be a problem with your API key? Please visit the troubleshooting notebook!")
    
MODEL = 'gpt-5-nano'
openai = OpenAI()


system_message = "You are a helpful assistant. You answer questions. If you don't know the answer you say I don't know"

def chat(message, history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response
		
		
gr.ChatInterface(fn=chat, type="messages").launch()