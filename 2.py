import os

filename = "hightemp.txt"
#10
with open(filename, "r") as f:
    data =f.readlines()
    print("10: "+str(len(data)))
os.system("wc -l hightemp.txt")

#11
with open(filename, "r") as f:
    data =f.readlines()
    data = [line.replace(" ", "\t") for line in data]
    print(">>>11")
    print(str(data))
os.system('cat hightemp.txt |tr " " "\t" ' )

#12
