# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QqScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    data_from = scrapy.Field()
    #author = scrapy.Field()
    #check = scrapy.Field()
    #comment = scrapy.Field()
    #click = scrapy.Field()
