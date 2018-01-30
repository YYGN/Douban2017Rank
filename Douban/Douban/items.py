# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MusicRankItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    background_img = Field()
    description = Field()
    title = Field()
    avatar = Field()
    id = Field()
    name = Field()
    url = Field()
    subjects = Field()

class MovieRankItem(Item):
    background_img = Field()
    description = Field()
    title = Field()
    avatar = Field()
    id = Field()
    name = Field()
    url = Field()
    subjects = Field()

class BookRankItem(Item):
    pass