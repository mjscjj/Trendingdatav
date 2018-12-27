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
    name = "mws"

    # http://wmoov.com/movie/showing﻿
    # ﻿http://wmoov.com/movie/upcoming﻿
    start_urls = ['http://wmoov.com/movie/showing','http://wmoov.com/movie/upcoming']

    collection_urls = []

    # 实现上下滑功能
    def start_requests(self):
        script = """
                function main(splash)
                    splash:set_viewport_size(1028, 10000)
                    splash:go(splash.args.url)
                    local scroll_to = splash:jsfunc("window.scrollTo")
                    scroll_to(0, 2000)
                    splash:wait(15)
                    return {
                        html = splash:html()
                    }
                end
                """

        for url in self.start_urls:
            yield Request(url, callback=self.parse_info_index, meta={
                'dont_redirect': True,
                'splash': {
                    'args': {'lua_source': script, 'images': 0},
                    'endpoint': 'execute',

                }
            })

    def parse_info_index(self, response):
        items = response.css('.each a::text').extract()
        for item in items:
            # 过滤英文
            item = clean_no_chinese_ustr(item)
            item = self.filter_word(item)
            if item:
                record = ScrapyWord()
                record['annotations'] = ['movie-name']
                record['word'] = item
                record['source'] = 'wmoov.com'
                yield record

    def filter_word(self, item):
        if len(item) < 3 or len(item) > 40:
            return
        dic = {'電影', '上映戲院'}
        for d in dic:
            if item.__contains__(d):
                return
        return item
