# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import re

class CleanPipeline(object):

    def process_item(self, item, spider):

        # 清洗 item['comment_count']
        comment = []
        for value in item['comment_count']:
            comment.append(re.findall('[0-9]+', value)[0])
        item['comment_count'] = comment

        # 清洗 item['release_time']
        release = []
        for i in range(len(item['release_time'])):
            if i % 2 != 0:
                release.append(re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', item['release_time'][i])[0])
        item['release_time'] = release

        # 清洗 item['view_count']
        view = []
        for i in range(len(item['view_count'])):
            view.append(re.findall('[0-9]+', item['view_count'][i])[0])
        item['view_count'] = view

        return item

class JsonPipeline(object):
    def __init__(self):
        print('打开文件准备写入。。。')
        self.flie = codecs.open('cnblogs.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        print('正在写入。。。')
        line = json.dumps(dict(item), ensure_ascii=False)+'\n'
        self.flie.write(line)
        return item

    def close_spider(self, spider):
        print('写入完成，关闭文件')
        self.flie.close()