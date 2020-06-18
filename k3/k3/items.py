# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class K3Item(scrapy.Item):
    # 名字
    # 网站地址
    # QQ号码
    # 手机号码
    # 公司地址
    名字 = scrapy.Field()
    网站地址 = scrapy.Field()
    QQ号码 = scrapy.Field()
    手机号码1 = scrapy.Field()
    手机号码2 = scrapy.Field()
    拿货地址 = scrapy.Field()
