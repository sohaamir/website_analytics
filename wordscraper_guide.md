# Creating a wordcloud of scientific terms used across a website

This is a detailed guide for creating a wordcloud of scientific terms used across the website (using `scrapy`, `spacy` and `nltk`).

<div align="center">
  <img src="https://github.com/sohaamir/website_projects/blob/main/wordscraper/assets/website_wordcloud.png" width="70%">
</div>

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
spacy
wordcloud
matplotlib
scrapy
nltk
```

#### Installing spacy
You will need to run the following manually in your `venv`: 

`python -m spacy download en_core_web_sm`

#### Installing nltk

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

### Extracting words using `scrapy`

We will run the Python framework `scrapy` to get a list of words that appear on the website. Information regarding how `scrapy` works and how to run it is available on their [documentation](https://docs.scrapy.org/en/latest/). The general command to run `scrapy` is: 

`scrapy runspider quotes_spider.py -o quotes.jsonl`

The official documentation describes this command:

> When you ran the command `scrapy runspider quotes_spider.py`, Scrapy looked for a Spider definition inside it and ran it through its crawler engine.
>
> The crawl started by making requests to the URLs defined in the `start_urls` attribute (in this case, only the URL for quotes in *humor* category) and called the default callback method `parse`, passing the response object as an argument. In the `parse` callback, we loop through the quote elements using a CSS Selector, yield a Python dict with the extracted quote text and author, look for a link to the next page and schedule another request using the same `parse` method as callback.

You don't need to know the exact details on how to set up your `scrapy` spider, but within the repository, this function is contained within the `sohaamir_spider.py` file:

```python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class SohaamirSpider(CrawlSpider):
    name = 'sohaamir'
    allowed_domains = ['sohaamir.github.io']
    start_urls = ['http://sohaamir.github.io/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # Extract all text nodes
        texts = response.xpath("//body//text()").extract()
        words = []
        for text in texts:
            # Split text into words and filter empty entries
            words += re.findall(r'\b\w+\b', text.lower())
        return {'url': response.url, 'words': words[14:]}  # Skip the first 14 entries as before

```

I also specifically modified the spider by changing the `pipelines.py` to use `nltk`. `nltk` (Natural Language Toolkit) is a library 'utilized primarily for its comprehensive list of English stop words. NLTK is a leading platform for building Python programs to work with human language data, offering libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, amongst other NLP tasks.'

Specifically, I incorporated it's use of stop words. This is a set of common English words that are often filtered out before processing natural language data, as they are considered to be of little value in understanding the essence of the text. Examples include "and", "the", "is", etc.

I also added a counter, which after filtering out the stop words, counts the remaining words that are considered more relevant for analysis.

This part of the code `pipelines.py` is shown below:

```py
import json
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

class WordscraperPipeline:
    def open_spider(self, spider):
        self.word_counts = Counter()

    def close_spider(self, spider):
        # Sort words by frequency in descending order
        sorted_word_counts = dict(sorted(self.word_counts.items(), key=lambda item: item[1], reverse=True))
        
        # Dump the sorted dict to JSON
        with open('words.json', 'w', encoding='utf-8') as f:
            json.dump(sorted_word_counts, f, ensure_ascii=False, indent=4)

    def process_item(self, item, spider):
        words = item['words']
        # Filter out the stop words
        filtered_words = [word for word in words if word.lower() not in stop_words]
        self.word_counts.update(filtered_words)
        return item
```

Despite looking complicated, everything is ran just by doing: 

```bash
cd wordscraper # making sure we are in the correct directory
scrapy crawl sohaamir -o words.json 
```

Which will generate `words.json`, is a list of words mentioned in the website and how much they are mentioned. 

```json
{
    "function": 313,
    "window": 228,
    "progressbar": 190,
    "e": 163,
    "css": 155,
    "document": 152,
    "getcurrentscrollposition": 152,
    "resizeprogressbar": 152,
    "top": 115,
  (and so on until line 2590)
    "published": 1,
    "clockwise": 1,
    "phoenix": 1,
    "byrne": 1,
    "hidden": 1,
    "dean": 1,
    "charlenne": 1,
    "ordonez": 1,
    "anastasiya": 1,
    "savchenko": 1,
    "rodriguez": 1,
    "sobstel": 1
}
```

(There is a problem where it generates a weird-looking last line, you will have to manually remove the last line from `words.json` for now until I fix this.)

But, we aren't interested in all of the words in my website! Most of these are nonsense words, we want something which is meaningful, such as scientific words. To specifically extract scientific words, I pasted the `json` into GPT and asked it to generate a list of scientific words as an array. As a side-note, I also extracted the names mentioned in my website, which was done using `spacy`. It uses Named Entity Recognition (NER)  to identify whether a word is a person's name. This is saved as `names.json`, but we will plot our scientific words output `scientific_words.json`.

We do both of this by running `python3 subsetting_json.py`:

```python
import json
import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Define your list of scientific words - asked ChatGPT to generate a list of scientific words from the .json file
scientific_words = set([
    "neuroscience", "psychiatry", "psychology", "programming", "mental", "learning", 
    "disorders", "cognitive", "computational", "behavioral", "neurocomputational", 
    "modelling", "neuroimaging", "decision", "therapy", "biomedical", "modelling", 
    "cognitive", "therapy", "neurotransmitters", "neuroethics", "neurodynamics", 
    "phd", "research", "academic", "university", "brain", "health", "science", 
    "imaging", "mri", "fmri", "spectroscopy", "behavior", "neural", "neurons", 
    "neurological", "physiological", "psychopharmacology", "haemodynamic", 
    "neurocognitive", "metacognitive", "diagnosis", "psychopathology", "neurotransmitters"
])  # Extend this list based on further detailed analysis or specific context of your project.


# Load words from the original JSON file
with open('../data/words.json') as f:
    word_counts = json.load(f)

# Initialize containers for scientific words and names
scientific = {}
names = {}

for word, count in word_counts.items():
    # Check if the word is in the predefined list of scientific words
    if word in scientific_words:
        scientific[word] = count
        continue
    
    # Use spaCy's NER to check if the word is a name
    doc = nlp(word)
    for ent in doc.ents:
        if ent.label_ in ["PERSON"]:
            names[word] = count
            break
    else:  # The word is not recognized as a name
        continue

# Write scientific words to a new JSON file
with open('../data/scientific_words.json', 'w') as f:
    json.dump(scientific, f, indent=4)

# Write names to another new JSON file
with open('../data/names.json', 'w') as f:
    json.dump(names, f, indent=4)
```

And then it is a simple case of plotting! To plot the wordcloud, run `python3 plot_wordcloud.py`.

And voila, you have your wordcloud of scientific terms!

