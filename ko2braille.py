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
def sub_all(str, arr):
    for p,s in arr:
        str = p.sub(s, str)
    return str

def to_braille(str):
    # MARK 모든 regex 를 일일이 탐색하는 것은 글쎄...
    # 약어
    str = sub_all(str, ABBREV_WORDS)
    str = decompose(str)
    # 모음연쇄, 약자
    str = sub_all(str, ABBREV_JAMO_GROUP)

    str = dict_tr(str, SIMPLE_TR_TBL)
    
    # MARK 보기가 힘들어서
    str = '|'.join(str)
    return str
            
while True:
    line = sys.stdin.readline()
    if not line:
        break
    line = to_braille(line)
    sys.stdout.write(line)
