# -*- coding: utf-8 -*-

import sys
import unicodedata

from hj_uni_utils import *

# Braille Pattern
define_unicode_vars(globals(), 0x2800, 0x283f, 'BRAILLE PATTERN ', 'BR_')

KO_CHOSUNG_BRAILLE_TBL = {
    L_KIYEOK : BR_DOTS_4,
    L_SSANGKIYEOK : BR_DOTS_6 + BR_DOTS_4,
    L_NIEUN : BR_DOTS_14,
    L_TIKEUT : BR_DOTS_24,
    L_SSANGTIKEUT : BR_DOTS_6 + BR_DOTS_24,
    L_RIEUL : BR_DOTS_5,
    L_MIEUM : BR_DOTS_15,
    L_PIEUP : BR_DOTS_45,
    L_SSANGPIEUP : BR_DOTS_6 + BR_DOTS_45,
    L_SIOS : BR_DOTS_6,
    L_SSANGSIOS : BR_DOTS_6 + BR_DOTS_6,
    L_IEUNG : BR_DOTS_1245,
    L_CIEUC : BR_DOTS_46,
    L_SSANGCIEUC : BR_DOTS_6 + BR_DOTS_46,
    L_CHIEUCH : BR_DOTS_56,
    L_KHIEUKH : BR_DOTS_124,
    L_THIEUTH : BR_DOTS_125,
    L_PHIEUPH : BR_DOTS_145,
    L_HIEUH : BR_DOTS_245,
}

KO_JUNGSEONG_BRAILLE_TBL = {
    V_A : BR_DOTS_126,
    V_AE : BR_DOTS_1235,
    V_YA : BR_DOTS_345,
    V_YAE : BR_DOTS_345 + BR_DOTS_1235,
    V_EO : BR_DOTS_234,
    V_E : BR_DOTS_1345,
    V_YEO : BR_DOTS_156,
    V_YE : BR_DOTS_34,
    V_O : BR_DOTS_136,
    V_WA : BR_DOTS_1236,
    V_WAE : BR_DOTS_1236 + BR_DOTS_1235,
    V_OE : BR_DOTS_13456,
    V_YO : BR_DOTS_346,
    V_U : BR_DOTS_134,
    V_WEO : BR_DOTS_1234,
    V_WE : BR_DOTS_1234 + BR_DOTS_1235,
    V_WI : BR_DOTS_134 + BR_DOTS_1235,
    V_YU : BR_DOTS_146,
    V_EU : BR_DOTS_246,
    V_YI : BR_DOTS_2456,
    V_I : BR_DOTS_135,
}

KO_JONGSEONG_BRAILLE_TBL = {
    T_KIYEOK : BR_DOTS_1,
    T_SSANGKIYEOK : BR_DOTS_1 + BR_DOTS_1,
    T_KIYEOK_SIOS : BR_DOTS_1 + BR_DOTS_3,
    T_NIEUN : BR_DOTS_25,
    T_NIEUN_CIEUC : BR_DOTS_25 + BR_DOTS_13,
    T_NIEUN_HIEUH : BR_DOTS_25 + BR_DOTS_356,
    T_TIKEUT : BR_DOTS_35,
    T_RIEUL : BR_DOTS_2,
    T_RIEUL_KIYEOK : BR_DOTS_2 + BR_DOTS_1,
    T_RIEUL_MIEUM : BR_DOTS_2 + BR_DOTS_26,
    T_RIEUL_PIEUP : BR_DOTS_2 + BR_DOTS_12,
    T_RIEUL_SIOS : BR_DOTS_2 + BR_DOTS_3,
    T_RIEUL_THIEUTH : BR_DOTS_2 + BR_DOTS_236,
    T_RIEUL_PHIEUPH : BR_DOTS_2 + BR_DOTS_256,
    T_RIEUL_HIEUH : BR_DOTS_2 + BR_DOTS_356,
    T_MIEUM : BR_DOTS_26,
    T_PIEUP : BR_DOTS_12,
    T_PIEUP_SIOS : BR_DOTS_12 + BR_DOTS_3,
    T_SIOS : BR_DOTS_3,
    T_SSANGSIOS : BR_DOTS_34,
    T_IEUNG : BR_DOTS_2356,
    T_CIEUC : BR_DOTS_13,
    T_CHIEUCH : BR_DOTS_23,
    T_KHIEUKH : BR_DOTS_235,
    T_THIEUTH : BR_DOTS_236,
    T_PHIEUPH : BR_DOTS_256,
    T_HIEUH : BR_DOTS_356,
}

JAMO_TBL = KO_CHOSUNG_BRAILLE_TBL.copy()
JAMO_TBL.update(KO_JUNGSEONG_BRAILLE_TBL)
JAMO_TBL.update(KO_JONGSEONG_BRAILLE_TBL)

SIMPLE_TR_TBL = JAMO_TBL.copy()
SIMPLE_TR_TBL[L_IEUNG] = ''

# 온표
BR_KO_WHOLE = BR_DOTS_123456

# 붙임표
BR_KR_CONT = BR_DOTS_36

# Hangul Compatibility Jamo 를 Hangul Jamo 로
# Hangul Compatibility Jamo 에는 초성과 종성의 구분이 없다
def add_compat_to_tr_tbl(c):
    name = unicodedata.name(c)
    letter_name = name.replace('HANGUL LETTER ', '').replace('-', '_')
    dic = globals()
    names = map(lambda p: p + letter_name ,['L_', 'V_', 'T_'])
    for name in names:
        if (name in globals()):
            jamo_c = globals()[name]
            SIMPLE_TR_TBL[c] = BR_KO_WHOLE + JAMO_TBL[jamo_c]
            break

for code in range(0x3131, 0x318e + 1):
    add_compat_to_tr_tbl(chr(code))

###################    
    
def decompose(str):
    return unicodedata.normalize('NFD', str)

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
