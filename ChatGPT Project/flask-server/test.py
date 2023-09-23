import os
import openai

# Set your OpenAI API key here
openai.api_key = "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"


completion = openai.Completion.create(
    engine="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" for the turbo model
    prompt="You are a helpful assistant.\nUser: Hello!",
    max_tokens=5
)

print(completion.choices[0].text.strip())
