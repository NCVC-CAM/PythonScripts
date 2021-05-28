import sys
import re

reg_ignore = re.compile(r'\W')
reg_word   = re.compile(r'[A-Z]-*\d+\.*\d*')

for line in sys.stdin:
    if re.match(reg_ignore, line):
        print(line, end='')
        continue
    wordlist = re.findall(reg_word, line)
    for w in wordlist:
        print(w, end=' ')
    print('')