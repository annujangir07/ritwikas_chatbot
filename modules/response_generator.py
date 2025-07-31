import os
from modules.openai_formatter import rephrase_answer

def generate_response(product, query, openai_key=None):
    title = product.get("title", "No title")
    price = product.get("variants", [{}])[0].get("price", "N/A")
    image = product.get("image", {}).get("src", "")
    url = f"https://{os.getenv('SHOP_URL')}/products/{product.get('handle', '')}"

    if openai_key:
        try:
            return rephrase_answer(title, price, url, image, query, openai_key)
        except:
            pass

    return f"""
    <b>🖼️ {title}</b><br>
    💲 Price: ₹{price}<br>
    🔗 <a href="{url}" target="_blank">View Product</a><br>
    <img src="{image}" alt="{title}" width="250">
    """

