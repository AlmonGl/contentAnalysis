import os
import re
import copy
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
files = os.listdir("C:/NKR/tmp")
f1 = open("C:/NKR/tmpRes/sumOdd.txt",'w')
f2 = open("C:/NKR/tmpRes/sumEven.txt",'w')
f2.write("тест ")
des=0
func_words = {'INTJ', 'PRCL', 'CONJ', 'PREP', 'NUMR'}
for x in files:
    
    f = open("C:/NKR/tmp/"+x,'r')
    old=f.read()
    words=old.split()
    f.close()
    
    
    for y in words:
        y="".join(c for c in y if c.isalpha())  
        y=y.lower()
        if len(y)<3 and y!="мы":
            continue
        if len(y)<4 and y!="был" and y!="год" and y!="дал":
            continue
        z=morph.parse(y)[0]
        
        if z.tag.POS in func_words:
            continue
        
        y=z.normal_form
        des+=1
        f1.write(y)
        f2.write(y)
        if des%2==0:
            f1.write("\n")
            f2.write(" ")
        else:
            f1.write(" ")
            f2.write("\n")
        
        
f1.close()
f2.close()