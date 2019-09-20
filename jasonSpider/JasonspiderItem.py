# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JasonspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    release_time = scrapy.Field()
    comment_count = scrapy.Field()
    view_count = scrapy.Field()
    recommended_count = scrapy.Field()
    pass
