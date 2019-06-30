# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TextPipeline(object):
    def __init__(self):
        self.limit=50
    def process_item(self, item, spider):
        if item['text']:
            if len(item['text'])>self.limit:
                item['text']=item['text'][0:self.limit].rstrip()+'...'
            return item
        else:
            return DropItem('Missing Text')
class LixuPip(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            a=crawler.settings.get('MONGO_URI'),
            b=crawler.settings.get('MONGO_DB')

       )
    def open_spider(self,spider):
        print('任务开始')
    def close_spider(self,spider):
        print('任务结束')
