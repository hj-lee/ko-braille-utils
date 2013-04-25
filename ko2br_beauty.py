# -*- coding: utf-8 -*-

import sys

from ko_braille import *

cnt = 0

while True:
    cnt += 1
    line = sys.stdin.readline()
    if not line:
        break
    sys.stdout.write("%3d %s" % (cnt, line))
    line = to_braille(line)
    line = '|'.join(line)
    line = line.replace(' ', '_')
    sys.stdout.write(line)
