# Import scrapy library
import scrapy


# Create the spider class
class YourSpider(scrapy.Spider):
    name = "your_spider"

    # start_requests method
    def start_requests(self):
        yield scrapy.Request(url="https://www.datacamp.com", callback=self.parse)

    # parse method
    def parse(self, response):
        pass


# Inspect Your Class
inspect_class(YourSpider)

'''
Output:
The url you would scrape is: https://www.datacamp.com
The name of the callback method you called is: parse
'''