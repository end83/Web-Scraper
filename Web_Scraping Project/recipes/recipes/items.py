# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class Cookbook(Item):
    # define the fields for your item here like:
    name=Field()
    nutrients=Field()
    steps=Field()
    ingredients=Field()
    reviews=Field()
    
