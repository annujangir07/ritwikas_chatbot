import openai

def rephrase_answer(title, price, url, image, query, openai_key):
    openai.api_key = openai_key
    prompt = f"""You are a product assistant. Format your response in HTML to include:
- Product name: {title}
- Price: ₹{price}
- Image: {image}
- Link: {url}
Respond in 2 lines for: '{query}'
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response['choices'][0]['message']['content']


