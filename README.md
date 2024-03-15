# Website analytics

This directory contains code for some analytics of my [GitHub website](https://sohaamir.github.io/).

## Setting up the environment:

Here are instructions on how to set up your environment:

```bash
git clone <repo>
cd <repo>
pip install virtualenv (if you don't already have virtualenv installed)
virtualenv venv to create your new environment (called 'venv' here)
source venv/bin/activate to enter the virtual environment
pip install -r requirements.txt
```
The more basic `requirements.txt` file is:

```bash
spacy
wordcloud
matplotlib
scrapy
nltk
```

### Installing spacy
You may need to run the following manually in your terminal: 

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

`cd /your/venv/path/here `

and activate venv by 

`source scrapyenv311/bin/activate `

`cd/ wordscraper` and run `scrapy crawl sohaamir -o words.json`

Manually remove the last line (for now until I fix this).

Then run `python3 subsetting_json.py`, `pip install wordcloud` and `plot_wordcloud.py`.
