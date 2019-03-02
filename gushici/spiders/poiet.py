# -*- coding: utf-8 -*-
import re

import scrapy

from scrapy import Request
from gushici.items import GushiciItem


class PoietSpider(scrapy.Spider):
    name = 'poiet'
    # allowed_domains = ['https://www.gushiwen.org/shiwen/']
    start_urls = ['https://www.gushiwen.org/shiwen/']
    def clean(self,poietlist):
        poiet=[]
        for sentence in poietlist:
            if sentence!='\n' and sentence!='\u3000\\u3000':
                sentence=sentence.replace('\n','')\
                    .replace('\u3000\u3000','')
                poiet.append(sentence)
        return poiet
    def parse(self, response):
        timeauthorlist=response.css('.source a::text').extract()
        namelist=response.css('.cont b::text').extract()
        quotes=response.css('.contson')
        contentlist=[]
        for quote in quotes:
            contentlist.append(quote.css('::text').extract())
        item=GushiciItem()
        for i in range(len(contentlist)):
            item['time']=timeauthorlist[i*2]
            item['author']=timeauthorlist[i*2+1]
            item['name']=namelist[i]
            item['content']=self.clean(contentlist[i])
            yield item
        next_page_url='https://www.gushiwen.org'+response.css('.amore::attr(href)').extract_first()
        yield Request(callback=self.parse,url=next_page_url)