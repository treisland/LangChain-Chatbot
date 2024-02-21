import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
# Load environment variables
load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST")

ollama = Ollama(model="llama2")

response = ollama.invoke("Hello world")

print(response)
