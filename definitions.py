# -*- coding: utf-8 -*-

# Global definitions

import unicodedata
import re

from hj_uni_utils import *

# Braille Pattern
define_unicode_vars(globals(), 0x2800, 0x283f, 'BRAILLE PATTERN ', 'BR_')

# 된소리표
BR_KO_SSANG = BR_DOTS_6

# 온표
BR_KO_WHOLE = BR_DOTS_123456

# 붙임표
BR_KO_CONT = BR_DOTS_36


KO_CHOSUNG_BRAILLE_TBL = {
    L_KIYEOK : BR_DOTS_4,
    L_SSANGKIYEOK : BR_KO_SSANG + BR_DOTS_4,
    L_NIEUN : BR_DOTS_14,
    L_TIKEUT : BR_DOTS_24,
    L_SSANGTIKEUT : BR_KO_SSANG + BR_DOTS_24,
    L_RIEUL : BR_DOTS_5,
    L_MIEUM : BR_DOTS_15,
    L_PIEUP : BR_DOTS_45,
    L_SSANGPIEUP : BR_KO_SSANG + BR_DOTS_45,
    L_SIOS : BR_DOTS_6,
    L_SSANGSIOS : BR_KO_SSANG + BR_DOTS_6,
    L_IEUNG : BR_DOTS_1245,
    L_CIEUC : BR_DOTS_46,
    L_SSANGCIEUC : BR_KO_SSANG + BR_DOTS_46,
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

# Hangul Compatibility Jamo 를 단독 자모로 처리
# Hangul Compatibility Jamo 에는 초성과 종성의 구분이 없다
def _add_compat_to_tr_tbl(c):
    name = unicodedata.name(c)
    letter_name = name.replace('HANGUL LETTER ', '').replace('-', '_')
    dic = globals()
    names = map(lambda p: p + letter_name ,['L_', 'V_', 'T_'])
    for name in names:
        if (name in globals()):
            jamo_c = globals()[name]
            SIMPLE_TR_TBL[c] = BR_KO_WHOLE + JAMO_TBL[jamo_c]
            break

# 일단 현대 한글 자모가 아닌 전체 자모 전부를 처리
for code in range(0x3131, 0x318e + 1):
    _add_compat_to_tr_tbl(chr(code))

###################

# 종성이 포함된 약자 처리를 위해서
KO_JONGSEONG_DIVIDE_TBL = {
    T_SSANGKIYEOK : T_KIYEOK + T_KIYEOK,
    T_KIYEOK_SIOS : T_KIYEOK + T_SIOS,
    T_NIEUN_CIEUC : T_NIEUN + T_CIEUC,
    T_NIEUN_HIEUH : T_NIEUN + T_HIEUH,
    T_RIEUL_KIYEOK : T_RIEUL + T_KIYEOK,
    T_RIEUL_MIEUM : T_RIEUL + T_MIEUM,
    T_RIEUL_PIEUP : T_RIEUL + T_PIEUP,
    T_RIEUL_SIOS : T_RIEUL + T_SIOS,
    T_RIEUL_THIEUTH : T_RIEUL + T_THIEUTH,
    T_RIEUL_PHIEUPH : T_RIEUL + T_PHIEUPH,
    T_RIEUL_HIEUH : T_RIEUL + T_HIEUH,
    T_PIEUP_SIOS : T_PIEUP + T_SIOS,
    # T_SSANGSIOS 은 따로 약자가 있고 연계된 약자가 없기 때문에 변환 하지 않음
}

ABBREV_WORDS = {
    re.compile('\\b그래서') : BR_DOTS_1 + BR_DOTS_234,
    re.compile('\\b그러나') : BR_DOTS_1 + BR_DOTS_14,
    re.compile('\\b그러면') : BR_DOTS_1 + BR_DOTS_25,
    re.compile('\\b그러므로') : BR_DOTS_1 + BR_DOTS_26,
    re.compile('\\b그런데') : BR_DOTS_1 + BR_DOTS_1345,
    re.compile('\\b그리고') : BR_DOTS_1 + BR_DOTS_136,
    re.compile('\\b그리하여') : BR_DOTS_1 + BR_DOTS_156,
    # 6절 12항 중
    re.compile('것') : BR_DOTS_456 + BR_DOTS_234,
    # 6절 14항 중
    re.compile('껏') : BR_KO_SSANG + BR_DOTS_456 + BR_DOTS_234,
    # 6절 16항
    re.compile('성') : JAMO_TBL[L_SIOS] + BR_DOTS_12456,
    re.compile('썽') : JAMO_TBL[L_SSANGSIOS] + BR_DOTS_12456,
    re.compile('정') : JAMO_TBL[L_CIEUC] + BR_DOTS_12456,
    re.compile('쩡') : JAMO_TBL[L_SSANGCIEUC] + BR_DOTS_12456,
    re.compile('청') : JAMO_TBL[L_CHIEUCH] + BR_DOTS_12456,
}

V_CLASS = '[' + ''.join([chr(c) for c in range(V_START, V_END + 1)]) + ']'
T_CLASS = '[' + ''.join([chr(c) for c in range(T_START, T_END + 1)]) + ']'

PRE_AE_V = '[' + V_YA + V_WA + V_U + V_WEO + ']'

def _ext_re(ext, str):
    return '(?' + ext + str + ')'

# Positive lookbehind assertion
def _lookbehind_re(str):
    return _ext_re('<=', str)

# Negative lookahead_assertion
def _neg_re(str):
    return _ext_re('!', str)


ABBREV_JAMO_GROUP = {
    # 5절 10항
    re.compile(_lookbehind_re(V_CLASS) +
               L_IEUNG + V_YE) : BR_KO_CONT + JAMO_TBL[V_YE],
    # 5절 11항
    re.compile(_lookbehind_re(PRE_AE_V) +
               L_IEUNG + V_AE) : BR_KO_CONT + JAMO_TBL[V_AE],
    
}


# import sys

# for k,v in ABBREV_JAMO_GROUP.items():
#     print(k.pattern, file=sys.stderr)

