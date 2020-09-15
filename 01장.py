#01장
if 0 :
    #01-1
    
    #세정수의 최댓값 구하기
    #실습 1-1
    
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
    
    #실습1C-1
    
    print('이름을 입력하세요.: ', end='')
    name = input()
    print('안녕하세요? {} 님.'.format(name))
    
    print(int('17'))    
    print(int('0b110', 2))
    print(int('0o75', 8))
    print(int('13', 10))
    print(int('0x3F', 16))
    print(float('3.14'))
        
    #실습1-2
    #세 정수의 최댓값 구하기
    
    def max3(a,b,c):
        maximum = a
        if b > maximum: maximum=b
        if c > maximum: maximum = c
        return maximum
        
    print('max3(3,2,1) = {}'.format(max3(3,2,1)))
    
    #def gen():
    #    g = list('abcd')+list('fghijk')
    #    for n in g:
    #        yield n
    #for s in gen():
    #    print(s)
    #    if s in ['h']: 
    #        print('broken')
    #        break
    #for s in gen():
    #    print(s)
    #print('*'*10)    
    #gen = gen()    
    #for s in gen:
    #    print(s)
    #    if s in ['h']: 
    #        print('broken')
    #        break
    #for s in gen:
    #    print(s)

    # 실습 1C-2
    #세 정수를 입력받아 중앙값 구하기 1
     
    def med3(a,b,c):
        if a >= b:
            if b >= c:
                return b
            elif a <= c:
                return a
            else :
                return c
        elif a > c:
            return a
        elif b > c:
            return c
        else :
            return b
            
    print('세 정수의 중앙값을 구합니다.')
    a = int(input('정수 a의 값을 입력하세요.: '))
    b = int(input('정수 b의 값을 입력하세요.: '))
    c = int(input('정수 c의 값을 입력하세요.: '))
    
    print('중앙값은 {} 입니다.'.format (med3(a,b,c)))

    #세 정수를 입력받아 중앙값 구하기 2
    
    def med3(a,b,c):
        if (b >= a and c <= a) or (b <= a and c >= a):
            return a
        elif (a > b and c < b) or ( a < b and c > b):
            return b
        return c
        
    print('세 정수의 중앙값을 구합니다..')
    a = int(input('정수 a의 값을 입력하세요.: '))
    b = int(input('정수 b의 값을 입력하세요.: '))
    c = int(input('정수 c의 값을 입력하세요.: '))
    
    print('중앙값은 {} 입니다.'.format (med3(a,b,c)))
        
        
    #a = x if x > y else y
    c = 0
    print('c는 0입니다' if c == 0 else 'c는 0이 아닙니다')        
            
        
        
    #01-2 반복하는 알고리즘
    
    #실습 1-7
    
    # 1부터 n까지 정수의 합 구하기 1(while 문)
    
    print('1부터 n까지 정수의 합을 구합니다.')
    n = int(input('n값을 입력하세요.:'))
    sum = 0
    i = 1
    
    while i <= n:
        sum += i
        i += 1
    
    print('1부터 {}까지 정수의 합은 {}입니다.'.format (n, sum))    
    print('i값은 {}입니다.'.format (i))
            
        
    #실습 1-8
    
    print('1부터 n까지 정수의 합을 구합니다.')
    n = int(input('n값을 입력하세요.:'))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print('1부터 {}까지 정수의 합은 {}입니다.'.format (n, sum))    
    print('i값은 {}입니다.'.format (i))

        
    #실습 1-9
    #a부터 b까지 정수의 합 구하기
    
    print('a부터 b까지 정수의 합 구합니다')    
    a = int(input('정수 a를 입력하세요.:'))
    b = int(input('정수 b를 입력하세요.:'))
    
    if a > b :
        a, b = b, a
    
    sum = 0
    for i in range(a, b+1):
        sum += i
    print('{} 부터 {}까지 정수의 합은 {}입니다.'.format (a,b,sum))    
    
    #실습 1-10    
    #a부터 b까지 정수의 합 구하기
    print('a부터 b까지 정수의 합 구합니다')    
    a = int(input('정수 a를 입력하세요.:'))
    b = int(input('정수 b를 입력하세요.:'))
    
    if a > b :
        a, b = b, a
    
    sum = 0
    for i in range(a, b+1):    
        if i < b :
            print('{} + '.format(i), end='')
        else :
            print('{} = '.format(i), end='')
        sum += i
    print(sum)
            
    
    #실습 1-10    
    #a부터 b까지 정수의 합 구하기
    print('a부터 b까지 정수의 합 구합니다')    
    a = int(input('정수 a를 입력하세요.:'))
    b = int(input('정수 b를 입력하세요.:'))
    
    if a > b :
        a, b = b, a
    
    sum = 0
    for i in range(a, b):     
        print('{} + '.format(i), end='')
        sum += i
        
    print('{} = '.format(b), end='')
    sum += b
    
    print(sum)


    #실습 1-12
    # +와 -를 번갈아 출력하기
    print('+와 -를 번갈아 출력하기')
    n = int(input('몇 개를 출력할까요?:'))
    
    for i in range(n):
        if i % 2 :
            print('-', end='')
        else :
            print('+', end='')
            
    print()
    
    print('+-'*(n//2), end='')
    if n%2: print('+', end='')
    print()
    
    for _ in range(n//2):
        print('+-', end='')
    if n%2: print('+', end='')
    print()
        

#실습 1-14
#*를 n개 출력하되 w개마다 줄바꿈하기

print('*를 n개 출력하되 w개마다 줄바꿈하기')
n = int(input('몇 개를 출력할까요?:'))
w = int(input('몇 개마다 줄바꿈할까요?:'))

for i in range(n):
    print('*',end='')
    if i % w == w -1:
        print()
if i % w != w - 1:
    print()
        
for _ in range(n // w):
    print('*' * w)
print('*' * (n%w))








    
    
    
    
    
    
    
    
    
    
    

