from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowedDomains = ["toscrape.com"]
    start_url = ["http://books.toscrape.com"]