# imports

import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display

requests.get("http://localhost:11434/").content

# If not running, run ollama serve at a command line

!ollama pull -deepseekr1:1.5b

!ollama pull gemma3
    

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
	
	
# Connect to OpenAI client library
# A thin wrapper around calls to HTTP endpoints

openai = OpenAI()



gpt_model = "gpt-4.1-mini"
gemma_model = "gemma3"
deepseek_model = "deepseekr1:1.5b"


system_prompt = """
You are Alex, a chatbot who is very argumentative; you disagree with anything in the conversation and you challenge everything, in a snarky way.
You are in a conversation with Blake and Charlie.
"""

conversation = ["Hi"]


def get_user_prompt(conversation):
    return f"""
You are Alex, in conversation with Blake and Charlie.
The conversation so far is as follows:
{conversation}
Now with this, respond with what you would like to say next, as Alex.
"""

def call_gpt():
    user_prompt = get_user_prompt(conversation)
    messages = [{"role": "system", "content": system_prompt}]
    messages.append({"role": "user", "content": user_prompt})
    response = openai.chat.completions.create(model=gpt_model, messages=messages)
    reply = response.choices[0].message.content
    conversation.append(f"Alex: {reply}")
    return reply

   

def call_gemma():
    user_prompt = get_user_prompt(conversation)
    messages = [{"role": "system", "content": system_prompt}]
    messages.append({"role": "user", "content": user_prompt})
    response = ollama.chat.completions.create(model=gemma_model, messages=messages)
    reply = response.choices[0].message.content
    conversation.append(f"Blake: {reply}")
    return reply


def call_deepseek():
    user_prompt = get_user_prompt(conversation)
    messages = [{"role": "system", "content": system_prompt}]
    messages.append({"role": "user", "content": user_prompt})
    response = ollama.chat.completions.create(model="deepseek-r1:1.5b", 	messages=messages)
    reply = response.choices[0].message.content
    conversation.append(f"Charlie: {reply}")
    return reply
	
 

def start_conversation():
    for i in range(5):
        gpt_next = call_gpt()
        display(Markdown(f"### GPT:\n{gpt_next}\n"))

        gemma_next = call_gemma()
        display(Markdown(f"### Gemma:\n{gemma_next}\n"))

        deepseek_next = call_deepseek()
        display(Markdown(f"### Deepseek:\n{deepseek_next}\n"))
		

start_conversation()
        
		
		
