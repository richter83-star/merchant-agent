import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_description(title, keywords=None):
    prompt = f"Write a persuasive Gumroad product description for a digital product titled '{title}'."
    if keywords:
        prompt += f" Include the following themes: {', '.join(keywords)}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400
    )
    return response['choices'][0]['message']['content']
