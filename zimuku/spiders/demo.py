# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from zimuku.items import ZimukuItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['zimuku.net']
    start_urls = ['http://zimuku.net']

    def parse(self, response):
        items={}
        names=response.xpath('//b/text()').extract()
        items['names']=names
        yield items
        next_url=response.xpath('//body/div[@class="container"]/div/div//div/a[@class="next"]/@href').extract()[0]
        if next_url:
            url='http://zimuku.net'+next_url
            yield scrapy.Request(url,callback=self.parse)
