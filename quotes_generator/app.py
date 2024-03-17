import streamlit as st
import requests
import json
import random
import time
import os
import io
from PIL import Image

# Define a function to load quotes from the quotes.json file
def load_quotes():
    try:
        with open("quotes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("File quotes.json not found in the current directory.")
        return []
    except json.JSONDecodeError:
        st.error("Error reading quotes.json. Make sure the file is valid JSON.")
        return []

# Define a function to fetch a random background image
def fetch_random_background():
    response = requests.get("https://minimalistic-wallpaper.demolab.com/?random")
    return response.content if response.status_code == 200 else None

# Define a function to display a quote and author over a background image
def display_quote(quote, author, background_image_bytes):
    # Display the image with the quote as a caption
    st.image(background_image_bytes, caption=f'"{quote}" - {author}', use_column_width='always')

# Define the main function of the Streamlit app
def main():
    st.title('Inspirational Quotes Generator')

    # Load quotes
    quotes = load_quotes()

    # Check if quotes are loaded
    if not quotes:
        st.warning("No quotes to display.")
        return

    # Continuously update the quote and background
    while True:
        # Randomly select a quote and its author
        selected_quote = random.choice(quotes)
        quote_text = selected_quote["quote"]
        quote_author = selected_quote["author"]
        
        # Fetch a random background image
        background_image_bytes = fetch_random_background()
        
        # Display quote and author on the background image
        if background_image_bytes:
            display_quote(quote_text, quote_author, background_image_bytes)
        
        # Sleep for some time before showing the next quote
        time.sleep(10)  # Adjust the sleep time as needed

        # Rerun the app to update the quote and background
        st.rerun()

# Run the Streamlit app
if __name__ == "__main__":
    main()
