#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2018-12-23 20:58
# @Author : Leon Chu <ieno_chu@apple.com>

import re
import sys


def list_to_string_comma(items):
    if not isinstance(items, list):
        return
    res = ""
    for x in items:
        res += x + ','
    if len(res) > 1:
        res = res.__getslice__(0, len(res) - 1)
    return res

    # print list_to_string_comma(["aa", 'bb'])


def clean_no_chinese_or_english(raw):
    raw = raw.strip()
    fil = re.compile(u'[^0-9a-zA-Z\u4e00-\u9fa5.，,。？“”]+', re.UNICODE)
    return fil.sub(' ', raw)


def clean_no_chinese_strstr(in_str):
    in_str = str.decode(in_str, 'UTF-8')
    out_str = ''
    for i in range(len(in_str)):
        if is_uchar(in_str[i]):
            out_str = out_str + in_str[i]
    if isinstance(out_str, unicode):
        out_str = unicode.encode(out_str, 'UTF-8')
    return out_str


def clean_no_chinese_ustr(in_str):
    in_str = in_str.strip()
    out_str = ''
    for i in range(len(in_str)):
        if is_uchar(in_str[i]):
            out_str = out_str + in_str[i]
    if isinstance(out_str, unicode):
        out_str = unicode.encode(out_str, 'UTF-8')
    return out_str


def is_uchar(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return False
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return False
    if uchar in ('-', ',', '，', '。', '.', '>', '?', '(', ')', '#', '*', '&'):
        return False
    return False


def clean_no_chinese(str):
    str = re.sub("[A-Za-z0-9\!\%\[\]\,\。\?\!\@\#\$\%\^\&\*\(\)\_]", "", str)
    return str


def is_Contain_non_Chinese(string):
    line = string.decode('utf-8', 'ignore')
    p2 = re.compile(ur'[^\u4e00-\u9fa5]')
    if p2.search(line):
        return True
    else:
        return False
