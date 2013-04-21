# -*- coding: utf-8 -*-

import sys
import unicodedata

from jamo import *

def decompose(str):
    return unicodedata.normalize('NFD', str)



SIMPLE_KOR_BRAILLE_TBL = {
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
    # L_IEUNG : BR_DOTS_1245,
    L_CIEUC : BR_DOTS_46,
    L_SSANGCIEUC : BR_DOTS_6 + BR_DOTS_46,
    L_CHIEUCH : BR_DOTS_56,
    L_KHIEUKH : BR_DOTS_124,
    L_THIEUTH : BR_DOTS_125,
    L_PHIEUPH : BR_DOTS_145,
    L_HIEUH : BR_DOTS_245,

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
    

    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    # L_ : unicodedata.lookup('BRAILLE PATTERN DOTS-'),
    }

def to_braille(str):
    str = decompose(str)
    res = ''
    for c in str:
        if c in SIMPLE_KOR_BRAILLE_TBL:
            res += SIMPLE_KOR_BRAILLE_TBL[c]
        else:
            res += c
    return res
            
while True:
    line = sys.stdin.readline()
    if not line:
        break
    line = to_braille(line)
    sys.stdout.write(line)
