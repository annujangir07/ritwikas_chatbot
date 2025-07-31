import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_products():
    SHOP_URL = os.getenv("SHOP_URL")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

    if not SHOP_URL or not ACCESS_TOKEN:
        print("❌ SHOP_URL or ACCESS_TOKEN is missing!")
        return []

    url = f"https://{SHOP_URL}/admin/api/2023-01/products.json"
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": ACCESS_TOKEN,
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("❌ Shopify API error:", response.text)
        return []

    products = response.json().get("products", [])
    product_data = []
    for product in products:
        image = product["image"]["src"] if product.get("image") else ""
        price = product["variants"][0]["price"] if product.get("variants") else "N/A"
        product_data.append({
            "title": product["title"],
            "price": f"₹{price}",
            "image": image,
            "link": f"https://{SHOP_URL}/products/{product['handle']}"
        })
    return product_data


