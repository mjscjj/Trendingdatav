# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Trendingdatav2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ScrapyWord(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    word = scrapy.Field()
    annotations = scrapy.Field()
    source = scrapy.Field()
    pass
