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
    name = "g_game"

    start_urls = ['https://play.google.com/store/apps/category/GAME']

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
        texts = response.css('.details .title::text').extract()
        mores = response.css('.cluster-heading')
        if mores:
            for url in mores:
                url = url.css('h2.single-title-link a::attr(href)').extract_first()
                yield response.follow(url, callback=self.parse_info_index, dont_filter=False)

        for txt in texts:
            # 过滤英文
            txt = clean_no_chinese_ustr(txt)
            if len(txt) <= 3:
                continue
            record = ScrapyWord()
            record['annotations'] = ['game-name']
            record['word'] = txt
            record['source'] = 'google.game'
            yield record

    def filter_word(self, item):
        if len(item) <= 3 or len(item) > 12:
            return
        dic = {'香港', '类', '人', '页面', '编辑', '维基'}
        for d in dic:
            if item.__contains__(d):
                return
        return item
