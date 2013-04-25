# -*- coding: utf-8 -*-

import unicodedata
import re

from utils import *


# 수표
BR_DIGIT = br(3456)

# - 가 마지막에 오도록 한다. character class
DIGIT_MODE_CHARS = "0123456789,.-"
    
DIGIT_MODE_TBL = {
    '0' : br(245),
    '1' : br(1),
    '2' : br(12),
    '3' : br(14),
    '4' : br(145),
    '5' : br(15),
    '6' : br(124),
    '7' : br(1245),
    '8' : br(125),
    '9' : br(24),
    ',' : br(2),
    '-' : br(36),
    '.' : br(3)
}

DIGIT_PATTERN = '[' + DIGIT_MODE_CHARS + ']+'

DIGIT_AMBIGUOUS = '([' + ''.join(DIGIT_MODE_TBL.values()) + \
  l('나') + l('다') + l('마') + l('카') + l('타') + l('파') + l('하') + \
   '])|(' + l('운') + v('운') + t('운') + ')'

DIGIT_NO_SPACE_RE = re.compile(DIGIT_PATTERN
                              + neg_lookahead_re(DIGIT_AMBIGUOUS))
DIGIT_SPACE_RE = re.compile(DIGIT_PATTERN
                            + lookahead_re(DIGIT_AMBIGUOUS))

