# -*- coding: utf-8 -*-

import sys
import unicodedata

from definitions import *

def dict_tr(str, dict):
    res = ''
    for c in str:
        if c in dict:
            res += dict[c]
        else:
            res += c
    return res

def decompose(str):
    str = nfd(str)
    return dict_tr(str, KO_JONGSEONG_DIVIDE_TBL)

# (pattern, subst_str) array 의 모든 pattern 을 subst_str 로 대체
# MARK 모든 regex 를 일일이 탐색하는 것은 글쎄...
def sub_all(str, arr):
    for p,s in arr:
        str = p.sub(s, str)
    return str

def to_braille(str):
    # 약어
    str = sub_all(str, ABBREV_WORDS)
    # 자모, 종성 분해
    str = decompose(str)
    # 모음연쇄, 약자
    str = sub_all(str, ABBREV_JAMO_GROUP)

    str = dict_tr(str, SIMPLE_TR_TBL)
    return str
