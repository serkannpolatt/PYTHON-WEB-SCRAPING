# -*- coding: utf-8 -*-
import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.groupon.com']
    start_urls = ['https://www.groupon.com/landing/deal-of-the-day']

    def parse(self, response):
        for product in response.xpath("//div[@class='grpn-dc-caption']"):
            yield{
                "title" : product.xpath(".//div[@class='grpn-dc-title grpn-dc-two-line-ellipsis']/text()").get(),
                "price" : product.xpath(".//span[@class='wh-dc-price-discount wh-dc-urgent']/text()").get(),
                "products_sold" : product.xpath(".//div[@class='wh-quantity-bought wh-txt-grey']/text()").get()
            }


