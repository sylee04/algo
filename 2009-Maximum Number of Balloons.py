#1189. Maximum Number of Balloons
#text = "nlaebolko"
#text = "loonbalxballpoon"
#text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"

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

