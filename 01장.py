#01-1

#세정수의 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print('최댓값은 %d 입니다.' % maximum)
print('최댓값은 {} 입니다..'.format (maximum))


#print(f'최댓값은 {maximum}입니다.')
#  File "<ipython-input-2-1e35c36865f5>", line 1
#    print(f'최댓값은 {maximum}입니다.')
#                              ^
#SyntaxError: invalid syntax
#C:\Users\hana1602a\Anaconda3>python --version
#Python 3.5.3 :: Anaconda 4.2.0 (32-bit)
# %s : 문자, %d : 정수, %f : 실수
