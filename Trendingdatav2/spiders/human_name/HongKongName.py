#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>


import sys

# reload(sys)
# sys.setdefaultencoding('UTF-8')
from scrapy.spiders import CrawlSpider, Rule, Request
# 配合Rule进行URL规则匹配
from scrapy.linkextractors import LinkExtractor
from Trendingdatav2.items import ScrapyWord


class myspider(CrawlSpider):
    name = 'hkname'
    # allowed_domains = ['cuiqingcai.com']
    count_all = 0
    url_all = []
    start_urls = ['https://zh.wikiquote.org/zh-hk/Category:香港人']
    label_tags = ['爬虫', 'scrapy', 'selenium', 'selenium']

    rules = (
        Rule(LinkExtractor(allow=(".*.*",)), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        items = response.css('.mw-content-ltr ::text').extract()
        for item in items:
            item = unicode.encode(item, 'utf-8')
            item = item.strip()
            item = self.filter_word(item)
            print item
            if item:
                record = ScrapyWord()
                record['annotations'] = ['human-name']
                record['word'] = item
                record['source'] = 'HK.man'
                yield record

    def filter_word(self, item):
        if len(item) <= 3 or len(item) > 12 or item.__contains__('(') or item.__contains__('.') or item.__contains__(
                '香港') or item.__contains__('外部') or item.__contains__('编辑') or item.__contains__('人') \
                or item.__contains__('类'):
            return
        return item
