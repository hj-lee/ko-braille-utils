# -*- coding: utf-8 -*-

import sys
import unicodedata

from definitions import *

def decompose(str):
    str = nfd(str)
    res = ''
    for c in str:
        if c in KO_JONGSEONG_DIVIDE_TBL:
            res += KO_JONGSEONG_DIVIDE_TBL[c]
        else:
            res += c
    return res

def to_braille(str):
    # MARK 모든 regex 를 일일이 탐색하는 것은 글쎄...
    # 약어
    for p,s in ABBREV_WORDS:
        str = p.sub(s, str)
        
    str = decompose(str)

    # 모음연쇄, 약자
    for p,s in ABBREV_JAMO_GROUP:
        str = p.sub(s, str)
    
    res = ''
    for c in str:
        if c in SIMPLE_TR_TBL:
            res += SIMPLE_TR_TBL[c]
        else:
            res += c
    # MARK 보기가 힘들어서
    res = '|'.join(res)
    return res
            
while True:
    line = sys.stdin.readline()
    if not line:
        break
    line = to_braille(line)
    sys.stdout.write(line)
