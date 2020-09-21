# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:04:38 2020

@author: hana1602a
"""

#07장

item = 'rin'
st = 'string'


#item = 'ABC'
#st = 'ABABCDEFGHA'
itemlen = len(item)
stlen = len(st)


id = 0

for n in range(stlen):
    id += 1
    if item == st[n:n+itemlen]:
        break
else :
    id = 0
    print('일치하는 문자가 없습니다')

if id :
    print('{}번째 문자가 일치합니다.'.format (id))

print('###################################################')

stList = [st[n:n+itemlen] for n in range(stlen-itemlen+1)]
id1 = 0

if item in st:
    for i in range(len(stList)):
        id1 += 1
        if item == stList[i]:
            break
else :
    id1 = 0
    print('일치하는 문자가 없습니다1')

if id1 :
    print('{}번째 문자가 일치합니다1.'.format (id1))
    
print('###################################################')

id2 = 0

if item in st:
    for n in range(stlen):
        id2 += 1
        if item == st[n:n+itemlen]:
            break
else :
    id2 = 0
    print('일치하는 문자가 없습니다2')

if id2 :
    print('{}번째 문자가 일치합니다2.'.format (id2))

print('###################################################')

stList3len = len([st[n:n+itemlen] for n in range(stlen-itemlen+1)])
stgen3 = (st[n:n+itemlen] for n in range(stlen-itemlen+1))

if item in st:
    for s3 in stgen3:
        if item == s3:
            id3 = stList3len - len(list(stgen3))
            break
else :
    id3 = 0
    print('일치하는 문자가 없습니다3')

if id3 :
    print('{}번째 문자가 일치합니다3.'.format (id3))

print('###################################################')

stList4 = [st[n:n+itemlen] for n in range(stlen-itemlen+1)]
stList4len = len(stList4)

if item in st:
    for _ in range(stList4len):
        if item == stList4.pop(0):
            id4 = stList4len - len(stList4)
            break
else :
    id4 = 0
    print('일치하는 문자가 없습니다4')

if id1 :
    print('{}번째 문자가 일치합니다4.'.format (id4))  
  

print('###################################################')

stList5 = [st[n:n+itemlen] for n in range(stlen-itemlen+1)]
stList5len = len(stList5)

if item in st:
    for _ in range(stList5len):
        if item == stList5.pop():
            id5 = len(stList5)+1
            break
else :
    id5 = 0
    print('일치하는 문자가 없습니다5')

if id5 :
    print('{}번째 문자가 일치합니다5.'.format (id5))  


    