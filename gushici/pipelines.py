# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class GushiciPipeline(object):
    def __init__(self):
        host='localhost'
        port=27017
        db='gushici'
        sheet='poiet'
        client=MongoClient(host,port)
        mydb=client[db]
        self.post=mydb[sheet]
    def process_item(self, item, spider):
        data=dict(item)
        self.post.insert(data)
        return item
