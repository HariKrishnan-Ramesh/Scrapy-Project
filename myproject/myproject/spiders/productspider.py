import scrapy


class ProductSpider(scrapy.Spider):
    name = 'product'
    start_urls = ['https://www.bayut.com/to-rent/property/dubai/']

    
