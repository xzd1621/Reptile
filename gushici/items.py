# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GushiciItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()#诗词名字
    author=scrapy.Field()#作者
    time=scrapy.Field()#年代
    content=scrapy.Field()#内容


