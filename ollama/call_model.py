from ollama import Client

client = Client()

messages = [
  {
    'role': 'user',
    'content': 'Explain the theory of relativity in simple terms.',
  },
]

for part in client.chat('gpt-oss:120b-cloud', messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True)
