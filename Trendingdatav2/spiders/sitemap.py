# #!/usr/bin/env python3
# # encoding:utf-8
# # -*- coding: utf-8 -*-
# # @Time : 2018-12-24 09:22
# # @Author : Leon Chu <ieno_chu@apple.com>
# #使用 parse 处理通过 sitemap 发现的所有 url:
# import sys
# reload(sys)
# sys.setdefaultencoding('UTF-8')
# from scrapy.spiders import CrawlSpider, Rule, Request
# # 配合Rule进行URL规则匹配
# from scrapy.linkextractors import LinkExtractor
#
# class myspider(CrawlSpider):
#     name = 'cqc'
#     allowed_domains = ['cuiqingcai.com']
#     count_all = 0
#     url_all = []
#     start_urls = ['http://cuiqingcai.com']
#     label_tags = ['爬虫', 'scrapy', 'selenium', 'selenium']
#
#     rules = (
#         Rule(LinkExtractor(allow=('*',)), callback='parse_item', follow=True),
#     )
#
#     def parse_item(self, response):
#         print(response.url)
#
#     def parse(self):
#         print 'in'
#
#
