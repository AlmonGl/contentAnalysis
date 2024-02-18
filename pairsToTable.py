import os
import re
import xlsxwriter
workbook=xlsxwriter.Workbook("C:/NKR/tmpRes/sumPair.xlsx")
worksheet=workbook.add_worksheet()
files = os.listdir("C:/NKR/tmp")

year=2
mtrx=[]
for x in files:
    
    f = open("C:/NKR/tmp/"+x,'r')
    old=f.read()
    f.close()
    words=old.split("\n")
    
    for line in words:
        find=0
        first,second=line.split()
        
        for r in mtrx:
            
            if (r[0][:-2]==first[:-2] and r[1][:-2]==second[:-2]) or (r[1][:-2]==first[:-2] and r[0][:-2]==second[:-2]):
                r[year]+=1                
                find=1
                break
        if find==0:
            row=[first,second,0,0,0,0,0,0]
            row[year]=1
            mtrx.append(row)
        
    year+=1    
        
        
        
        
        
        
        
        
        
x1=0
y1=1  
worksheet.set_column(0,0,25)
worksheet.write(0,0,"Word1")
worksheet.write(0,1,"Word2")
worksheet.write(0,2,1924)
worksheet.write(0,3,1926)
worksheet.write(0,4,1932)
worksheet.write(0,5,1936)
worksheet.write(0,6,1940)
worksheet.write(0,7,1947)
worksheet.write(0,8,"Сумма")

for r in mtrx:      
    r.append(r[2]+r[3]+r[4]+r[5]+r[6]+r[7])
    
    
def srt(e):
    return e[8]
    
mtrx.sort(reverse=True,key=srt)
for r in mtrx:
    for l in r:
        
        worksheet.write(y1,x1,l)
        x1+=1
    x1=0
    y1+=1    
workbook.close()