import sys
import re
import math

# 直径を指定してください
D=100.0
piD=math.pi*D

reg_ignore = re.compile(r'\W')
str_num    = r'-*\d+\.*\d*'
str_word   = r'([A-XZ]'+str_num+r')*'
str_Yword  = r'Y('+str_num+r')'
reg_match  = re.compile(str_word+str_Yword+str_word)

for line in sys.stdin:
    if re.match(reg_ignore, line):
        print(line, end='')
        continue
    m = re.match(reg_match, line)
    if m:
        Ynum = float(m.group(2))
        deg  = int(360.0*Ynum/piD*1000.0+0.5) / 1000.0
        result = ''
        if m.group(1):
            result = m.group(1)
        result += 'C'+str(deg)
        if m.group(3):
            result += m.group(3)
        print(result)
    else:
        print(line, end='')
