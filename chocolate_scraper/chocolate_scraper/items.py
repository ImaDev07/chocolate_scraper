# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ChocolateItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()
