# 言語処理100本ノック
##概要
http://www.cl.ecei.tohoku.ac.jp/nlp100/
を解いていく
##環境
*Anaconda4.2.0
*MeCab
*Win10 64bit
*Unixコマンドが必要な部分はbash on windowsで。

#Mecab
##win10 64bitでの構築に苦労したのでメモ。
基本は 
https://github.com/buruzaemon/natto/wiki/64-Bit-Windows 　
にのっとってやればできる。
https://kiidax.wordpress.com/2015/10/04/msvc-15%E3%81%A7mecab-python-0-996%E3%82%92%E3%83%93%E3%83%AB%E3%83%89/　　
も参考にした。
インストーラーを使うとき辞書はUTF-8を使った方が良い。（コマンドプロンプトなら出力がバグるが）　
pythonのインターフェースとしては,nattoを使ってやれば十分だった。(今回は使わない)
こちらは
　　　　pip install natto
で入る。

##Mecabの出力について
表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
の順に並ぶ。

