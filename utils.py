import openai
from typing import Dict


def build_prompt(product: Dict[str, str]) -> str:
    """Builds a prompt for the language model based on product attributes."""
    name = product.get('name', '')
    features = product.get('features', '')
    tone = product.get('tone', 'professional')
    prompt = (
        f"Write a {tone} marketing description for the product '{name}'. "
        f"Highlight the following features: {features}. "
        f"Keep it under 60 words."
    )
    return prompt


def generate_copy(prompt: str, api_key: str) -> str:
    """Calls OpenAI's API to generate marketing copy. Returns the generated text."""
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}],
        max_tokens=80,
        temperature=0.8
    )
    return response['choices'][0]['message']['content'].strip()
