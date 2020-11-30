# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class Demo01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 基础字段
    title = Field()
    price = Field()
    description = Field()
    address = Field()
    image_urls = Field()

    # 可计算字段
    images = Field()
    location = Field()


    # 管理字段
    url = Field()
    project= Field()
    spider = Field()
    server = Field()
    date = Field()