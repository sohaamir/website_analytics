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
