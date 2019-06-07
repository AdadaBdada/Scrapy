# -*- coding: utf-8 -*-
import scrapy
from scrapy_items_example.items import ScrapyItemsExampleItem


class SampleItemsSpiderSpider(scrapy.Spider):
    name = "sample_items_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = (
        'http://quotes.toscrape.com/',
    )

    def parse(self, response):
        authors = response.xpath('//*[@itemprop="author"]/text()').extract()

        item = ScrapyItemsExampleItem()
        item['authors'] = authors
        return item
