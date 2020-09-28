#866. Prime Palindrome
#class Solution:
#    def primePalindrome(self, N: int) -> int:
#        if N == 1 :
#            return 2
#        for i in range(N,1000):
#            if str(i) == str(i)[::-1] :
#                for n in range(2,i):
#                    if i % n == 0 :
#                        break
#                else : 
#                    break        
#        return i
#        
#import time
#stime = time.time()
#sol = Solution()
#print(sol.primePalindrome(102))
#print('elapse time: {:.9f} sec'.format(time.time() - stime)) 


#class Solution:
#    def primePalindrome(self, N: int) -> int:
#        if N in [1,2] :
#            return 2
#        while True:
#            if str(N) == str(N)[::-1] :
##                gen = [ i for i in range(2,N) if i*i <= N]
#                gen = ( i for i in range(2,N) if i*i <= N)
##                for n in range(2,N):
#                for n in gen:
##                    print('a1',n)
#                    if N % n == 0 :
##                        print('a2',n)
##                        print(list(gen))
#                        break
#                else : 
##                    print('b1',n)
#                    break        
#            N += 1  
##        print(list(gen))              
#        return N
#        
#'''Time Limit Exceeded
#Details 
#Last executed input
#9989900        '''
##100030001
##elapse time: 64.073712587 sec


#class Solution:
#    def primePalindrome(self, N: int) -> int:
#        if N in [1,2] :
#            return 2
#        while True:
#            if str(N) == str(N)[::-1] :
#                gen = ( i for i in range(2,N) if i*i <= N)
#                for j in gen:
#                    if N % j == 0 :
#                        break
#                else : 
#                    break        
#            N += 1  
#        return N
#        
#'''Accepted
#Runtime: 32 ms
#
#Time Limit Exceeded
#Details 
#Last executed input
#9989900'''
#
#import time
#stime = time.time()
#sol = Solution()
##print(sol.primePalindrome(9989900))
#print(sol.primePalindrome(102))
#print('elapse time: {:.9f} sec'.format(time.time() - stime)) 

#class Solution:
#    def primePalindrome(self, N: int) -> int:
#        if N in [1,2] :
#            return 2
#        g1 = [2]
#        while True:
#            if str(N) == str(N)[::-1] :
#                g2 = [ i for i in range(2,N) if i*i <= N]
##                for k in range(g1[len(g1)],g2[len(g2)]):
##                    if 
#                for j in g2:
#                    if N % j == 0 :
#                        break
#                else : 
##                    g1.append(N)
#                    break        
#            N += 1  
#        return N,g1,g2
#sol = Solution()
#print(sol.primePalindrome(102))


class Solution:
    def primePalindrome(self, N: int) -> int:
        if N in [1,2] :
            return 2
        while True:
            if N % 2 != 0:
                if str(N) == str(N)[::-1] :
                    gen = ( i for i in range(2,N) if i*i <= N)
                    for j in gen:
                        if N % j == 0 :
                            break
                    else : 
                        break        
            N += 1  
        return N
        
'''Time Limit Exceeded
Details 
Last executed input
9989900

100030001
elapse time: 48.828393936 sec'''
        
import time
stime = time.time()
sol = Solution()
#print(sol.primePalindrome(9989900))
print(sol.primePalindrome(102))
print('elapse time: {:.9f} sec'.format(time.time() - stime)) 


