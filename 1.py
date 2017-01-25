# -*- coding: utf-8 -*-
import numpy

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

