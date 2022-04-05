import sys
import os
import re
import pandas as pd

################################################################################
## procssheet.py Ver1.00
################################################################################
## 使い方
## python procsheet.py sample.ncd [sample.xlsx]
## 最後の出力ファイル名は省略可．省略すると 入力ファイル.xlsx で出力されます．
################################################################################

## 引数処理
inFile=sys.argv[1]
outFile=os.path.splitext(sys.argv[2 if len(sys.argv)>2 else 1])[0]+'.xlsx'
#print(outFile)

## 無視する行とワード処理する正規表現
reg_ignore = re.compile(r'^%|\(.*?\)|[\r\n]$')
reg_progno = re.compile(r'O\d+')
reg_word   = re.compile(r'[A-Z/]-?\d*\.?\d*')

## プロセスシートの列をDataFrameで作成
col = ['/','N','G','X','Y','Z','R/I','J','K','F','S','T','M','H/D','L','P','Q']
df = pd.DataFrame(index=[], columns=col)

prog=''

## 1行（ブロック）ずつ処理
with open(inFile) as f:
    for line in f:
        ## 先頭の%とカッコ内のコメントと行末の改行は''に置換
        line = reg_ignore.sub('', line)
        if len(line)==0:
            continue
        print(line)


        ## プログラム番号
#        wordlist = reg_progno.findall(line)
#        for word in wordlist:
#            prog += word + ' '
#        ## ブロックをワードごとに分割
#        dic = {}
#        wordlist = reg_word.findall(line)
#        for word in wordlist:
#            ## ワードの先頭1文字をキーに各列に文字列を追加
#            w = word[:1]
#            if w=='R' or w=='I':
#                w = 'R/I'
#            elif w=='H' or w=='D':
#                w = 'H/D'
#            elif w=='O':
#                continue
#            dic[w] = (dic.get(w) or '') + word
#        ## DataFrameに1行追加
#        df = df.append(dic, ignore_index=True)

#print(df)
#df.to_excel(outFile, index=False, startrow=4)   ## 4行空けて出力
