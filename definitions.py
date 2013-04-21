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

def nfd(str):
    return unicodedata.normalize('NFD', str)

def _l(c):
    return nfd(c)[0]

def _v(c):
    return nfd(c)[1]

def _t(c):
    return nfd(c)[2]

def _vt(c):
    return nfd(c)[1:]

#######################################################

KO_CHOSUNG_BRAILLE_TBL = {
    _l('가') : BR_DOTS_4,
    _l('까') : BR_KO_SSANG + BR_DOTS_4,
    _l('나') : BR_DOTS_14,
    _l('다') : BR_DOTS_24,
    _l('따') : BR_KO_SSANG + BR_DOTS_24,
    _l('라') : BR_DOTS_5,
    _l('마') : BR_DOTS_15,
    _l('바') : BR_DOTS_45,
    _l('빠') : BR_KO_SSANG + BR_DOTS_45,
    _l('사') : BR_DOTS_6,
    _l('싸') : BR_KO_SSANG + BR_DOTS_6,
    _l('아') : BR_DOTS_1245,
    _l('자') : BR_DOTS_46,
    _l('짜') : BR_KO_SSANG + BR_DOTS_46,
    _l('차') : BR_DOTS_56,
    _l('카') : BR_DOTS_124,
    _l('타') : BR_DOTS_125,
    _l('파') : BR_DOTS_145,
    _l('하') : BR_DOTS_245,
}

KO_JUNGSEONG_BRAILLE_TBL = {
    _v('아') : BR_DOTS_126,
    _v('애') : BR_DOTS_1235,
    _v('야') : BR_DOTS_345,
    _v('얘') : BR_DOTS_345 + BR_DOTS_1235,
    _v('어') : BR_DOTS_234,
    _v('에') : BR_DOTS_1345,
    _v('여') : BR_DOTS_156,
    _v('예') : BR_DOTS_34,
    _v('오') : BR_DOTS_136,
    _v('와') : BR_DOTS_1236,
    _v('왜') : BR_DOTS_1236 + BR_DOTS_1235,
    _v('외') : BR_DOTS_13456,
    _v('요') : BR_DOTS_346,
    _v('우') : BR_DOTS_134,
    _v('워') : BR_DOTS_1234,
    _v('웨') : BR_DOTS_1234 + BR_DOTS_1235,
    _v('위') : BR_DOTS_134 + BR_DOTS_1235,
    _v('유') : BR_DOTS_146,
    _v('으') : BR_DOTS_246,
    _v('의') : BR_DOTS_2456,
    _v('이') : BR_DOTS_135,
}

KO_JONGSEONG_BRAILLE_TBL = {
    _t('악') : BR_DOTS_1,
    _t('앆') : BR_DOTS_1 + BR_DOTS_1,
    _t('앇') : BR_DOTS_1 + BR_DOTS_3,
    _t('안') : BR_DOTS_25,
    _t('앉') : BR_DOTS_25 + BR_DOTS_13,
    _t('않') : BR_DOTS_25 + BR_DOTS_356,
    _t('앋') : BR_DOTS_35,
    _t('알') : BR_DOTS_2,
    _t('앍') : BR_DOTS_2 + BR_DOTS_1,
    _t('앎') : BR_DOTS_2 + BR_DOTS_26,
    _t('앏') : BR_DOTS_2 + BR_DOTS_12,
    _t('앐') : BR_DOTS_2 + BR_DOTS_3,
    _t('앑') : BR_DOTS_2 + BR_DOTS_236,
    _t('앒') : BR_DOTS_2 + BR_DOTS_256,
    _t('앓') : BR_DOTS_2 + BR_DOTS_356,
    _t('암') : BR_DOTS_26,
    _t('압') : BR_DOTS_12,
    _t('앖') : BR_DOTS_12 + BR_DOTS_3,
    _t('앗') : BR_DOTS_3,
    _t('았') : BR_DOTS_34,
    _t('앙') : BR_DOTS_2356,
    _t('앚') : BR_DOTS_13,
    _t('앛') : BR_DOTS_23,
    _t('앜') : BR_DOTS_235,
    _t('앝') : BR_DOTS_236,
    _t('앞') : BR_DOTS_256,
    _t('앟') : BR_DOTS_356,
}

JAMO_TBL = KO_CHOSUNG_BRAILLE_TBL.copy()
JAMO_TBL.update(KO_JUNGSEONG_BRAILLE_TBL)
JAMO_TBL.update(KO_JONGSEONG_BRAILLE_TBL)

SIMPLE_TR_TBL = JAMO_TBL.copy()
# 초성 ㅇ생략
SIMPLE_TR_TBL[_l('아')] = ''


# MARK 바꾸자
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

##################################################3

# 종성이 포함된 약자 처리를 위해서
KO_JONGSEONG_DIVIDE_TBL = {
    _t('앆') : _t('악') + _t('악'),
    _t('앇') : _t('악') + _t('앗'),
    _t('앉') : _t('안') + _t('앚'),
    _t('않') : _t('안') + _t('앟'),
    _t('앍') : _t('알') + _t('악'),
    _t('앎') : _t('알') + _t('암'),
    _t('앏') : _t('알') + _t('압'),
    _t('앐') : _t('알') + _t('앗'),
    _t('앑') : _t('알') + _t('앝'),
    _t('앒') : _t('알') + _t('앞'),
    _t('앓') : _t('알') + _t('앟'),
    _t('앖') : _t('압') + _t('앗'),
    # 종성 ㅆ은 따로 약자가 있고 연계된 약자가 없기 때문에 변환 하지 않음
}
    
