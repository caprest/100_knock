# -*- coding: utf-8 -*-
import numpy
import random
"""
http://www.cl.ecei.tohoku.ac.jp/nlp100/
1st chap
"""
#00
a0 = "stressed"
print("00: "+a0[::-1])

#01
a1 = u"パタトクカシー"
print("01: "+a1[::2])

#02
a2_1 =u"パトカー"
a2_2 =u"タクシー"
a2 =u""
for i,j in zip(a2_1,a2_2):
    a2 = a2+i+j
print("02: "+a2)

#03
a3 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
a3_words = a3.split(" ")
a3_num = [len(i.strip(",.")) for i in a3_words ]
a3_ans = 0
for t,i in enumerate(a3_num):
    a3_ans += int(i) * (10**(-t))
print("03: "+str(a3_ans))

#04
a4 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
a4_words = a4.strip(".,").split(" ")
a4_ind =[1, 5, 6, 7, 8, 9, 15, 16, 19]
a4_list = []
a4_list +=[ [i,a4_words[i-1][0]] for i in a4_ind]
a4_list +=[ [i,a4_words[i-1][0:2]] for i in range(1,len(a4_words)) if i not in a4_ind ]
a4_ans = dict(a4_list)
print("04: "+str(a4_ans))

#05
def ngram(string,n,mode="c"):
    if mode =="c":
        words = [(string[i:i+n],i) for i in range(len(string)-n+1) ]
        ngram_dict ={}
        for word in words:
            if word[0] in ngram_dict:
                ngram_dict[word[0]].append(word[1])
            else:
                ngram_dict[word[0]] = [word[1]]

    elif mode == "w":
        words = string.split(" ")
        dict_words = [(" ".join(words[i:i+n]),i) for i in range(len(words)-n+1)]
        print(dict_words)
        ngram_dict = {}
        for word in dict_words:
            if words[0] in ngram_dict:
                ngram_dict[word[0]].append(word[1])
            else:
                
                ngram_dict[word[0]] =[word[1]]


    return ngram_dict
a5 = "I am an NLPer"
dictionary_c = ngram(a5,2,"c")
dictionary_w = ngram(a5,2,"w")
print(u"05: 文字bi-gram\n"+str(dictionary_c))
print(u"05: 単語bi-gram\n"+str(dictionary_w))


#06
a6_1 = "paraparaparadise"
a6_2 = "paragraph"
dic1=ngram(a6_1,2,"c")
dic2=ngram(a6_2,2,"c")
x = dic1.keys()
y =dic2.keys()
X = set(x)
Y = set(y)

print("X&Y="+str(list(X&Y)))
print("X+Y="+str(list(X|Y)))
print("X-Y="+str(list(X-Y)))
true_string =u"含まれる。"
false_string =u"含まれない。"
tf1 = true_string if "se" in X else false_string
tf2 = true_string if "se" in Y else false_string
print(u"seというbi-gramはXに"+tf1+u"そしてYに"+tf2)


#07
def xyz_string(x,y,z):
    return str(x)+u"時の"+str(y)+u"は"+str(z)
print(xyz_string(12,u"気温",22.4))

#08
def cipher(text):
    cipherlist = [chr(219-ord(char)) if char.islower() else char for char in text]
    ciphertext = "".join(cipherlist)
    return ciphertext
text = "Make America Great Britain Again"
print(text+"を暗号化すると"+cipher(text)+"になり"+"復号化すると"+cipher(cipher(text))+"になる")
#09




