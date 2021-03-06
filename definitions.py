# -*- coding: utf-8 -*-

# Global definitions

import unicodedata
import re

from utils import *

# 된소리표
BR_KO_SSANG = br(6)

# 온표
BR_KO_WHOLE = br(123456)

# 붙임표
BR_KO_CONT = br(36)

# 로마자표, 로마자종료표
BR_ROMAN_START = br(356)
BR_ROMAN_END = br(256)

#######################################################

KO_CHOSUNG_BRAILLE_TBL = {
    l('가') : br(4),
    l('까') : BR_KO_SSANG + br(4),
    l('나') : br(14),
    l('다') : br(24),
    l('따') : BR_KO_SSANG + br(24),
    l('라') : br(5),
    l('마') : br(15),
    l('바') : br(45),
    l('빠') : BR_KO_SSANG + br(45),
    l('사') : br(6),
    l('싸') : BR_KO_SSANG + br(6),
    l('아') : br(1245),
    l('자') : br(46),
    l('짜') : BR_KO_SSANG + br(46),
    l('차') : br(56),
    l('카') : br(124),
    l('타') : br(125),
    l('파') : br(145),
    l('하') : br(245),
}

KO_JUNGSEONG_BRAILLE_TBL = {
    v('아') : br(126),
    v('애') : br(1235),
    v('야') : br(345),
    v('얘') : br(345) + br(1235),
    v('어') : br(234),
    v('에') : br(1345),
    v('여') : br(156),
    v('예') : br(34),
    v('오') : br(136),
    v('와') : br(1236),
    v('왜') : br(1236) + br(1235),
    v('외') : br(13456),
    v('요') : br(346),
    v('우') : br(134),
    v('워') : br(1234),
    v('웨') : br(1234) + br(1235),
    v('위') : br(134) + br(1235),
    v('유') : br(146),
    v('으') : br(246),
    v('의') : br(2456),
    v('이') : br(135),
}

KO_JONGSEONG_BRAILLE_TBL = {
    t('악') : br(1),
    t('앆') : br(1) + br(1),
    t('앇') : br(1) + br(3),
    t('안') : br(25),
    t('앉') : br(25) + br(13),
    t('않') : br(25) + br(356),
    t('앋') : br(35),
    t('알') : br(2),
    t('앍') : br(2) + br(1),
    t('앎') : br(2) + br(26),
    t('앏') : br(2) + br(12),
    t('앐') : br(2) + br(3),
    t('앑') : br(2) + br(236),
    t('앒') : br(2) + br(256),
    t('앓') : br(2) + br(356),
    t('암') : br(26),
    t('압') : br(12),
    t('앖') : br(12) + br(3),
    t('앗') : br(3),
    t('았') : br(34),
    t('앙') : br(2356),
    t('앚') : br(13),
    t('앛') : br(23),
    t('앜') : br(235),
    t('앝') : br(236),
    t('앞') : br(256),
    t('앟') : br(356),
}

JAMO_TBL = KO_CHOSUNG_BRAILLE_TBL.copy()
JAMO_TBL.update(KO_JUNGSEONG_BRAILLE_TBL)
JAMO_TBL.update(KO_JONGSEONG_BRAILLE_TBL)
    
KO_SYMBOL_TBL = {
    '.' : br(256),
    '?' : br(236),
    '!' : br(235),
    ',' : br(5),
    # 가웃뎃점
    '·' : br(5) + br(23),
    ':' : br(5) + br(2),
    ';' : br(56) + br(23),
    '/' : br(456) + br(34),
    '“' : br(236),
    '”' : br(356),
    '"' : br(356),
    # 겹낫표들
    '『' : br(236),
    '』' : br(356),
    '`' : br(6) + br(236),
    '\'' : br(356) + br(3),
    # 낫표들 
    '「' : br(6) + br(236),
    '」' : br(356) + br(3),

    # MARK 붙임표 주의
    '(' : br(36),
    ')' : br(36),
    '{' : br(236) + br(23),
    '}' : br(56) + br(356),
    '[' : br(236) + br(3),
    ']' : br(6) + br(356),
    # minus 와 hangul symbol
    '-' : br(36),
    '­' : br(36),
    # 줄표 --
    '―' : br(36) * 2,
    '~' : br(36) * 2,
    '∼' : br(36) * 2,
    # 줄임표 ......
    # '' : br(6) * 3,
    '*' : br(35) * 2,

    ####
    
    # 아포스트로피와 닫는 작은 따옴표 구분 어려움
    # '\'' : br(3),

    # 위와 같음표 ''
    '〃' : br(56) + br(23),

    # 긴 소리표
    'ː' : br(6) + br(3),

    # 화폐 기호들 (with fullwidth)
    '₩' : br(4) + br(2456), # 원
    '￦' : br(4) + br(2456), # 원
    '¢' : br(4) + br(14), # 센트
    '￠': br(4) + br(14), # 센트
    '$' : br(4) + br(145), # 달러
    '＄' : br(4) + br(145), # 달러
    '£' : br(4) + br(123), # 파운드
    '￡' : br(4) + br(123), # 파운드
    '¥' : br(4) + br(13456), # 엔
    '￥' : br(4) + br(13456), # 엔
    unicodedata.lookup('EURO SIGN') : br(4) + br(15), # 유로
}


