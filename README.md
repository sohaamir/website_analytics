# Website analytics

This directory contains code for some analytics of my [GitHub website](https://sohaamir.github.io/).

### Creating a wordcloud of scientific terms used

Here is how I was able to create the following wordcloud plot, based upon the number of times a scientific term was used in my website:

[image]

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

```bash
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
```
import nltk
nltk.download('punkt')
```

and then 

`exit()`

### Running the scripts

From inside your `venv` at the root of the `website_analytics` directory:

`cd/ wordscraper` and run `scrapy crawl sohaamir -o words.json`.

Manually remove the last line (for now until I fix this).

Then run `python3 subsetting_json.py`, `pip install wordcloud` and `python3 plot_wordcloud.py`.
