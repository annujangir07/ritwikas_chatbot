# bot_logic.py

def get_faq():
    return {
        "delivery": "📦 Delivery within India: 5-7 working days | International: 10-15 working days.",
        "offers": "🎉 Get **15% OFF** on orders above ₹2000! Use code **RIT15** at checkout.",
        "return": "🔄 7-day easy return policy. No questions asked.",
        "payment": "💳 Accepted: UPI, Credit/Debit Cards, and Cash on Delivery."
    }


def get_products():
    return {
        "Star Maps": {"price": "₹999 - ₹2999", "stock": "Available", "sizes": ["A4", "A3", "A2"], "image": "star_map.png"},
        "Acrylic Frames": {"price": "₹799 - ₹1599", "stock": "Available", "sizes": ["A5", "A4", "A3"], "image": "acrylic_frames.png"},
        "Wall Art": {"price": "₹1499 - ₹3999", "stock": "Out of stock", "sizes": ["A3", "A2", "24x36 inch"], "image": "wall_art.png"},
        "Decor Items": {"price": "₹599 - ₹2499", "stock": "Available", "sizes": ["Small", "Medium", "Large"], "image": "decor_items.png"},
        "Music Plaques": {"price": "₹699 - ₹1599", "stock": "Available", "sizes": ["A5", "A4"], "image": "music_plaques.png"},
        "Image Sets": {"price": "₹1499 - ₹3999", "stock": "Available", "sizes": ["A3", "A2"], "image": "image_sets.png"},
        "Newspaper Posters": {"price": "₹999 - ₹2999", "stock": "Available", "sizes": ["A4", "A3"], "image": "newspaper_posters.png"},
        "Distance Maps": {"price": "₹999 - ₹2999", "stock": "Available", "sizes": ["A3", "A2"], "image": "distance_maps.png"},
        "Line Art": {"price": "₹999 - ₹2999", "stock": "Available", "sizes": ["A4", "A3", "A2"], "image": "line_art.png"},
        "Religious Paintings": {"price": "₹999 - ₹2999", "stock": "Available", "sizes": ["A3", "A2"], "image": "religious_paintings.png"},
        "Sports Paintings": {"price": "₹1299 - ₹2999", "stock": "Available", "sizes": ["A3", "A2"], "image": "sports_paintings.png"},
        "Other Art": {"price": "₹699 - ₹2999", "stock": "Available", "sizes": ["A4", "A3"], "image": "other_art.png"},
        "Personalised Gifts": {"price": "₹1499 - ₹1999", "stock": "Available", "sizes": ["A5", "A4", "A3"], "image": "personalised_gifts.png"}
    }


def ask_bot(question, st):
    faq = get_faq()
    products = get_products()
    found = False
    q = question.lower()

    # Check FAQs
    if "delivery" in q or "when will i get" in q:
        st.info(faq["delivery"])
        return

    elif "offer" in q or "discount" in q:
        st.success(faq["offers"])
        return

    elif "return" in q:
        st.info(faq["return"])
        return

    elif "payment" in q or "payment options" in q:
        st.info(faq["payment"])
        return

    # Product-related
    for product in products:
        prod_lower = product.lower()
        if prod_lower in q:
            if "stock" in q:
                st.info(f"{product} is {products[product]['stock']}.")
                found = True
            elif "price" in q:
                st.info(f"Price for {product}: {products[product]['price']}")
                found = True
            elif "size" in q or "sizes" in q:
                sizes = ", ".join(products[product]['sizes'])
                st.info(f"Available sizes for {product}: {sizes}")
                found = True
            elif "image" in q or "show me" in q:
                st.image(products[product]["image"], width=300)
                st.caption(f"📸 {product}")
                found = True
            break

    if not found:
        st.warning("❓ Sorry, I didn’t understand. You can ask about products, pricing, delivery, offers, stock, or sizes.")
