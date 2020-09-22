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

        
#https://www.codegrepper.com/code-examples/delphi/how+to+find+all+subarrays+of+an+array+python
# Python program to print all  
# sublist from a given list  
# function to generate all the sub lists
#“how to find all subarrays of an array python” Code Answer  
def sub_lists(list1):  #contiguous subarray이다 not 멱집합
    # store all the sublists  
    sublist = [[]] 
    # first loop  
    for i in range(len(list1) + 1): 
        # second loop  
        for j in range(i + 1, len(list1) + 1): 
            # slice the subarray  
            sub = list1[i:j] 
            sublist.append(sub) 
    return sublist 
  
# driver code 
l1 = [1, 2, 3] #[[], [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]] 그럼 [1,3]은 어디에?
#l1 = 'abcd' 
#l1 = [1, 2, 3, 4]
l1 = [-2,-3,4,-1,-2,1,5,-3]
print(sub_lists(l1))      

#https://blog.naver.com/kmh03214/221702095617
#모든 부분집합 구하기(멱집합) - 비트마스킹(Python)|작성자 화닝이
def powerset(s):
	masks = [ 1 << i for i in range(len(s)) ]
	for i in range( 1 << len(s) ):
		yield [ss for ss,mask in zip(s,masks) if mask & i ]

for power in powerset([1,2,3]):
    print(power)

#https://stackoverflow.com/questions/22699625/palindromic-prime-number-in-python
#회문을 상대로 소수인지 판단하므로 시간이 절약
a = 0
b = 500
a += 1
for i in range(a,b):
    y = True
    if(str(i) == str(i)[::-1]):
        if(i>2):
            for a in range(2,i):
                if(i%a==0):
                    y = False
                    break
            if y:
                print(i, end=' ')
#3 5 7 11 101 131 151 181 191 313 353 373 383



      