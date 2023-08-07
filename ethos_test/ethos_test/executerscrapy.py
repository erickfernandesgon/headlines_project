# run_spider.py

from scrapy.crawler import CrawlerProcess
from ethos_test.ethos_test.spiders import ethos

def run_spider():
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',  # Output format (JSON)
        'FEED_URI': r'C:\Users\egoncal9\PycharmProjects\pythonProject2\ethos_test\newversion2.json',  # Output file path
        # Add other settings as needed
    })

    process.crawl(ethos.KeywordsSpider)
    process.start()

if __name__ == "__main__":
    run_spider()
