# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EnglishwordsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #单词释意不完整
    word = scrapy.Field()
    phoneticSymbols = scrapy.Field()
    meaning = scrapy.Field()
    example = scrapy.Field()
    



