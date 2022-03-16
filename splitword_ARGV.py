import sys
import re

inFile=open(sys.argv[1])
outFile=open(sys.argv[2], "w")

reg_ignore = re.compile(r'\W')
reg_word   = re.compile(r'[A-Z]-*\d+\.*\d*')

for line in inFile.readlines():
    if re.match(reg_ignore, line):
        print(line, end='', file=outFile)
        continue
    wordlist = re.findall(reg_word, line)
    for w in wordlist:
        print(w, end=' ', file=outFile)
    print('', file=outFile)
