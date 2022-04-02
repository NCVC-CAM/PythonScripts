import sys
import re
import pandas as pd

reg_ignore = re.compile(r'\W')      ## まだ'/'は入れてません
reg_word   = re.compile(r'[A-Z]-*\d+\.*\d*')

## プロセスシートの列をDataFrameで作成
col = ['/','N','G','X','Y','Z','R/I','J','K','F','S','T','M','H/D','L','P','Q']
df = pd.DataFrame(index=[], columns=col)

for line in sys.stdin:
    ## コメント行とかは無視
    if re.match(reg_ignore, line):
        continue
    ## 1ブロックをワードごとに分割
    dic = {}
    wordlist = re.findall(reg_word, line)
    for word in wordlist:
        ## ワードの先頭1文字をキーに各列に文字列を追加
        w = word[:1]
        if w=='R' or w=='I':
            w = 'R/I'
        elif w=='H' or w=='D':
            w = 'H/D'
        dic[w] = dic.get(w) or "" + word
    ## DataFrameに1行追加
    df = df.append(dic, ignore_index=True)

print(df)
df.to_excel('./sample.xlsx', index=False)