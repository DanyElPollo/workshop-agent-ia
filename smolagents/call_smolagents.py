from smolagents import LiteLLMModel

messages = [
  {"role": "user", "content": [{"type": "text", "text": "Explain the theory of relativity in simple terms."}]},
]

model = LiteLLMModel(
    model_id="ollama_chat/gemma3:1b",  # Or try other Ollama-supported models
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    num_ctx=8192,
    temperature=0.2,
    max_tokens=1000,
    requests_per_minute=60,
)

print(model(messages))