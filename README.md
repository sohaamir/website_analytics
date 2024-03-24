# Website projects

This directory contains code for some projects related to my [GitHub website](https://sohaamir.github.io/). 

- Creating a wordcloud of scientific terms used across the website (using `scrapy`, `spacy` and `nltk`).
- Generating a deployable app that refreshes scenic cartoon wallpapers and inspirational quotes (using `requests` and `streamlit`).

## Directory structure

```
├── README.md
├── quotes.json
├── quotes_app_guide.md
├── quotes_generator
│   ├── app.py
│   ├── assets
│   │   └── streamlit.gif
│   └── quotes.json
├── requirements.txt
├── wordscraper
│   ├── assets
│   │   └── website_wordcloud.png
│   ├── data
│   │   ├── names.json
│   │   ├── scientific_words.json
│   │   └── words.json
│   ├── misc_code
│   │   ├── plot_wordcloud.py
│   │   ├── slice_json.py
│   │   └── subsetting_json.py
│   ├── scrapy.cfg
│   └── wordscraper
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-311.pyc
│       │   ├── pipelines.cpython-311.pyc
│       │   └── settings.cpython-311.pyc
│       ├── items.py
│       ├── middlewares.py
│       ├── pipelines.py
│       ├── settings.py
│       └── spiders
│           ├── __init__.py
│           ├── __pycache__
│           │   ├── __init__.cpython-311.pyc
│           │   └── sohaamir_spider.cpython-311.pyc
│           └── sohaamir_spider.py
└── wordscraper_guide.md
```

## Creating a wordcloud of scientific terms used across the website

<div align="center">
  <img src="https://github.com/sohaamir/website_projects/blob/main/wordscraper/assets/website_wordcloud.png" width="70%">
</div>
<br>
The following packages were used:

- `Scrapy`: Extracting structured text data from the website.
- `Spacy`: Processing text, identifying scientific terms with better accuracy.
- `NLTK`: Supporting text filtering based on a scientific vocabulary list.
- `Wordcloud`: Generating a visually insightful word cloud.

1. Web Scraping with Scrapy:

I designed a Scrapy spider to systematically navigate my GitHub website. The spider carefully extracted textual content from designated sections of the website using CSS selectors. This scraped data was stored for further processing.

2. Scientific Term Extraction with Spacy and NLTK:

I then loaded Spacy's 'en_core_sci_sm' model, a language model trained on scientific texts, for enhanced accuracy in recognizing relevant terms.
The scraped text was cleaned and tokenized using Spacy. Spacy's part-of-speech tagging identified nouns and adjectives, focusing on scientific terms.

NLTK cross-referenced the extracted words with a curated list of common scientific terms, filtering the results.

3. Word Cloud Generation with Wordcloud:

Using the Wordcloud library, I generated a word cloud highlighting the most frequently occurring scientific terms on the website.



## Creating a wordcloud of scientific terms used across the website

<div align="center">
  <img src="https://github.com/sohaamir/website_projects/blob/main/quotes_generator/assets/streamlit.gif" width="70%">
</div>
<br>

The project utilizes the following packages:

- `streamlit`: For creating and hosting the web app.
- `requests`: To fetch random background images from the web.
- `Pillow`: For image processing tasks.

1. **Quote Extraction and JSON Storage**:

I sourced a comprehensive list of inspirational quotes in JSON format from a GitHub repository. This file, `quotes.json`, provide the list of quotes for the app.

2. **Dynamic Background Image Fetching with Requests**:

I utilized the wallpaper library [Minimalistic Wallpaper Collection](https://github.com/DenverCoder1/minimalistic-wallpaper-collection) which includes a random wallpaper API. We can then request random wallpapers from the collection and load it into our app.

3. **Streamlit App Development**:

- The app was built using Streamlit to read quotes from the JSON file. 
- Utilizing a combination of the `random` library for quote selection and time-controlled loops with `time.sleep(10)`, the app is designed to continuously loop through both quotes and wallpaper, presenting a new quote and background image approximately every 10 seconds.

**Deployment on Streamlit Sharing**:

The app is prepared for deployment on Streamlit Sharing, a platform that simplifies the process of bringing Python apps online. By connecting the GitHub repository containing the app's code, the app can be easily shared and accessed via the web.

You can access the app by going to https://quotesgenerator.streamlit.app (although it doesn't run for very long due to request limitations from the API I think).

