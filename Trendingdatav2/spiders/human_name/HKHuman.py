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
from Trendingdatav2.utils import *


class myspider(CrawlSpider):
    name = 'hkhuman'
    # allowed_domains = ['cuiqingcai.com']
    count_all = 0
    url_all = []
    start_urls = ['https://zh.wikiquote.org/zh-hk/Category:香港人']

    def parse(self, response):
        urls = response.css('.mw-content-ltr a::attr(href)').extract()
        for url in urls:
            yield response.follow(url, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        items = response.css('.mw-content-ltr ::text').extract()
        for item in items:
            its = item
            item = clean_no_chinese_ustr(item)
            item = self.filter_word(item)
            print item
            if item and not is_Contain_non_Chinese(its):
                record = ScrapyWord()
                record['annotations'] = ['human-name']
                record['word'] = its
                record['source'] = 'HK.man'
                yield record

    def filter_word(self, item):
        if len(item) <= 3 or len(item) > 12:
            return
        dic = {'香港', '类', '人', '页面', '编辑', '维基'}
        for d in dic:
            if item.__contains__(d):
                return
        return item
