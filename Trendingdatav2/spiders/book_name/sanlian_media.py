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
import scrapy


class myspider(CrawlSpider):
    name = 'sl_m'
    count_all = 0
    url_all = []
    start_urls = ['http://www.jointpublishing.com/publishing/media-coverage.aspx']
    fix = 'http://www.jointpublishing.com/publishing/media-coverage.aspx?page='
    page = 1

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse_index)

    def parse_index(self, response):
        items = response.css('.mediaCoverageTitle a::attr(title)').extract()
        for item in items:
            print item
            ite = item
            if item.__contains__('-'):
                item = item.__getslice__(0, item.index('-'))
            if item.__contains__('（'):
                item = item.__getslice__(0, item.index('（'))
            if item.__contains__('：'):
                item = item.__getslice__(0, item.index('：'))
            item = clean_no_chinese_ustr(item)
            if item and 3 <= len(item) <= 30:
                record = ScrapyWord()
                record['annotations'] = ['book-name']
                record['word'] = item
                record['source'] = 'sanlian'
                yield record

        if items and len(items) > 1:
            self.page = self.page + 1
            url = self.fix + str(self.page)
            print url
            yield scrapy.Request(url, callback=self.parse_index)

    def parse_item(items):
        for item in items:
            item = clean_no_chinese_ustr(item)
            print item
            if item:
                record = ScrapyWord()
                record['annotations'] = ['human-name']
                record['word'] = item
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
