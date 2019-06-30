# -*- coding: utf-8 -*-
import logging

import scrapy


class ZhihucrawalSpider(scrapy.Spider):
    name = 'zhihuCrawal'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    def  make_requests_from_url(self,url):
        logger=logging.getLogger(__name__)
        self.logger.debug("--------------------")
        print('***********************')
        return scrapy.Request(url=url,meta={'download_timeout':3},callback=self.parse)
    def parse(self, response):
        pass
