#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>

import scrapy


class Yahoo_tw(scrapy.Spider):  # 需要继承scrapy.Spider类
    name = "yahoo_tw"  # 定义蜘蛛名

    start_urls = [  # 另外一种写法，无需定义start_requests方法
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]

    def parse_start_url(self, response):
        ###
        ###
        formdate = {
            'log': account,
            'pwd': password,
            'rememberme': "forever",
            'wp-submit': "登录",
            'redirect_to': "http://www.haoduofuli.wang/wp-admin/",
            'testcookie': "1"
        }

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'mingyan-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s' % filename)

