import sys
import re

num=1000
add=5
reg_ignore = re.compile(r'[O%\(\n]')

for line in sys.stdin:
    if re.match(reg_ignore, line):
        print(line, end='')
        continue
    print(f'N{num:>04d}'+line, end='')
    num += add
