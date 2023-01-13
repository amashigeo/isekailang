import os
import math
cwd = os.getcwd()

def is_zh (c):
        x = ord (c)
        # Punct & Radicals
        if x >= 0x2e80 and x <= 0x33ff:
                return True
        # Fullwidth Latin Characters
        elif x >= 0xff00 and x <= 0xffef:
                return True
        # CJK Unified Ideographs &
        # CJK Unified Ideographs Extension A
        elif x >= 0x4e00 and x <= 0x9fbb:
                return True
        # CJK Compatibility Ideographs
        elif x >= 0xf900 and x <= 0xfad9:
                return True
        # CJK Unified Ideographs Extension B
        elif x >= 0x20000 and x <= 0x2a6d6:
                return True
        # CJK Compatibility Supplement
        elif x >= 0x2f800 and x <= 0x2fa1d:
                return True
        else:
                return False

#读取音标字典
with open(cwd+"\\dict.txt","r", encoding='UTF-8') as file:
    dict=file.read()
    lin=dict.splitlines()
    init=lin[0]
    vow=lin[1]        
    init=init.split()
    vow=vow.split()
    initlen=len(init)
    vowlen=len(vow)
#读取特定人名地名等
with open(cwd+"\\names.txt","r", encoding='UTF-8') as file:
    names=file.read()
    namelist=names.splitlines()
    for index in range(len(namelist)):
        namelist[index]=namelist[index].split()

outfile=open(cwd+"\\rst.txt","w", encoding='UTF-8')
with open(cwd+"\\tst.txt","r", encoding='UTF-8') as file:   
    for rows in file:   
        #替换特定名词    
        for index in range(len(namelist)):
            rows=rows.replace(namelist[index][0],namelist[index][1])
        #替换中文
        newrow=""
        for index in range(len(rows)):
            c=rows[index]           
            if is_zh(c):
                bt=bytearray(c,"utf-8")
                initnum=int(bt[0])*16+math.floor(int(bt[1])/16)
                vownum=(int(bt[1])%16)*256+int(bt[2])
                initnum=initnum%initlen
                vownum=vownum%vowlen
                c=init[initnum]+vow[vownum]
                if bt==b'\xef\xbc\x8c':
                    c=','
                if bt==b'\xe3\x80\x82':
                    c='.'
                if newrow != '' and newrow[-1] != ' ':
                    newrow=newrow +' '
                newrow=newrow + c+' '
            else:
                newrow=newrow + c
        outfile.write(newrow)
outfile.close()
