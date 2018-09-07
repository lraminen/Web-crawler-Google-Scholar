# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
import pymongo

class GscholarPipeline(object):
    def __init__(self):
        self.file=open('items.json','w')
        self.titles=set()
    def process_item(self, item, spider):
        item['title']=''.join(item['title'])
        if item['title'] not in self.titles:
            line=json.dumps(dict(item),ensure_ascii=False)+"\n"
            self.file.write(line)
        self.titles.add(item['title'])
        return item
    def close_file(self,spider):
        self.file.close()

                        
