# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:39:12 2020

@author: hana1602a
"""

#202009
if 0:
    #762. Prime Number of Set Bits in Binary Representation
    #https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
    #https://www.tutorialspoint.com/prime-number-of-set-bits-in-binary-representation-in-python
    class Solution:
       def countPrimeSetBits(self, L, R):
          def popcount(i):
             return bin(i)[2:].count('1')
          count = 0
          for j in range(L,R+1):
             if popcount(j) in [2,3,5,7,11,13,17,19]:
                count +=1
          return count
          
    L, R = 6, 10      
    ob = Solution()
    print(ob.countPrimeSetBits(L,R))
    
    print('{} to {}'.format (bin(L), bin(R)))
    
    
    
    def countPrimeSetBits(L, R):
        def popcount(i):
            return bin(i)[2:].count('1')
        count = 0
        for j in range(L,R+1):
            if popcount(j) in [2,3,5,7,11,13,17,19]:
                count +=1
        return count
    
    
    def primeNumber(n):
        pl = []
        for i in range(2, n+1):
            for j in range(2, i):
                if i % j == 0 :
                    break
            else : pl.append(i)
        return pl
            
    print(primeNumber(50))        

    print('###################################################')

def primeNumber(n): # Prime Numbers : n or less; n이하
    pl = [2]
    for i in range(3, n+1):
        for j in range(2, i):
            if i % j == 0 :
                break
        else : pl.append(i)
    return pl
                
L, R = 6, 10  
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
    





      