# -*- coding: utf-8 -*-
import scrapy
from demo01.items import Demo01Item


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['https://sz.fang.lianjia.com/']

    def parse(self, response):
        title = response.xpath('//p[@class="title"]/a/text()').extract()
       	price = response.xpath('//span[@class="price"]/text()').extract()
       	description = response.xpath('//p[@class="title"]/span/text()').extract()
       	address = response.xpath('//p[@class="list-name"]/text()').extract()
        image_urls = response.xpath('//div[@class="items-list fl"]/a/img/@src').extract()

        
        items = []
        i=1
        while i < 5:
        	item = Demo01Item()
	        item["title"] = title[i]
	        item["price"] = price[i]
	        item["description"] = description[i]
	        item["address"] = address[i]
	        item["image_urls"] = image_urls[i]
	        items.append(item)
	        i +=  1

        return items
