## What is smolagents?

`smolagents`  is an open-source Python library designed to make it extremely easy to build and run agents using just a few lines of code.

## Basic Installation

Install  `smolagents`  core library with:

    uv pip install smolagents
    
## Installation with Extras

`smolagents`  provides several optional dependencies (extras) that can be installed based on your needs. You can install these extras using the following syntax:

    uv pip install "smolagents[extra1,extra2]"

### Tools

These extras include various tools and integrations:

**toolkit**: Install a default set of tools for common tasks.

    uv pip install "smolagents[toolkit]"

**mcp**: Add support for the Model Context Protocol (MCP) to integrate with external tools and services.

    uv pip install "smolagents[mcp]"

### Model Integration

These extras enable integration with various AI models and frameworks:

**openai**: Add support for OpenAI API models.

    uv pip install "smolagents[openai]"
    
**transformers**: Enable Hugging Face Transformers models.
 
    uv pip install "smolagents[transformers]"
    
**vllm**: Add VLLM support for efficient model inference.

    uv pip install "smolagents[vllm]"
    
**mlx-lm**: Enable support for MLX-LM models.
   
    uv pip install "smolagents[mlx-lm]"
    
**litellm**: Add LiteLLM support for lightweight model inference.
    
    uv pip install "smolagents[litellm]"
    
**bedrock**: Enable support for AWS Bedrock models.

    uv pip install "smolagents[bedrock]"

### Multimodal Capabilities

Extras for handling different types of media and input:

**vision**: Add support for image processing and computer vision tasks.
   
    uv pip install "smolagents[vision]"
    
**audio**: Enable audio processing capabilities.

    uv pip install "smolagents[audio]"


### Complete Installation

To install all available extras, you can use:

    uv pip install "smolagents[all]"

## Verifying Installation

After installation, you can verify that  `smolagents`  is installed correctly by running:

    import smolagents
    print(smolagents.__version__)
