from modules.query_handler import handle_query
from modules.response_generator import generate_response
from modules.logger import log_unanswered_query

def chatbot_pipeline(user_query, use_openai=True):
    """
    Main pipeline to handle incoming user queries and generate a response.
    
    Args:
        user_query (str): The question asked by the user.
        use_openai (bool): Whether to use OpenAI to rephrase and enhance the answer.
        
    Returns:
        dict: A dictionary containing the chatbot's response and product info (if any).
    """
    try:
        # Handle product + FAQ matching
        response_data = handle_query(user_query)

        # If no match found
        if not response_data.get("answer") and not response_data.get("products"):
            log_unanswered_query(user_query)
            return {
                "answer": "I'm sorry, I couldn't find information on that. Please try rephrasing your question.",
                "products": []
            }

        # Enhance response using OpenAI (if enabled and key exists)
        final_response = generate_response(user_query, response_data, use_openai=use_openai)
        return final_response

    except Exception as e:
        return {
            "answer": f"An internal error occurred: {str(e)}",
            "products": []
        }







