# Website projects

This directory contains code for some projects related to my [GitHub website](https://sohaamir.github.io/). 

Specifically, this involves:

- Creating a wordcloud of scientific terms used across the website (using `scrapy`, `spacy` and `nltk`).
- Generating a deployable app that refreshes scenic cartoon wallpapers and inspirational quotes (using `beautifulsoup4`, `serpapi`, `requests` and `streamlit`).

## Project structure

```

```

## Creating a wordcloud of scientific terms used across the website

Here is how I was able to create the following wordcloud plot, based upon the number of times a scientific term was used in my website:

[put wordcloud here]

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

From inside your `venv` at the root of the `website_analytics` directory:

`cd wordscraper` and then run `scrapy crawl sohaamir -o words.json`.

Manually remove the last line from `words.json` (for now until I fix this).

Then run `python3 subsetting_json.py`, `pip install wordcloud` and `python3 plot_wordcloud.py`.
