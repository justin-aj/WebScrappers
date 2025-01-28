from autoscraper import AutoScraper

UrlToScrape = "https://www.northeastern.edu/"

WantedList = [
    "https://sandbox.oxylabs.io/products/category/nintendo",
    "https://sandbox.oxylabs.io/products/category/dreamcast"
]

Scraper = AutoScraper()
data = Scraper.build(UrlToScrape, wanted_list=WantedList)
print(data)
