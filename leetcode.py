# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:21:30 2020

@author: hana1602a
"""

#for 20200927


'''762. Prime Number of Set Bits in Binary Representation''' # 용도 ?
#https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
#2	3	5	7	11	13	17	19	23	29	31	37	41	43	47	53	59	61	67	71	73	79	83	89	97	101	103	107	109	113	127	131	137	139	149	151	157	163	167	173	179	181	191	193	197	199	211	223	227	229	233	239	241	251	257	263	269	271	277	281
def primeNumber(n): # Prime Numbers : n or less; n이하
    pl = [2]
    for i in range(3, n+1):
        for j in range(2, i):
            if i % j == 0 :
                break
        else : pl.append(i)
    return pl
                
L, R = 10, 15  
c1 = 0
binDict = {}
setbitcount = lambda x : bin(x)[2:].count('1')
primeNumberR = primeNumber(R)

for j in range(L, R+1):
    binDict[j] = [bin(j), setbitcount(j)]
    if bin(j)[2:].count('1') in primeNumberR:
        c1 += 1
print('Prime Numbers not more than {} : {}'.format (R, primeNumberR))        
print('Prime Number of Set Bits count is {}'.format (c1))

for key in sorted(binDict):
    for k in range(2, binDict[key][1]):
        if binDict[key][1] % k == 0 :
            primeOrNot = 'not prime'
            break
    else : 
        primeOrNot = 'prime'
    print('{} -> {} ( {} set bits → {} )'.format (key, binDict[key][0], binDict[key][1], primeOrNot))


print('###################################################')    
    
'''53. Maximum Subarray'''
#https://leetcode.com/problems/maximum-subarray/
# 주식
def sub_lists_sum(list1):  #contiguous subarray이다 not 멱집합
    sublist = [[]] 
    for i in range(len(list1) + 1): 
        # second loop  
        for j in range(i + 1, len(list1) + 1): 
            sub = list1[i:j] 
            sublist.append(sum(sub)) 
    sublist.pop(0) # 첫번째 []공집합 제거해서 max내장함수 오류안나게함
    return sublist 
l1 = [1, 2, 3] # 6 ← [1, 2, 3]
l1 = [-2,1,-3,4,-1,2,1,-5,4] # 6 ← [4, -1, 2, 1]
l1 = [-2,-3,4,-1,-2,1,5,-3] # 7 ← [4, -1, -2, 1, 5]
print(sub_lists_sum(l1)) 
print('maximum is {}'.format (max(sub_lists_sum(l1)))) 

# 어떤 부분집합의 합이 max인지 출력
maxsub = sub_lists_sum(l1)
maxindex = maxsub.index(max(maxsub))
def sub_lists(list1):
    sublist = [[]] 
    for i in range(len(list1) + 1): 
        for j in range(i + 1, len(list1) + 1): 
            sub = list1[i:j] 
            sublist.append(sub) 
    sublist.pop(0)
    return sublist 
print(sub_lists(l1))
print('Maximum Subarray is {}'.format (sub_lists(l1)[maxindex]))

print('###################################################') 


'''866. Prime Palindrome'''
#https://leetcode.com/problems/prime-palindrome/
#3 5 7 11 101 131 151 181 191 313 353 373 383
#Palindromes are used in DNA for marking and permitting cutting
def prime_palindrome_greater_than_N_1(n): # 소수를 먼저구하고 회문인지 판단
    a = n
    palindrome = ''
    #while True :
    for _ in range(1000): # 루프제한설정
        for j in range(2, n):
            if n % j == 0 :
                break
        else : 
            print(n)
            word = str(n)
            for i in range(len(word) // 2): 
                if word[i] != word[-1 - i]:
                    break
            else : 
                palindrome = word
        if palindrome :
            break
        n += 1
    return (a, palindrome)
    
print(prime_palindrome_greater_than_N_1(102))


#회문을 먼저 구하고 소수인지 판단하므로 더 심플함
b = 1000 # 루프제한설정
a = 102
for i in range(a,b):
    if str(i) == str(i)[::-1] :
        for n in range(2,i):
            if i % n == 0 :
                break
        else : 
            print('{} → prime palindrome is {}'.format (a, i))
            break
























   