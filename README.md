# Website projects

This directory contains code for some projects related to my [GitHub website](https://sohaamir.github.io/). 

- Creating a wordcloud of scientific terms used across the website (using `scrapy`, `spacy` and `nltk`).
- Generating a deployable app that refreshes scenic cartoon wallpapers and inspirational quotes (using `requests` and `streamlit`).

## Directory structure

```
├── README.md
├── quotes.json
├── quotes_generator
│   ├── app.py
│   └── quotes.json
├── requirements.txt
└── wordscraper
    ├── assets
    │   └── website_wordcloud.png
    ├── data
    │   ├── names.json
    │   ├── scientific_words.json
    │   └── words.json
    ├── misc_code
    │   ├── plot_wordcloud.py
    │   ├── slice_json.py
    │   └── subsetting_json.py
    ├── scrapy.cfg
    └── wordscraper
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-311.pyc
        │   ├── pipelines.cpython-311.pyc
        │   └── settings.cpython-311.pyc
        ├── items.py
        ├── middlewares.py
        ├── pipelines.py
        ├── settings.py
        └── spiders
            ├── __init__.py
            ├── __pycache__
            │   ├── __init__.cpython-311.pyc
            │   └── sohaamir_spider.cpython-311.pyc
            └── sohaamir_spider.py
```

## Creating a wordcloud of scientific terms used across the website

Here is how I was able to create the following wordcloud plot, based upon the number of times a scientific term was used in my website:

<div align="center">
  <img src="https://github.com/sohaamir/website_projects/blob/main/wordscraper/assets/website_wordcloud.png" width="60%">
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

## Setting up the environment:

Here are instructions on how to set up your environment:

```bash
git clone <repo>
cd <repo>
pip install virtualenv # (if you don't already have virtualenv installed)
virtualenv venv # to create your new environment (called 'venv' here)
source venv/bin/activate # to enter the virtual environment
pip install -r requirements.txt
```

The dependencies contained within the `requirements.txt` file are:

```python
spacy
wordcloud
matplotlib
scrapy
nltk
```

### Installing spacy
You will need to run the following manually in your `venv`: 

`python -m spacy download en_core_web_sm`

### Installing nltk

You may also need to manually install `nltk` which you can do using the following steps:

Navigate to the Python installation directory by running:
`cd "/path/to/your/python"`

e.g.
`cd "/Applications/Python 3.11"`

Run the Install Certificates.command script by typing:
`"./Install\ Certificates.command"`

Open python3 in your terminal and type the following:
```python
import nltk
nltk.download('punkt')
```

and then 

`exit()`.

### Running the scripts

Make sure you are in the correct directory when running these scripts!

From inside your `venv` at the root of the `website_analytics` directory:

Change into the correct directory by `cd wordscraper` and then run `scrapy` on the website by `scrapy crawl sohaamir -o words.json`.

This will generate `words.json`, which is a list of words mentioned in the website. You will have to manually remove the last line from `words.json` (for now until I fix this).

Then run `python3 subsetting_json.py` which subsets the words to scientific words using `spacy`. 

To plot the wordcloud, run `python3 plot_wordcloud.py`.

And voila, you have your wordcloud of scientific terms!
