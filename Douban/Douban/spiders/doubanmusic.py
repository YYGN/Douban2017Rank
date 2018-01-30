# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from Douban.items import MusicRankItem
import json


class DoubanSpider(Spider):
    """
        This application is work for crawling the 2017's rank of music that on douban website.
        OS: Ubuntu 16.04
        Python version: 3.5.2
        Author: YYGN
        data: 2018.1.30
        IDE: Pycharm
        """
    name = 'doubanmusic'
    allowed_domains = ['douban.com']
    start_urls = ['https://music.douban.com/ithil_j/activity/music_annual2017/widget/{page}'.format(page=str(page)) for page in range(1, 55)]

    def parse(self, response):
        item = MusicRankItem()
        data = json.loads(response.text)
        if data and 'res' in data.keys():
            res = data.get('res')
            if res:
                if 'subjects' in res.keys() and res.get('subjects'):
                    item['subjects'] = res.get('subjects')
                else:
                    return None
                if 'payload' in res.keys():
                    payload = res.get('payload')
                    item['title'] = payload.get('title')
                    item['background_img'] = payload.get('background_img')
                    item['description'] = payload.get('description')
                if 'user' in res.keys():
                    user = res.get('user')
                    item['avatar'] = user.get('avatar')
                    item['id'] = user.get('id')
                    item['name'] = user.get('name')
                    item['url'] = user.get('url')
            yield item