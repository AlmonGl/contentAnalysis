import os
import re
import collections
import copy
files = os.listdir("C:/NKR/tmp")
f = open("C:/NKR/tmpRes/sum.txt",'w')
f.close()
count=collections.defaultdict(int)
wordCount=0
for x in files:
    
    f = open("C:/NKR/tmp/"+x,'r')
    old=f.read()
    words=old.split()
    
    
    f.close()
    
    wordCount+=len(words)
    
    for y in words:
        #y=re.sub("[1|2|3|4|5|6|7|8|9|0|,|.|']","",y)
       # y=re.sub("[)]","",y)
       # y=re.sub("[(]","",y)   
       # y=re.sub("[\]","",y)   
       # y=re.sub("["]","",y)   
        y="".join(c for c in y if c.isalpha())  
        y=y.lower()
        if len(y)<3 and y!="мы":
            continue
        if y=="как" or y=="что" or y=="для" or y=="все" or y=="тыс" or y=="чем" or y=="руб" or y=="при": 
            continue
        if y=="проц"  or y=="это"or y=="его" or y=="так" or y=="еще" or y=="тов" or y=="того":
            continue
        if y=="или"  or y=="тем"or y=="млн" or y=="этого" or y=="январе" or y=="которых" or y=="год":
            continue
        if y=="тысяч"  or y=="милл"or y=="году" or y=="корр" or y=="года" or y=="под" or y=="здесь":
            continue
        if y=="правды"  or y=="правда"or y=="только" or y=="годы" or y=="года" or y=="проп" or y=="этой":
            continue
        #for key in count:
            
        #    if len(y)>=5 and len(key)>=4:
        #        if y==key[:-1] or key ==y[:-1] or y[:-1]==key[:-1]:
        #           y=key
                
        count[y]+=1  

f = open("C:/NKR/tmpRes/sum.txt",'w')    
f.write(str(wordCount))  
countNew=collections.defaultdict(int)
for key in count:
    find=0
    for keyN in countNew:
        if len(keyN)>=4 and len(key)>=5:
            if keyN==key[:-1] or key ==keyN[:-1] or keyN[:-1]==key[:-1]:
                countNew[keyN]+=count[key]
                find=1
                break
        if len(keyN)>=6 and len(key)>=6:
            if keyN==key[:-2] or key ==keyN[:-2] or keyN[:-2]==key[:-1]or keyN[:-1]==key[:-2]or keyN[:-2]==key[:-2]:
                countNew[keyN]+=count[key]
                find=1
                break
    if find==0:
   
        countNew[key]=count[key]

count=copy.deepcopy(countNew)

for key in count:
    count[key]=int(count[key]*50000/wordCount)

f.write("\n")
sorted_count=(sorted(count.items(), reverse=True,key=lambda x: x[1]))
count=dict(sorted_count)
lst = list(count.items())
print(lst[0])
for key in count:
        f.write(key)
        f.write(" ")
        f.write(str(count[key]))
        f.write("\n")
f.close()
        #for x1 in f:
         #   if re.search('text',x1):
         #       t=x1
         #       t=re.sub('"text":',' ',t)
         #       t=t.replace(' ','')
         #       t=t[1:-3]
         #       f1.write(t)
          #      f1.write(' ')
       # f1.close()