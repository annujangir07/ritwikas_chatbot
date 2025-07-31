from modules.product_fetcher import fetch_products
from modules.fuzzy_matcher import get_best_matches

def handle_query(query):
    all_products = fetch_products()
    matched_titles = get_best_matches(query, [p["title"] for p in all_products], limit=5)

    top_matches = []
    for match in matched_titles:
        for product in all_products:
            if match.lower() == product["title"].lower():
                top_matches.append(product)
                break
    return top_matches









