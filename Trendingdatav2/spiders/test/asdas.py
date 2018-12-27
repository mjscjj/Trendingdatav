#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>
# def abc(s):
#     if s == 1:
#         return "asd"
#     return
#
#
# if abc(0):
#     print "have"
# else:
#     print "no"
#
# item = "狼王子#27[粵/普]==="
#
# li = ['香港']
# print li



item = '社長作戰室'
item = str.decode(item,'UTF-8')
item = unicode.encode(item,'UTF-8')

print item.replace("粤", "")


print len('你'.encode('UTF-8'))
# print item.index('[')
# idx = item.index('[')
# print item.__getslice__(0, idx)
# print item.__getslice__(0, item.index('#'))
