#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>

from scrapy.spiders import CrawlSpider, Rule, Request
import scrapy
# 配合Rule进行URL规则匹配
from scrapy.linkextractors import LinkExtractor
from Trendingdatav2.items import ScrapyWord
from Trendingdatav2.utils import *


class myspider(scrapy.Spider):
    name = "movie_theatre"

    # http://wmoov.com/movie/showing﻿
    # ﻿http://wmoov.com/movie/upcoming﻿
    start_urls = ['http://wmoov.com/cinema']


    def parse(self, response):
        items = response.css('.list a::text').extract()
        for item in items:
            print item
            # 过滤英文
            item = clean_no_chinese_ustr(item)
            item = self.filter_word(item)
            if item:
                record = ScrapyWord()
                record['annotations'] = ['movie-name']
                record['word'] = item
                record['source'] = 'wmoov.com.theatre'
                yield record

    def filter_word(self, item):
        if len(item) < 3 or len(item) > 40:
            return
        return item
