# -*- coding: utf-8 -*-

import sys

from ko_braille import *

while True:
    line = sys.stdin.readline()
    if not line:
        break
    line = to_braille(line)
    # # MARK 보기가 힘들어서
    # line = '|'.join(line)
    sys.stdout.write(line)
