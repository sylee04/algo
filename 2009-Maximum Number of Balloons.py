#1189. Maximum Number of Balloons
text = "nlaebolko"
text = "loonbalxballpoon"*2
list1 = list(text)
ret = []

        
for _ in range(len(text)//7):
    for s in 'balloon':
        if s in list1:
            ret.append(s)
            list1.remove(s) 

print('count of balloon is {}'.format (len(ret)//7))

for k, v in enumerate(ret):
    if k%7 == 0:
        print('%2d' % (k//7+1),v, end='')
    elif (k+1) % 7:
        print(v, end='')
    else :
        print(v)
        
        
        