# -*- coding: utf-8 -*-
import scrapy
import logging

class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['www.google.com']
    start_urls = ['http://www.google.com/','http://www.baidu.com/']
    def  make_requests_from_url(self,url):
        logger=logging.getLogger(__name__)
        self.logger.debug("--------------------")
        print('***********************')
        return scrapy.Request(url=url,meta={'download_timeout':3},callback=self.parse)

    def parse(self, response):
        print('++++++++++++++++++++++++++++')
        print(response.text)
