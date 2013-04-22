# -*- coding: utf-8 -*-

import sys

from ko_braille import *

while True:
    line = sys.stdin.readline()
    if not line:
        break
    sys.stdout.write(line)
    line = to_braille(line)
    line = '|'.join(line)
    line = line.replace(' ', '  ')
    sys.stdout.write(line)
