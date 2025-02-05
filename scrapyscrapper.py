import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://www.northeastern.edu/"]

    def parse(self, response):
        # Extract data
        title = response.css("title::text").get()
        links = response.css("a::attr(href)").getall()

        yield {
            "title": title,
            "links": links,
        }

# Run the spider (from command line)
# scrapy runspider example_spider.py -o output.json