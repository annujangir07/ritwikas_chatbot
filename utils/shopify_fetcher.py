import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch from .env
SHOP_URL = os.getenv("SHOP_URL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Validate presence
if not SHOP_URL or not ACCESS_TOKEN:
    raise ValueError("❌ Missing SHOP_URL or ACCESS_TOKEN in your .env file!")

# Optional: print masked token
print("🔐 Loaded ACCESS_TOKEN:", ACCESS_TOKEN[:6] + "..." + ACCESS_TOKEN[-4:])

def get_all_products():
    """Fetch all products from the Shopify store."""
    try:
        url = f"https://{SHOP_URL}/admin/api/2023-07/products.json"
        headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": ACCESS_TOKEN
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get("products", [])
    except requests.exceptions.RequestException as e:
        print("❌ Failed to fetch products:", e)
        return []
