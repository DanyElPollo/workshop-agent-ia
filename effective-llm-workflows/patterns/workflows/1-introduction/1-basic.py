from openai import OpenAI
from ai_custom_utils.helper import get_openai_api_key

client = OpenAI(api_key=get_openai_api_key())


completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        },
    ],
)

response = completion.choices[0].message.content
print(response)