# -*- coding: utf-8 -*-
import re
import matplotlib.pyplot as plt
import collections
import numpy as np
plt.rcParams['font.family'] = 'MotoyaLMaru'

"""
mecab neko.txt -o neko.txt.mecab
to make neko.txt.mecab
"""
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


#31 #32 #33 #34
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
'''
print(verb_list)
print(verb_base_list)
print(sahen_list)
'''

#35
AsB = []
for sentence in sentence_list:
    words=[]
    for word in sentence:
        if word["pos"] == "名詞":
            words.append(word["surface"])
            if len(words)==3:
                AsB.append("".join(words))
                words = [word["surface"]] #AのBのCも一応考慮
            elif len(words)==2:
                words = []
            else:
                continue
        if len(words)==1:
            if word["surface"] == "の":
                 words.append(word["surface"])
            else:
                words=[]
#print(AsB)

#36 #37
word_list = [word["base"]  for sent in sentence_list for word in sent]
noun_list = [word["base"] 
                for sent in sentence_list
                    for word in sent
                        if (word["pos1"] == "一般") & (word["pos"] == "名詞")
            ]
word_ranking = collections.Counter(word_list).most_common()
word_ranking_10 = collections.Counter(word_list).most_common(10)
noun_ranking_10 = collections.Counter(noun_list).most_common(10)
print(word_ranking_10)
print(noun_ranking_10)
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
def ranking_plot(ranking,ax,title):
    x = np.array([pair[1] for pair in ranking])[::-1]
    y = np.arange(10)
    ax.barh(y,x,align = "center")
    ax.set_yticks(y)
    ax.set_yticklabels([ str(i+1)+": "+pair[0] for i,pair in enumerate(ranking)][::-1])
    ax.set_xlabel("頻度[回]")
    ax.set_ylabel("単語")
    ax.set_title(title)
ranking_plot(word_ranking_10,ax1,"37:ベスト10")
ranking_plot(noun_ranking_10,ax2,"37:ベスト10(名詞)")

#38
print(type(word_ranking[0][1]))
number_word= [word[1] for word in word_ranking]
ax3 = fig.add_subplot(223)
ax3.hist(number_word, bins=10, normed=True)
ax3.set_title('38:ヒストグラム')
ax3.set_xlabel('word')
ax3.set_ylabel('freq')
ax3.set_yscale("log")
ax3.set_ylim(0,0.1)
#39
ax4 = fig.add_subplot(224)
ax4.scatter(np.arange(len(number_word))+1,number_word)
ax4.set_xlabel("順位")
ax4.set_title("39:Zipfの法則")
ax4.set_xscale("log")
ax4.set_yscale("log")
#fig.subplots_adjust(hspace = 0.5)
plt.tight_layout()
plt.show()
