import sys

tbl = str.maketrans('XYZ', 'YZX')

for line in sys.stdin:
    dst = line.translate(tbl)
    print(dst, end='')