###################
    
ABBREV_WORDS = [
    (re.compile('\\b그래서'), BR_DOTS_1 + BR_DOTS_234),
    (re.compile('\\b그러나'), BR_DOTS_1 + BR_DOTS_14),
    (re.compile('\\b그러면'), BR_DOTS_1 + BR_DOTS_25),
    (re.compile('\\b그러므로'), BR_DOTS_1 + BR_DOTS_26),
    (re.compile('\\b그런데'), BR_DOTS_1 + BR_DOTS_1345),
    (re.compile('\\b그리고'), BR_DOTS_1 + BR_DOTS_136),
    (re.compile('\\b그리하여'), BR_DOTS_1 + BR_DOTS_156),
    # 6절 12항 중
    (re.compile('것'), BR_DOTS_456 + BR_DOTS_234),
    # 6절 14항 중
    (re.compile('껏'), BR_KO_SSANG + BR_DOTS_456 + BR_DOTS_234),
    # 6절 16항
    (re.compile('성'), JAMO_TBL[_l('성')] + BR_DOTS_12456),
    (re.compile('썽'), JAMO_TBL[_l('썽')] + BR_DOTS_12456),
    (re.compile('정'), JAMO_TBL[_l('정')] + BR_DOTS_12456),
    (re.compile('쩡'), JAMO_TBL[_l('쩡')] + BR_DOTS_12456),
    (re.compile('청'), JAMO_TBL[_l('청')] + BR_DOTS_12456),
    # 6절 17항 붙임
    (re.compile('팠'),
     JAMO_TBL[_l('팠')] + JAMO_TBL[_v('팠')] + JAMO_TBL[_t('팠')]),
    
]

V_CLASS = '[' + ''.join([chr(c) for c in range(V_START, V_END + 1)]) + ']'
T_CLASS = '[' + ''.join([chr(c) for c in range(T_START, T_END + 1)]) + ']'

PRE_AE_V = '[' + _v('야') + _v('와') + _v('우') + _v('워')  + ']'

def _ext_re(ext, str):
    return '(?' + ext + str + ')'

# Positive lookbehind assertion
def _lookbehind_re(str):
    return _ext_re('<=', str)

# Negative lookahead_assertion
def _neg_re(str):
    return _ext_re('!', str)


ABBREV_JAMO_GROUP = [
    # 5절 10항
    (re.compile(_lookbehind_re(V_CLASS) + nfd('예')),
     BR_KO_CONT + JAMO_TBL[V_YE]),
    # 5절 11항
    (re.compile(_lookbehind_re(PRE_AE_V) + nfd('애')),
     BR_KO_CONT + JAMO_TBL[V_AE]),
    # 6절 12항 가, 사
    (re.compile(nfd('가')), BR_DOTS_1246),
    (re.compile(nfd('사')), BR_DOTS_123),
    # 6절 14항 까, 싸
    (re.compile(nfd('까')), BR_KO_SSANG + BR_DOTS_1246),
    (re.compile(nfd('싸')), BR_KO_SSANG + BR_DOTS_123),
    # 6절 17항
    (re.compile(nfd('나') + _neg_re(_l('아'))), BR_DOTS_14),
    (re.compile(nfd('다') + _neg_re(_l('아'))), BR_DOTS_24),
    (re.compile(nfd('마') + _neg_re(_l('아'))), BR_DOTS_15),
    (re.compile(nfd('바') + _neg_re(_l('아'))), BR_DOTS_45),
    (re.compile(nfd('자') + _neg_re(_l('아'))), BR_DOTS_46),
    (re.compile(nfd('카') + _neg_re(_l('아'))), BR_DOTS_124),
    (re.compile(nfd('타') + _neg_re(_l('아'))), BR_DOTS_125),
    (re.compile(nfd('파') + _neg_re(_l('아'))), BR_DOTS_145),
    (re.compile(nfd('하') + _neg_re(_l('아'))), BR_DOTS_245),
    # 6절 12항 중성 종성
    (re.compile(_vt('억')), BR_DOTS_1456),
    (re.compile(_vt('언')), BR_DOTS_23456),
    (re.compile(_vt('얼')), BR_DOTS_2345),
    (re.compile(_vt('연')), BR_DOTS_16),
    (re.compile(_vt('열')), BR_DOTS_1256),
    (re.compile(_vt('영')), BR_DOTS_12456),
    (re.compile(_vt('옥')), BR_DOTS_1346),
    (re.compile(_vt('온')), BR_DOTS_12356),
    (re.compile(_vt('옹')), BR_DOTS_123456),
    (re.compile(_vt('운')), BR_DOTS_1245),
    (re.compile(_vt('울')), BR_DOTS_12346),
    (re.compile(_vt('은')), BR_DOTS_1356),
    (re.compile(_vt('을')), BR_DOTS_2346),
    (re.compile(_vt('인')), BR_DOTS_12345),
]

    
    
# import sys

# for k,v in ABBREV_JAMO_GROUP.items():
#     print(k.pattern, file=sys.stderr)

