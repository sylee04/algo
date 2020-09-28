# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:21:30 2020

@author: hana1602a
"""

#for 20200927

if 0 :
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

if 0 :        
    '''53. Maximum Subarray'''
    #https://leetcode.com/problems/maximum-subarray/
    # maximum-subarray algorithms are used on bitmap images to detect the brightest area in an image; 주식
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
    
if 0 :    
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
    
    
            
            
    print('###################################################') 
    
if 0 :      
    #1189. Maximum Number of Balloons
    #text = "nlaebolko"
    #text = "loonbalxballpoon"*5
    #list1 = list(text)
    ##ballist = list('balloon')
    #ret = []
    
    #gen1 = (s for s in 'balloon')
    #for s in gen1:
    #    if s in list(text):
    #        ret.append(s)
    #        list1.remove(s)
    #        print(s)
    #        
    
    
    #gen2 = (s for s in list1)
    #for s in gen2:
    #    if s in ballist:
    #        ballist.remove(s)
    #        print(s)   
    #        ret.append(s)
    
    #for _ in range(len(text)//7):
    #    for s in 'balloon':
    #        if s in list(text):
    #            ret.append(s)
    #            list1.remove(s) 
    #
    #print('count of balloon is {}'.format (len(ret)//7))
    #
    #for k,v in enumerate(ret):
    #    if (k+1) % 7:
    #        print(v, end='')
    #    else :
    #        print(v)
    
    #print('###################################################') 
    #
    ##1189. Maximum Number of Balloons
    #text = "nlaebolko"
    #text = "loonbalxballpoon"*2
    #list1 = list(text)
    #ret = []
    #
    #        
    #for _ in range(len(text)//7):
    #    for s in 'balloon':
    #        if s in list1:
    #            ret.append(s)
    #            list1.remove(s) 
    #
    #print('count of balloon is {}'.format (len(ret)//7))
    #
    #for k, v in enumerate(ret):
    #    if k%7 == 0:
    #        print('%2d' % (k//7+1),v, end='')
    #    elif (k+1) % 7:
    #        print(v, end='')
    #    else :
    #        print(v)
    
  
    #1189. Maximum Number of Balloons
    text = "nlaebolko"
    text = "loonbalxballpoon"
    list1 = list(text)
    ret = []
    
            
    for _ in range(len(text)//7):
        for s in 'balloon':
            if s in list1:
                ret.append(s)
                list1.remove(s) 
    
    print('count of balloon : {}'.format (len(ret)//7))
    
    for k, v in enumerate(ret):
        if k%7 == 0:
            print('%2d' % (k//7+1),v, end='')
        elif (k+1) % 7:
            print(v, end='')
        else :
            print(v)
    print('나머지 : {}'.format (''.join(list1)))

    print('###################################################') 
    '''1408. String Matching in an Array'''
    words = ["mass","as","hero","superhero"]
    words = ["leetcode","et","code"]
    
    subw = []
    for s in words:
        for ss in words:
            if ss != s and ss in s :
                subw.append(ss)
    print(subw)
    
    #1189. Maximum Number of Balloons
    text = "nlaebolko"
    text = "loonbalxballpoon"
    text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    
    list1 = list(text)
    ret = []
    stop = 0
            
    for _ in range(len(text)//7):
        for s in 'balloon':
            if s in list1:
                ret.append(s)
                list1.remove(s)
            else : 
                stop = 1
                break
        if stop :
            break
    
    print('count of balloon : {}'.format (len(ret)//7))
    print()
    for k, v in enumerate(ret):
        if k%7 == 0:
            print('%2d' % (k//7+1),v, end='')
        elif (k+1) % 7:
            print(v, end='')
        else :
            print(v)
    print()        
    print('나머지 : {}'.format (''.join(list1)))
            
            
    #class Solution:
    #    def maxNumberOfBalloons(self, text: str) -> int:
    #        list1 = list(text)
    #        ret = []
    #        for _ in range(len(text)//7):
    #            for s in 'balloon':
    #                if s in list1:
    #                    ret.append(s)
    #                    list1.remove(s)         
    #        return len(ret)//7
    
    class Solution:
        def maxNumberOfBalloons(self, text: str) -> int:
            list1 = list(text)
            ret = []
            stop = 0
            for _ in range(len(text)//7):
                for s in 'balloon':
                    if s in list1:
                        ret.append(s)
                        list1.remove(s)
                    else : 
                        stop = 1
                        break
                if stop :
                    break     
            return len(ret)//7
    
    '''Success
    Details 
    Runtime: 584 ms, faster than 5.65% of Python3 online submissions for Maximum Number of Balloons.
    Memory Usage: 14.3 MB, less than 5.24% of Python3 online submissions for Maximum Number of Balloons.'''
        
    import time
    stime = time.time()
    sol = Solution()
    print(sol.maxNumberOfBalloons("nlaebolko"))
    print('elapse time: {:.9f} sec'.format(time.time() - stime))   
    
    print('###################################################')            
    
if 0 :      
    '''383. Ransom Note'''
    ransomNote = "aa"
    magazine = "aab"
    magList = list(magazine)
    ret = []            
    for s in ransomNote:
        if s in magList:
            ret.append(s)
            magList.remove(s) 
    
    #print(''.join(ret) in ransomNote)
    print(''.join(ret) == ransomNote)

    #print('###################################################')            
    #'''383. Ransom Note'''
    #ransomNote = "aa"
    #magazine = "aab"
    #magList = list(magazine)
    #ret = []            
    #for s in ransomNote:
    #    if s in magList:
    #        ret.append(s)
    #        magList.remove(s) 
    #
    ##print(''.join(ret) in ransomNote)
    #print(''.join(ret) == ransomNote)
    #
    #
    ##383. Ransom Note
    #ransomNote = "aa"
    #magazine = "aab"
    #magList = list(magazine)
    #ret = []            
    #
    #for s in ransomNote:
    #    if s in magazine:
    #        ret.append(s)
    #        magList.remove(s) 
    #
    #print(''.join(ret) == ransomNote)
    
    
    
    #class Solution:
    #    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #        magList = list(magazine)
    #        ret = []
    #        for s in ransomNote:
    #            if s in magazine:
    #                ret.append(s)
    #                magList.remove(s) 
    #        return ''.join(ret) == ransomNote
    #Accepted
    #Runtime: 40 ms
    
    class Solution:
        def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            magList = list(magazine)
            ret = []
            for s in ransomNote:
                if s in magList:
                    ret.append(s)
                    magList.remove(s) 
            return ''.join(ret) == ransomNote
    
    
    '''Success
    Details 
    Runtime: 120 ms, faster than 12.87% of Python3 online submissions for Ransom Note.
    Memory Usage: 14.5 MB, less than 5.06% of Python3 online submissions for Ransom Note.'''

    print('###################################################') 
    
if 0 :      
    #1408. String Matching in an Array
    #words = ["mass","as","hero","superhero"]
    #words = ["leetcode","et","code"]
    #words = ["leetcoder","leetcode","od","hamlet","am"]
    #subw = []
    #
    #for s in words:
    #    for ss in words:
    #        if ss != s and ss in s :
    #            subw.append(ss)
    #print(list(set(subw)))
    
    
    #Accepted
    #Runtime: 32 ms
    #
    #
    #class Solution:
    #    def stringMatching(self, words: List[str]) -> List[str]:
    #        subw = []
    #        for s in words:
    #            for ss in words:
    #                if ss != s and ss in s :
    #                    subw.append(ss)        
    #        return subw
        
    import time
    
    class Solution:
        #def stringMatching(self, words: List[str]) -> List[str]: #NameError: name 'List' is not defined
        def stringMatching(self, words):
            subw = []
            for s in words:
                for ss in words:
                    if ss != s and ss in s :
                        subw.append(ss)        
            return list(set(subw))
    
    '''Success
    Details 
    Runtime: 40 ms, faster than 63.08% of Python3 online submissions for String Matching in an Array.
    Memory Usage: 14 MB, less than 27.48% of Python3 online submissions for String Matching in an Array.'''
    
    stime = time.time()  
    sol = Solution()
    print(sol.stringMatching(["mass","as","hero","superhero"]))
    print('elapse time: {:.9f} sec'.format(time.time() - stime))
    
    
    print('###################################################') 

 








   