SIMPLE_TR_TBL = JAMO_TBL.copy()
# 초성 ㅇ생략
SIMPLE_TR_TBL[l('아')] = ''
SIMPLE_TR_TBL.update(KO_SYMBOL_TBL)


# Hangul Compatibility Jamo 를 단독 자모로 처리
# Hangul Compatibility Jamo 에는 초성과 종성의 구분이 없다
def _add_compat_to_tr_tbl(c):
    name = unicodedata.name(c)
    for prefix in ['HANGUL CHOSEONG','HANGUL JUNGSEONG','HANGUL JONGSEONG']:
        letter_name = name.replace('HANGUL LETTER', prefix)
        try:
            jamo_c = unicodedata.lookup(letter_name)
            SIMPLE_TR_TBL[c] = BR_KO_WHOLE + JAMO_TBL[jamo_c]
        except KeyError:
            pass

# 일단 현대 한글 자모가 아닌 전체 자모 전부를 처리
for code in range(0x3131, 0x318e + 1):
    _add_compat_to_tr_tbl(chr(code))

##################################################3

# 종성이 포함된 약자 처리를 위해서
KO_JONGSEONG_DIVIDE_TBL = {
    t('앆') : t('악') + t('악'),
    t('앇') : t('악') + t('앗'),
    t('앉') : t('안') + t('앚'),
    t('않') : t('안') + t('앟'),
    t('앍') : t('알') + t('악'),
    t('앎') : t('알') + t('암'),
    t('앏') : t('알') + t('압'),
    t('앐') : t('알') + t('앗'),
    t('앑') : t('알') + t('앝'),
    t('앒') : t('알') + t('앞'),
    t('앓') : t('알') + t('앟'),
    t('앖') : t('압') + t('앗'),
    # 종성 ㅆ은 따로 약자가 있고 연계된 약자가 없기 때문에 변환 하지 않음
}
    
###################

ABBREV_WORDS = [
    (re.compile('\\b그래서'), br(1) + br(234)),
    (re.compile('\\b그러나'), br(1) + br(14)),
    (re.compile('\\b그러면'), br(1) + br(25)),
    (re.compile('\\b그러므로'), br(1) + br(26)),
    (re.compile('\\b그런데'), br(1) + br(1345)),
    (re.compile('\\b그리고'), br(1) + br(136)),
    (re.compile('\\b그리하여'), br(1) + br(156)),
    # 6절 12항 중
    (re.compile('것'), br(456) + br(234)),
    # 6절 14항 중
    (re.compile('껏'), BR_KO_SSANG + br(456) + br(234)),
    # 6절 16항
    (re.compile('성'), JAMO_TBL[l('성')] + br(12456)),
    (re.compile('썽'), JAMO_TBL[l('썽')] + br(12456)),
    (re.compile('정'), JAMO_TBL[l('정')] + br(12456)),
    (re.compile('쩡'), JAMO_TBL[l('쩡')] + br(12456)),
    (re.compile('청'), JAMO_TBL[l('청')] + br(12456)),
    # 6절 17항 붙임
    (re.compile('팠'),
     JAMO_TBL[l('팠')] + JAMO_TBL[v('팠')] + JAMO_TBL[t('팠')]),
    
]

L_START = 0x1100
L_END = 0x1112
V_START = 0x1161
V_END = 0x1175
T_START = 0x11a8
T_END = 0x11c2
    
V_CLASS = '[' + ''.join([chr(c) for c in range(V_START, V_END + 1)]) + ']'
T_CLASS = '[' + ''.join([chr(c) for c in range(T_START, T_END + 1)]) + ']'

PRE_AE_V = '[' + v('야') + v('와') + v('우') + v('워')  + ']'

ABBREV_JAMO_GROUP = [
    # 5절 10항
    (re.compile(lookbehind_re(V_CLASS) + nfd('예')),
     BR_KO_CONT + JAMO_TBL[v('예')]),
    # 5절 11항
    (re.compile(lookbehind_re(PRE_AE_V) + nfd('애')),
     BR_KO_CONT + JAMO_TBL[v('애')]),
    # 6절 12항 가, 사
    (re.compile(nfd('가')), br(1246)),
    (re.compile(nfd('사')), br(123)),
    # 6절 14항 까, 싸
    (re.compile(nfd('까')), BR_KO_SSANG + br(1246)),
    (re.compile(nfd('싸')), BR_KO_SSANG + br(123)),
    # 6절 12항 중성 종성
    (re.compile(vt('억')), br(1456)),
    (re.compile(vt('언')), br(23456)),
    (re.compile(vt('얼')), br(2345)),
    (re.compile(vt('연')), br(16)),
    (re.compile(vt('열')), br(1256)),
    (re.compile(vt('영')), br(12456)),
    (re.compile(vt('옥')), br(1346)),
    (re.compile(vt('온')), br(12356)),
    (re.compile(vt('옹')), br(123456)),
    (re.compile(vt('운')), br(1245)),
    (re.compile(vt('울')), br(12346)),
    (re.compile(vt('은')), br(1356)),
    (re.compile(vt('을')), br(2346)),
    (re.compile(vt('인')), br(12345)),
]

# 6절 12항, 17항
# 이들의 약자는 첫소리 자음의 점자와 같다
for c in ['나', '다', '마', '바', '자', '카', '타', '파', '하']:
    ABBREV_JAMO_GROUP.append(
        (re.compile(nfd(c) + neg_lookahead_re(l('아'))), JAMO_TBL[l(c)]))
    
