Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=1
print(x==1)
True
if x==1;
SyntaxError: invalid syntax
if x==1:
    print('사이다')

    
사이다

x=3
print(x==1)
False
if x==1:
    print('사이다')

    
x=1
if x==1:
    print('사이다')

    
사이다

a= ['사과','딸기','바나나','치킨']
'치킨' in a
True

if '치킨' in a:
    print('1234')

    
1234
if '파스타' in a:
    print('1234')

    

a[3]=='치킨'
True
if a[3]=='치킨':
    print('1234')

    
1234
a=['사과','딸기','바나나','치킨']
b=['사과','딸기','바나나','치킨']
c='사과','딸기','바나나','파스타']
SyntaxError: unmatched ']'
a=['사과','딸기','바나나','치킨']
b=['사과','딸기','바나나','치킨']
c=['사과','딸기','바나나','파스타']
SyntaxError: multiple statements found while compiling a single statement
print(a,b,c)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(a,b,c)
NameError: name 'c' is not defined
a=['사과','딸기','바나나']
b=['사과','딸기','바나나']
c=['사과','딸기','치킨']
print(a,b,c)
['사과', '딸기', '바나나'] ['사과', '딸기', '바나나'] ['사과', '딸기', '치킨']
print(a[2],b[2],c[2])
바나나 바나나 치킨
a[2]==b[2]
True
a[2]==c[2]
False
if a[2]==b[2]:
    print('123')

    
123
if a[2]==b[2] and a[2]==c[3]:
    print('1234')

    
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    if a[2]==b[2] and a[2]==c[3]:
IndexError: list index out of range
a=[2]==b[2] and a[2]==c[2]

a=[2]==b[2] or a[2]==c[2]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a=[2]==b[2] or a[2]==c[2]
TypeError: 'bool' object is not subscriptable
a[2]==b[2] and a[2]==c[2]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a[2]==b[2] and a[2]==c[2]
TypeError: 'bool' object is not subscriptable
if a[3]==b[3] or a[3]==c[3]:
    print('1234')

    
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    if a[3]==b[3] or a[3]==c[3]:
TypeError: 'bool' object is not subscriptable
if a[2]==b[3] or a[2]==c[2]:
    print('1234')

    
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    if a[2]==b[3] or a[2]==c[2]:
TypeError: 'bool' object is not subscriptable
if a[2]==b[2] or a[2]==c[2]:
    print('1234')

    
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    if a[2]==b[2] or a[2]==c[2]:
TypeError: 'bool' object is not subscriptable


x=1
if x==1:
    print('치킨')

    
치킨
if x==2:
    print('파스타')

    
x=1
if x==1:
    print('치킨')

    
치킨
if x==1:
    print('파스타')

    
파스타

print(x)
1

x=10
if >=15:
    
SyntaxError: invalid syntax
if x>=15:
    print('15이상입니다.')
    if x ==10:
        print('10입니다')

        
if x<15:
    print ('15미만입니다')
    ㅑㄹ ㅌ ==10:
        
SyntaxError: invalid syntax
if x < 15:
    print('15미만')
    if x ==10:
        print('10')

        
15미만
10
if x < 15:
    print('15 미만')
    if x !=10:
        print('10')

        
15 미만
print(x)
10
if x ==10:
    print('사이다')

    
사이다
if x ==15:
    print('사이다')
else:
    print('사이다 빼고 다')

    
사이다 빼고 다
print(x)
10

if x == 15:
    print('x는 15다')
else:
    print('x는 15가 아닌 다른 수다')

    
x는 15가 아닌 다른 수다

if x ==10:
    print('10이다')
else:
    print('10이 아니다')
if x >=10:
    
SyntaxError: invalid syntax
if x >=10:
    print('x는 10보다 크거나 작은 수다')

    
x는 10보다 크거나 작은 수다
else:
    
SyntaxError: invalid syntax
>>> if x>=10:
...     print('x는 10보다 크거나 작은 수다')
... else:
...     print('x는 10보다 작은 수다')
... 
...     
x는 10보다 크거나 작은 수다
>>> 
>>> ㅌ=1
>>> x=1
>>> if x==1:
...     print('사이다')
... else:
...     print('잘못된 번호')
... 
...     
사이다
>>> x=2
>>> if x==1:
...     print('사이다')
... else:
...     print('잘못된 번호')
... if x==2:
...     
SyntaxError: invalid syntax
>>> if x==2:
...     print('콜라')
... 
...     
콜라
