# Generating a deployable app that refreshes scenic cartoon wallpapers and inspirational quotes (using `requests` and `streamlit`).

Do you need constant inspiration? If so, then it may be worth creating an app which cycles through inspiration quotes and scenic wallpapers. The tutorial will guide you on how you can do so by creating your own app via `streamlit`. You can then subsequently host your app online, for anyone to see! 

The end result should look something like this:

![streamlit_app](https://github.com/sohaamir/website_projects/blob/main/quotes_generator/assets/streamlit.gif)

### Setting up the environment:

Here are instructions on how to set up your environment:

```bash
git clone <repo>
cd <repo>
pip install virtualenv # (if you don't already have virtualenv installed)
virtualenv venv # to create your new environment (called 'venv' here)
source venv/bin/activate # to enter the virtual environment
pip install -r requirements.txt
```

The relevant dependencies contained within the `requirements.txt` file are:

```python
streamlit
requests
Pillow
```

### Creating the app

Despite seeming to be quite complicated, there isn't a whole lot to this project. Just looking at the directory structure, we only have two files:

```bash
├── app.py
└── quotes.json
```

`quotes.json` refers to the fact that we are obviously going to need some quotes to load into our app, and so I just downloaded [this](https://github.com/AtaGowani/daily-motivation/blob/master/src/data/quotes.json) json file from GitHub.

```json
[
  {
    "quote": "What you do today can improve all your tomorrows.",
    "author": "Ralph Marston"
  },
  {
    "quote": "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "author": "Zig Ziglar"
  },
  {
    "quote": "Intelligence without ambition is a bird without wings.",
    "author": "Salvador Dali"
  },
  {
    "quote": "The key is to keep company only with people who uplift you, whose presence calls forth your best.",
    "author": "Epictetus"
  }
 ]
```

And to create the app, we just need 66 lines of code!

```python
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
```

There is quite a bit to unpack here. The code does the following:

- Defines a function `load_quotes()` to load quotes from our `quotes.json` file.
- Implements a function `fetch_random_background()` that retrieves a random background image from  [Minimalistic Wallpaper Collection](https://github.com/DenverCoder1/minimalistic-wallpaper-collection). Vitally, this includes a random wallpaper API, so we can request random wallpapers from the collection using a web request.
- Contains a function `display_quote(quote, author, background_image_bytes)` for displaying a quote and its author over a provided background image using Streamlit's `image` method.
- Using `random` we randomly loop through both the quotes and wallpapers, and utilize a sleep interval (`time.sleep(10)`) to refresh content every 10 seconds.

All you need to do now is to deploy your app on [Streamlit](https://streamlit.io), a service that makes it very easy and straightforward to create and deploy Python code as online interactive apps. All you have to do is to register (free) hook up your GitHub repository with your `streamlit.py` file and deploy!

And voila, you now have your own app, hosted online! You can access the app by going to https://quotesgenerator.streamlit.app (although it doesn't run for very long due to request limitations from the API I think).

![streamlit_app](https://github.com/sohaamir/website_projects/blob/main/quotes_generator/assets/streamlit.gif)
