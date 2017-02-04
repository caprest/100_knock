# -*- coding: utf-8 -*-

import os
import subprocess

filename = "hightemp.txt"
#10
with open(filename, "r") as f:
    data =f.readlines()
    print("10: hightemp.txtは"+str(len(data))+"行です。")
os.system("wc -l hightemp.txt")
print("\n\n\n\n\n")
#11
with open(filename, "r") as f:
    data =f.readlines()
    data = [line.replace(" ", "\t") for line in data]
    print(">>>11")
    print(str(data))
os.system('cat hightemp.txt |tr " " "\t" ' )
print("\n\n\n\n\n")

#12
with open(filename,"r") as f:
    data = f.readlines()
    data =[line.split("\t") for line in data]
    print(data)
    col1 = [line[0] for line in data]
    col2 = [line[1] for line in data]
    print("12:\n"+"\n".join(col1))
    print("12:\n"+"\n".join(col2))


os.system('cat hightemp.txt | cut -f1 >col1.txt')
os.system('cat hightemp.txt | cut -f2 >col2.txt')
print("\n\n\n\n\n")

#13
with open("col1.txt","r") as f:
    data1 = f.readlines()
with open("col2.txt","r") as f:
    data2 = f.readlines()
data = [col1+"\t"+col2 for col1,col2 in zip(data1,data2)]
print(data)
os.system('paste -d"\t" col1.txt col2.txt')

#14 #15
print ("Plase input the number of output lines.")
N = int(input())
with open(filename,"r") as f:
    data = f.readlines()
print(data[0:N])
os.system('cat hightemp.txt |head -n'+str(N) )
print(data[-N:])
os.system('cat hightemp.txt |tail -n'+str(N) )

#16
print("please input the number of split")
N = int(input())

os.system("LINE=`cat hightemp.txt|wc -l` ; VAR=`expr $LINE / {}` ;cat hightemp.txt|split -l $VAR".format(N))



#17
os.system('cat hightemp.txt | cut -f1 |sort|uniq')

#18
os.system('cat hightemp.txt |LANG=ja_JP.UTF-8 sort -k3')
#19

os.system(' cat hightemp.txt |cut -f1 | LANG=ja_JP.UTF-8 sort |LANG=ja_JP.UTF-8 uniq |sort -k1 -n')
os.system('cat hightemp.txt |cut -f1 | LANG=ja_JP.UTF-8 sort |LANG=ja_JP.UTF-8 uniq -c |sort -k1 -n -r')