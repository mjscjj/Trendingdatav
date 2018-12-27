#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2018-12-23 20:58
# @Author : Leon Chu <ieno_chu@apple.com>

def list_to_string_comma(items):
    if not isinstance(items, list):
        return
    res = ""
    for x in items:
        res += x + ','
    if len(res) > 1:
        res = res.__getslice__(0, len(res) - 1)
    return res


print list_to_string_comma(["aa", 'bb'])
