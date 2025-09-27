# Ollama

## Cloud Models

**Ollama currently supports the following cloud models**:

-   `gpt-oss:20b-cloud`
-   `gpt-oss:120b-cloud`
-   `deepseek-v3.1:671b-cloud`
-   `qwen3-coder:480b-cloud`



## Running Models Locally with Ollama (In case you run into Credit limits)

1.  **Install Ollama**
    
    Follow the official Instructions  [here.](https://ollama.com/download)
    
2.  **Pull a model Locally**
    
    Copied
    
    ollama pull qwen2:7b
    
    Here, we pull the  [qwen2:7b model](https://ollama.com/library/qwen2:7b). Check out  [the ollama website](https://ollama.com/search)  for more models.
    
3.  **Start Ollama in the background (In one terminal)**
    
    Copied
    
    ollama serve
    
    If you run into the error “listen tcp 127.0.0.1:11434: bind: address already in use”, you can use command  `sudo lsof -i :11434`  to identify the process ID (PID) that is currently using this port. If the process is  `ollama`, it is likely that the installation script above has started ollama service, so you can skip this command to start Ollama.
    
4.  **Use  `LiteLLMModel`  Instead of  `InferenceClientModel`**
    
    To use  `LiteLLMModel`  module in  `smolagents`, you may run  `pip`  command to install the module.
    

Copied

    pip install 'smolagents[litellm]'

Copied

    from smolagents import LiteLLMModel

    model = LiteLLMModel(
        model_id="ollama_chat/qwen2:7b",  # Or try other Ollama-supported models
        api_base="http://127.0.0.1:11434",  # Default Ollama local server
        num_ctx=8192,
    )

5.  **Why this works?**

-   Ollama serves models locally using an OpenAI-compatible API at  `http://localhost:11434`.
-   `LiteLLMModel`  is built to communicate with any model that supports the OpenAI chat/completion API format.
-   This means you can simply swap out  `InferenceClientModel`  for  `LiteLLMModel`  no other code changes required. It’s a seamless, plug-and-play solution.