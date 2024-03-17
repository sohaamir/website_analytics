import streamlit as st
import requests
import json
import random
import time
import os

# Print the current working directory to debug file not found errors
st.write('Current directory:', os.getcwd())

# Try to load quotes from the quotes.json file
try:
    with open("../quotes.json", "r") as file:
        quotes = json.load(file)
except FileNotFoundError:
    st.error("File quotes.json not found in the current directory.")
    quotes = []

# Define a function to fetch a random background image
def fetch_random_background():
    response = requests.get("https://minimalistic-wallpaper.demolab.com/?random")
    return response.content if response.status_code == 200 else None

# Define a function to display a quote and author over a background image
def display_quote(quote, author, background_image_bytes):
    # Display the image with the quote as a caption
    st.image(background_image_bytes, caption=f'"{quote}" - {author}', use_column_width='always')

def main():
    st.title('Inspirational Quotes Generator')

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
        st.experimental_rerun()

if __name__ == "__main__":
    main()
