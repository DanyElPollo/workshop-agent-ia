from ollama import Client
from ai_custom_utils.helper import get_llama_api_key

api_key = get_llama_api_key()

client = Client(
    host="https://ollama.com",
    headers={'Authorization': api_key}
)

messages = [
  {
    'role': 'user',
    'content': 'Explain the theory of relativity in simple terms.',
  },
]

for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True)