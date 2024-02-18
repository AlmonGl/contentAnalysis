import os
import re

files = os.listdir("C:/NKR/tmp")

for x in files:
    
    f = open("C:/NKR/tmp/"+x,'r')
    old=f.read()
    
    new=old.replace("-  ","")
    new=new.replace("- ","")
    new=new.replace('textDetection" ',"")
    f.close()
    f = open("C:/NKR/tmp/"+x,'w')
    f.write(new)
        
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