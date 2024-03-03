# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

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