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
#########################################################################
#1189. Maximum Number of Balloons
#text = "nlaebolko"
#text = "loonbalxballpoon"
#text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
if 10 :
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
            return len(ret)
    
    '''Success
    Details 
    Runtime: 584 ms, faster than 5.65% of Python3 online submissions for Maximum Number of Balloons.
    Memory Usage: 14.3 MB, less than 5.24% of Python3 online submissions for Maximum Number of Balloons.'''
        
    import time
    stime = time.time()
    sol = Solution()
    print(sol.maxNumberOfBalloons("nlaebolko"))
    print(sol.maxNumberOfBalloons("loonbalxballpoon"))
    print(sol.maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))
    print('elapse time: {:.9f} sec'.format(time.time() - stime))    

def end_of_loop():
    raise StopIteration
text="nlaebolko"
text = "loonbalxballpoon"
text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
list1 = list(text)
stop = 0
ret = []
for _ in range(len(text)//7):
    ret += [list1.pop(list1.index(s)) for s in 'balloon' if s in list1]
#    ret += [list1.pop(list1.index(s)) if s in list1 else end_of_loop() for s in 'balloon']
print(len(ret)//7)


