# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from .items import MusicRankItem, MovieRankItem, BookRankItem

class MongoPipeline(object):
    """
    重写MongoPipeline代码，直接从scrapy官方文档中复制的
    """

    collection_name = 'douban'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 用判断来分类存储数据
        if isinstance(item, MusicRankItem):
            self.db.music.insert(dict(item))
            return item
        if isinstance(item, MovieRankItem):
            self.db.movie.insert(dict(item))
            return item
        if isinstance(item, BookRankItem):
            self.db.book.insert(dict(item))
            return item
