from IPython.display import Markdown, display
from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')

# Step 1: Create your prompts
system_prompt = "You are a helpful assistant. You are given a book title and you need to summarize it in a few sentences. Be snarky and humorous."
user_prompt = """
    You need to summarize the book in a few sentences. In your response, include the title of the book, the author, and the summary. 
    Book title: 
"""

# Step 2: Make the messages list
def messages_for(book_title):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt + book_title}
    ]

# Step 3: Call OpenAI
def summarize(book_title):
    
    response = ollama.chat.completions.create(
        model = "llama3.2:1b",
        messages = messages_for(book_title)
    )
    return response.choices[0].message.content


# Step 4: print the result
def display_summary(book_title):
    summary = summarize(book_title)
    display(Markdown(summary))

display_summary("The Great Gatsby")