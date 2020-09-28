#383. Ransom Note
#ransomNote = "aa"
#magazine = "aab"

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

import time
stime = time.time()
sol = Solution()
print(sol.canConstruct("aa","aab"))
print('elapse time: {:.9f} sec'.format(time.time() - stime))
