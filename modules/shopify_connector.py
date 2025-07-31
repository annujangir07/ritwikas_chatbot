import os
import requests

def validate_shopify_credentials(shop_url, access_token):
    if not shop_url or not access_token:
        return False, "Missing SHOP_URL or ACCESS_TOKEN"

    test_url = f"https://{shop_url}/admin/api/2023-07/shop.json"
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(test_url, headers=headers)
        if response.status_code == 200:
            return True, "Shopify credentials are valid"
        else:
            return False, f"Invalid credentials. Status code: {response.status_code}"
    except Exception as e:
        return False, f"Error validating credentials: {e}"












