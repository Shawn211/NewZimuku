# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ZimukuPipeline(object):
    def process_item(self, item, spider):
        with codecs.open('zimu','a+') as zm:
            names=item['names']
            for name in names:
                zm.write(name+'\n')
