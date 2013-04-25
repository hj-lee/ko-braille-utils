# -*- coding: utf-8 -*-

import unicodedata
import re

def br(dots):
    dots = str(dots)
    c = unicodedata.lookup('BRAILLE PATTERN DOTS-' + dots)
    return c

def nfd(str):
    return unicodedata.normalize('NFD', str)

def l(c):
    return nfd(c)[0]

def v(c):
    return nfd(c)[1]

def t(c):
    return nfd(c)[2]

def vt(c):
    return nfd(c)[1:]

# Extended regex
def ext_re(ext, str):
    return '(?' + ext + str + ')'

# Positive lookbehind assertion
def lookbehind_re(str):
    return ext_re('<=', str)

# Negative lookahead_assertion
def neg_lookahead_re(str):
    return ext_re('!', str)

