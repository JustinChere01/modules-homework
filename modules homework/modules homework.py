# mood_responses.py

def mood_response(mood):
    """
    Returns a custom message based on the user's mood.

    Args:
        mood (str): The user's mood (e.g., happy, sad, excited).

    Returns:
        str: Custom message corresponding to the mood.
    """
    if mood.lower() == "happy":
        return "Great to hear that you're feeling happy!"
    elif mood.lower() == "sad":
        return "I'm sorry to hear that you're feeling sad. Remember, it's okay to reach out to someone."
    elif mood.lower() == "excited":
        return "Awesome! Excitement is contagious. What's got you so pumped?"
    else:
        return "I'm not sure how to respond to that mood. 🤔"

# You can add more mood-specific responses as needed.
