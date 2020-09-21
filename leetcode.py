# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:21:30 2020

@author: hana1602a
"""

#202009


#762. Prime Number of Set Bits in Binary Representation
#https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

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

for j in range(L, R+1):
    binDict[j] = [bin(j), setbitcount(j)]
    if bin(j)[2:].count('1') in primeNumber(R):
        c1 += 1
print('Prime Numbers not more than {} : {}'.format (R, primeNumber(R)))        
print('Prime Number of Set Bits count is {}'.format (c1))
for key in sorted(binDict):
    print('{} -> {} ( {} set bits )'.format (key, binDict[key][0], binDict[key][1]))


#53. Maximum Subarray    
#https://leetcode.com/problems/maximum-subarray/
    
    