import sys
import os
import re
import pandas as pd
import openpyxl

## 使い方
## python procsheet.py sample.ncd [sample.xlsx]
## 最後の出力ファイル名は省略可．省略すると 入力ファイル.xlsx で出力されます

## 引数処理
inFile=sys.argv[1]
outFile=os.path.splitext(sys.argv[2 if len(sys.argv)>2 else 1])[0]+'.xlsx'
print(outFile)

## 無視する行とワード処理する正規表現
reg_ignore = re.compile(r'^(%|\()')
reg_word   = re.compile(r'[A-Z/]-?\d*\.?\d*')

## プロセスシートの列をDataFrameで作成
col = ['/','N','G','X','Y','Z','R/I','J','K','F','S','T','M','H/D','L','P','Q']
df = pd.DataFrame(index=[], columns=col)

## 1行（ブロック）ずつ処理
with open(inFile) as f:
    for line in f:
        ## コメント行は無視
        if re.match(reg_ignore, line):
            continue
        ## ブロックをワードごとに分割
        dic = {}
        wordlist = re.findall(reg_word, line)
        for word in wordlist:
            ## ワードの先頭1文字をキーに各列に文字列を追加
            w = word[:1]
            if w=='R' or w=='I':
                w = 'R/I'
            elif w=='H' or w=='D':
                w = 'H/D'
            dic[w] = (dic.get(w) or '') + word
        ## DataFrameに1行追加
        df = df.append(dic, ignore_index=True)

#print(df)
df.to_excel(outFile, index=False, startrow=4)   ## 4行空けて出力

## openpyxlを用いてセルの飾り付け
wb = openpyxl.load_workbook(outFile)
ws = wb.active
ws['A1'] = '名称'
ws['A3'] = 'プログラム番号'
ws['E1'] = '注釈'
ws['N1'] = '日付'
ws['N3'] = '作成者'

wb.save(outFile)
