import os
import re
import xlsxwriter
workbook=xlsxwriter.Workbook("C:/NKR/tmpRes/sum.xlsx")
worksheet=workbook.add_worksheet()
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
func_words = {'INTJ', 'PRCL', 'CONJ', 'PREP', 'NUMR'}
files = os.listdir("C:/NKR/tmp")

year=1
mtrx=[]
for x in files:
    
    f = open("C:/NKR/tmp/"+x,'r')
    old=f.read()
    words=old.split("\n")
    
    for line in words:
        find=0
        y,key=line.split()
        key=int(key)
        z=morph.parse(y)[0]
        
        if z.tag.POS in func_words:
            continue
        
        y=z.normal_form
        for r in mtrx:
            
            if r[0]==y:
                r[year]=int(r[year])
                r[year]+=key
                find=1
                break
           
        if find==0:
            row=[y,0,0,0,0,0,0]
            row[year]=key
            mtrx.append(row)
        
    year+=1
 
x1=0
y1=1  
worksheet.set_column(0,0,25)
worksheet.write(0,0,"Word")
worksheet.write(0,1,1924)
worksheet.write(0,2,1926)
worksheet.write(0,3,1932)
worksheet.write(0,4,1936)
worksheet.write(0,5,1940)
worksheet.write(0,6,1947)
worksheet.write(0,7,"Сумма")
sumX=0
for r in mtrx:      
    r.append(r[1]+r[2]+r[3]+r[4]+r[5]+r[6])
   
        
def srt(e):
    return e[7]
    
mtrx.sort(reverse=True,key=srt)
for r in mtrx:
    for l in r:
        
        worksheet.write(y1,x1,l)
        x1+=1
    x1=0
    y1+=1    
workbook.close()