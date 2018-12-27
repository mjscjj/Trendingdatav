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
    name = 'sanlian'
    count_all = 0
    url_all = []
    # http://www.jointpublishing.com/publishing/media-coverage.aspx
    start_urls = ['http://www.jointpublishing.com/publishing/lastest-publishing.aspx']

    def parse(self, response):
        items = response.css('.bookPreviewImage a::attr(title)').extract()
        for item in items:
            print item
        next_page = response.xpath('//*[@id="p_lt_ctl05_phMasterContent_p_lt_ctl00_phSectionContent_p_lt_ctl03_repeaterBookListing_lkbAfterPageBottom"]').extract_first()
        if next_page is not None:
            # next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_item(self, response):
        print '=======&&&-======='
        items = response.css('.mw-content-ltr ::text').extract()
        for item in items:
            item = clean_no_chinese_ustr(item)
            item = self.filter_word(item)
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
