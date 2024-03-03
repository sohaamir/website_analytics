Do the following: 

Installing nltk

Navigate to the Python installation directory by running:
cd "/path/to/your/python"

e.g.
cd "/Applications/Python 3.11"

Run the Install Certificates.command script by typing:
"./Install\ Certificates.command"

Open python3 in your terminal and type the following:
import nltk
nltk.download('punkt')

and then 

exit()

- cd /scrapyenv311 and activate venv by source scrapyenv311/bin/activate 
- cd/ wordscraper and run scrapy crawl sohaamir -o words.json  
- manually remove last line (for now until I fix this)
- run python3 subsetting_json.py 
- run pip install wordcloud and run plot_wordcloud.py