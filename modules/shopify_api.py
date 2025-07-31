import requests

def get_all_products(store_url, access_token):
    try:
        headers = {
            "X-Shopify-Access-Token": access_token,
            "Content-Type": "application/json"
        }
        url = f"https://{store_url}/admin/api/2023-01/products.json?limit=250"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print("❌ Shopify API error:", response.text)
            return []

        products_data = response.json().get("products", [])
        formatted_products = []

        for product in products_data:
            title = product.get("title", "")
            image = product.get("image", {}).get("src", "")
            price = "N/A"
            variants = product.get("variants", [])
            if variants:
                price = variants[0].get("price", "N/A")
            link = f"https://{store_url}/products/{product.get('handle')}"
            formatted_products.append({
                "title": title,
                "price": price,
                "image": image,
                "link": link
            })

        return formatted_products

    except Exception as e:
        print(f"❌ Error fetching products: {e}")
        return []







