# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UsdtoirtItem(scrapy.Item):

    persionDate = scrapy.Field()
    latinDate = scrapy.Field()
    changePercent = scrapy.Field()
    changeAmount = scrapy.Field()
    closeValue = scrapy.Field()
    maxValue = scrapy.Field()
    minValue = scrapy.Field()
    openValue = scrapy.Field()
    
