Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a= [1,2,3]
a
[1, 2, 3]
b=['사과','배', '딸기']
ㅠ
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ㅠ
NameError: name 'ᅲ' is not defined
b
['사과', '배', '딸기']

a.append(4)
a.append(5)
a
[1, 2, 3, 4, 5]

a.append([6,7])

a
[1, 2, 3, 4, 5, [6, 7]]

len(a)
6

a.extend([8,9])
a
[1, 2, 3, 4, 5, [6, 7], 8, 9]

a. insert(0,100)
a
[100, 1, 2, 3, 4, 5, [6, 7], 8, 9]
a.append(10)
a
[100, 1, 2, 3, 4, 5, [6, 7], 8, 9, 10]
a.pop()
10
a
[100, 1, 2, 3, 4, 5, [6, 7], 8, 9]
b.pop(1)
'배'
b
['사과', '딸기']
del b
b
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b
NameError: name 'b' is not defined
del a[2]
a
[100, 1, 3, 4, 5, [6, 7], 8, 9]

c=[1,4,6,43,5,6,2,223,65]
c.sort()
c.sort(reverse=True)
c.clear()
c
[]
a=[1,2,3,4,5]
a[3:4]='6'
a
[1, 2, 3, '6', 5]
a=[1,2,3,4]
b=a
b
[1, 2, 3, 4]
c=a.copy()

c
[1, 2, 3, 4]
a
[1, 2, 3, 4]
a[0]=1000
a
[1000, 2, 3, 4]
b
[1000, 2, 3, 4]
c
[1, 2, 3, 4]
a is b
True
a=b
a is c
False
a==c
False


for i in range(10):
    print ('안녕하세요!',i)

    
안녕하세요! 0
안녕하세요! 1
안녕하세요! 2
안녕하세요! 3
안녕하세요! 4
안녕하세요! 5
안녕하세요! 6
안녕하세요! 7
안녕하세요! 8
안녕하세요! 9
b= ['사과','c','d','e',''e','e','d']
    
SyntaxError: unterminated string literal (detected at line 1)
b
    
[1000, 2, 3, 4]
b=['사과','c','d','e','e','e','d']
    
b
    
['사과', 'c', 'd', 'e', 'e', 'e', 'd']

for i in b:
    print(i)

    
사과
c
d
e
e
e
d

for idx, value in enumerate(b):
    print(idx,value)

    
0 사과
1 c
2 d
3 e
4 e
5 e
6 d
for idx, value in enumerate(b,start=1):
    print (idx, value)

    
1 사과
2 c
3 d
4 e
5 e
6 e
7 d

for idx, value in enumerate(b):
    print(idx, value)
    if idx > 3:
    print('안녕하세요', value)
    
SyntaxError: expected an indented block after 'if' statement on line 3
for idx, value in enumerate(b):
    print(idx, value)
    if idx > 3:
          print('안녕하세요', value)

    
0 사과
1 c
2 d
3 e
4 e
안녕하세요 e
5 e
안녕하세요 e
6 d
안녕하세요 d


e=[]
    
e
    
[]
e.append(100)
    
e
    
[100]
num = 123
    
num
    
123
f.append(num)
    
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    f.append(num)
NameError: name 'f' is not defined
f=[]
    
f.append(num)
    
f
    
[123]

for idx, value in enmerate(b, start = 1):
    print(idx, value)

    
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    for idx, value in enmerate(b, start = 1):
NameError: name 'enmerate' is not defined. Did you mean: 'enumerate'?
>>> for idx, value in enumerate(b, start = 1):
...     print(idx, value)
... 
...     
1 사과
2 c
3 d
4 e
5 e
6 e
7 d
>>> 
>>> b
...     
['사과', 'c', 'd', 'e', 'e', 'e', 'd']
>>> 
>>> new_app=[]
...     
>>> for idx, value in enumerate(b, start = 1):
...     #print(idx, value)
...     if value=='사과':
...         print (idx, value)
...         new_app.append(value)
... 
...     
1 사과
>>> 
>>> new_app
...     
['사과']
