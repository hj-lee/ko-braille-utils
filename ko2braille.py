# -*- coding: utf-8 -*-

import sys
import unicodedata

from definitions import *

def decompose(str):
    jamo_str = unicodedata.normalize('NFD', str)
    # 더 좋은 방법이 있을 수도 있겠지만, 일단...
    for k, v in KO_JONGSEONG_DIVIDE_TBL.items():
        if jamo_str.find(k) >= 0:
            jamo_str = jamo_str.replace(k,v)
    return jamo_str

def to_braille(str):
    str = decompose(str)
    res = ''
    for c in str:
        if c in SIMPLE_TR_TBL:
            res += SIMPLE_TR_TBL[c]
        else:
            res += c
    return res
            
while True:
    line = sys.stdin.readline()
    if not line:
        break
    line = to_braille(line)
    sys.stdout.write(line)
