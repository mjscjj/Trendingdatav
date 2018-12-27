#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>
import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from Trendingdatav2.items import ScrapyWord
from Trendingdatav2.utils import *


class itemSpider(scrapy.Spider):

    name = 'tvb'

    start_urls = ['http://programme.tvb.com/']

    def parse(self, response):
        # print response.text
        record = ScrapyWord()
        items = response.css('.iitem ::text').extract()
        for item in items:
            item = unicode.encode(item, 'UTF-8')
            if str.__contains__(item, "#"):
                idx = item.index("#")
                item = item.__getslice__(0, idx)
            if str.__contains__(item, '['):
                idx = item.index("[")
                item = item.__getslice__(0, idx)
            item = clean_no_chinese_strstr(item)
            item = self.filter_word(item)
            if item:
                record['annotations'] = ['tv-show-name']
                record['word'] = item
                record['source'] = 'tvb.com'
                yield record

    def filter_word(self, item):
        if len(item) < 3 or str.__contains__(item, ":"):
            return

        return item
