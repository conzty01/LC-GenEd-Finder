# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('lcCourses.json','w',encoding='utf-8')
        self.file.write('[\n')

    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False) + ',' + '\n'
        self.file.write(line)
        return item

    def close_spider(self,spider):
        self.file.close()
        self.file = self.file = codecs.open('lcCourses.json','r',encoding='utf-8')
        outString = self.file.read()[:-2] + '\n' + ']'
        self.file.close()
        self.file = codecs.open('lcCourses.json','w',encoding='utf-8')
        self.file.write(outString)
        self.file.close()
