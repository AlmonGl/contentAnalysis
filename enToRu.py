import os
import re

files = os.listdir("C:/NKR/tmp")
dic= {'c':'с','o':'о','p':'р'}
for x in files:
    
    f = open("C:/NKR/tmp/"+x,'r')
    f1=open("C:/NKR/tmp/"+"1"+x,'w')
    old=f.read()
    for y in old:
        if y in dic:
            y=dic[y]
            print(y)
        f1.write(y)
       
f.close()
f1.close()