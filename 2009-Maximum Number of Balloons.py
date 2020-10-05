#1189. Maximum Number of Balloons
#text = "nlaebolko"
#text = "loonbalxballpoon"
text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"

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
print(sol.maxNumberOfBalloons("loonbalxballpoon"))
print(sol.maxNumberOfBalloons(text))
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
##########
def end_of_loop():
    raise StopIteration
text="nlaebolko"
text = "loonbalxballpoon"
text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
list1 = list(text)
stop = 0
cnt0 = 0
cnt = 0
ret = []
for _ in range(len(text)//7):
#    ret += [list1.pop(list1.index(s)) for s in 'balloon' if s in list1]
#    ret += [list1.pop(list1.index(s)) for s in 'balloon' if s in list1 else (lambda s: break if s not in list1)(i)]
    try :
        ret += [list1.pop(list1.index(s)) if s in list1 else end_of_loop() for s in 'balloon']
#        ret += [list1.pop(list1.index(s)) for s in 'balloon' if s in list1 else end_of_loop()]
        cnt0 += 1
    except StopIteration as si:
        cnt += 1
        print(str(si), 'cnt1 :', cnt, cnt0)
print(len(ret)//7)
print(len(ret))
##############

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        def end_of_loop():
            raise StopIteration
        list1 = list(text)
        ret = []
        for _ in range(len(text)//7):
            try :
                ret += [list1.pop(list1.index(s)) if s in list1 else end_of_loop() for s in 'balloon']
            except StopIteration as si:
                break
        return len(ret)//7

import time
stime = time.time()
sol = Solution()
print(sol.maxNumberOfBalloons("nlaebolko"))
print(sol.maxNumberOfBalloons("loonbalxballpoon"))
print(sol.maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))
print('elapse time: {:.9f} sec'.format(time.time() - stime))
##################

#def end_of_loop():
#    raise StopIteration
#text="nlaebolko"
#text = "loonbalxballpoon"
#text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
#list1 = list(text)
##stop = 0
#cnt = 0
#ret = []
#try :
#    ret = [[list1.pop(list1.index(s)) if s in list1 else end_of_loop() for s in 'balloon'] for z in range(len(text)//7)]
#except StopIteration as si:
#    cnt += 1
#    print(str(si), 'cnt2 :', cnt)
#print(len(ret))

#datalist=['mytest123orange','dark angle','double69','spartan','broken image 999','2 cup of tea'] 
#filterList=['test','2','x','123','orange']
#print([i for i in datalist if any(j for j in filterList if j in i) ])
#use any() with a generator
#any stops the iterations when the first element is found

#def ret(a):
#    raise StopIteration, str(a)
#target ='c'
#x=['a','b','c','d','e']
#try:
#    [x[i] for i in range(len(x)) if x[i]==target and ret((x[i],i))]
#    print 'Not found'
#except StopIteration as si:
#	print str(si)
#""" Output:
#('c', 2)
#"""