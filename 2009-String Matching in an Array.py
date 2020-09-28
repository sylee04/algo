#1408. String Matching in an Array
#words = ["mass","as","hero","superhero"]
#words = ["leetcode","et","code"]
#words = ["leetcoder","leetcode","od","hamlet","am"]

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

import time
stime = time.time()  
sol = Solution()
print(sol.stringMatching(["mass","as","hero","superhero"]))
print('elapse time: {:.9f} sec'.format(time.time() - stime))
