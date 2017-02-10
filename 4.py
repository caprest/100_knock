# -*- coding: utf-8 -*-
import re

#For Windows to print utf-8
import sys
import io # 追加
import os
os.system("chcp 65001")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # 追加
###


#30
f = open("neko.txt.mecab","r",encoding = "utf-8")
text = f.readlines()

def process_parse(parsing_line):
    words = re.split(r"\t|,",parsing_line)
    return {
        "surface":words[0],
        "base":words[7],
        "pos":words[1],
        "pos1":words[2],
    }

word_list = []
sentence_list=[]
for word in text:
    if word=="EOS\n":
        if len(word_list)>0:
            sentence_list.append(word_list)
            word_list =[]
        else:
            pass
    else:
        word_list.append(process_parse(word.strip()))


#31 #32 #33
verb_list=[]
verb_base_list=[]
sahen_list=[]
for sentence in sentence_list:
    for word in sentence:
        if word["pos"] == "動詞":
            verb_list.append(word["surface"])
            verb_base_list.append(word["base"])
        if (word["pos1"] == "サ変接続") & (word["pos"] == "名詞"):
            sahen_list.append(word["surface"]) 
print(verb_list)
print(verb_base_list)
print(sahen_list)