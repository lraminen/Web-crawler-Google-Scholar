# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


from openpyxl import Workbook,load_workbook
import os

class NcbiPipeline(object):
    def open_spider(self,spider):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['title', 'date', 'doi'])
    def process_item(self, item, spider):
        line=[item['title'],item['date'],item['doi']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        save_file=os.getcwd()+"\\result.xlsx"
        print('done')
        self.wb.save(save_file)

        
##class MongoDBPipeline(object):
##
##    def __init__(self):
##        connection = pymongo.MongoClient(
##            settings['MONGODB_SERVER'],
##            settings['MONGODB_PORT']
##        )
##        db = connection[settings['MONGODB_DB']]
##        self.collection = db[settings['MONGODB_COLLECTION']]
##
##    def process_item(self, item, spider):
##        
##        for data in item:
##            if not data:
##                raise DropItem("Missing data!")
##        self.collection.update({'url': item['url']}, dict(item), upsert=True)
##        log.msg("Question added to MongoDB database!",
##                level=log.DEBUG, spider=spider)
##        return item


    
##    
##class PubmedPipeline(object):
##    def process_item(self, item, spider):
##        return item
