# -*- coding: utf-8 -*-
import scrapy

from ..items import K3Item


class K3spiderSpider(scrapy.Spider):
    name = 'k3spider'
    allowed_domains = ['k3.cn']
    start_urls = ['http://www.k3.cn/supplier/']

    def parse(self, response):
        for i in response.xpath("//div[@class='container']//ul[@class='seller_list']/li/div[@class='list_con']"):
            item = K3Item()
            item['名字'] = i.xpath("./div[@class='name']/a/text()").extract()
            item['网站地址'] = i.xpath("./div[@class='url']/a/text()").extract()
            item['QQ号码'] = i.xpath("./div[@class='text']/span[1]/text()").extract()
            item['手机号码1'] = i.xpath(".//input[@class='supplier_mobile_info_mobile']/@value").extract()
            item['手机号码2'] = i.xpath(".//input[@class='supplier_mobile_info_phone']/@value").extract()
            item['拿货地址'] = i.xpath("./div[last()]/text()").extract()
            yield item
        next_url = response.xpath("//span[@class='next']/a/@href").extract_first()
        if next_url:
            next_url = "http://www.k3.cn" + next_url
            yield scrapy.Request(next_url, callback=self.parse)
