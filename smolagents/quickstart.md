## Installation

Install smolagents with pip:

    pip install smolagents[toolkit]  # Includes default tools like web search

### First Agent

Here’s a minimal example to create and run an agent:

    from smolagents import CodeAgent, InferenceClientModel
    
    # Initialize a model (using Hugging Face Inference API)
    model = InferenceClientModel()  # Uses a default model
    
    # Create an agent with no tools
    agent = CodeAgent(tools=[], model=model)
    
    # Run the agent with a task
    result = agent.run("Calculate the sum of numbers from 1 to 10")
    print(result)


### Adding Tools

Let’s make our agent more capable by adding some tools:

    from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool
    
    model = InferenceClientModel()
    agent = CodeAgent(
        tools=[DuckDuckGoSearchTool()],
        model=model,
    )
    
    # Now the agent can search the web!
    result = agent.run("What is the current weather in Paris?")
    print(result)


### Using Different Models

You can use various models with your agent:


    # Using a specific model from Hugging Face
    model = InferenceClientModel(model_id="meta-llama/Llama-2-70b-chat-hf")
    
    # Using OpenAI/Anthropic (requires smolagents[litellm])
    from smolagents import LiteLLMModel
    model = LiteLLMModel(model_id="gpt-4")
    
    # Using local models (requires smolagents[transformers])
    from smolagents import TransformersModel
    model = TransformersModel(model_id="meta-llama/Llama-2-7b-chat-hf")