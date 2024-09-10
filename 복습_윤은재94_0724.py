Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
y={'a','a','b','b','c','d'}
b=['a','a','b','b','c','d']

print(y)
{'c', 'd', 'a', 'b'}
print(b)
['a', 'a', 'b', 'b', 'c', 'd']

a={1,2,3,}
a={1,2,3}
b={3,4,5}
c={5,6,7}

set.union(a,b,c)
{1, 2, 3, 4, 5, 6, 7}

set.intersection(a,b)
{3}
set.intersection(a,c)
set()
set.intersection(b,c)
{5}

a.union(b)
{1, 2, 3, 4, 5}

def hi():
    print('안녕하세요?')
    print('반갑습니다.')
    print('저는 윤은재입니다!')
    print('저의 mbit를 아시나요?')

    
hi()
안녕하세요?
반갑습니다.
저는 윤은재입니다!
저의 mbit를 아시나요?


a='윤은재'
b='mbit'

def hi(a,b):
    print('안녕하세요?')
    print('반갑습니다.')
    print('저는' ,a, '입니다!')
    print('저의' ,b, '를 아시나요?')

    
hi(a,b)
안녕하세요?
반갑습니다.
저는 윤은재 입니다!
저의 mbit 를 아시나요?


a='은재'
b='중간고사 성적'

hi(a,b)
안녕하세요?
반갑습니다.
저는 은재 입니다!
저의 중간고사 성적 를 아시나요?



def cal(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

    
a=5
b=3

cal(a,b)
8
2
15
1.6666666666666667


a=8
b=4

cal(a,b)
12
4
32
2.0

c
{5, 6, 7}

def cal(a,b):
    print(a+b)

    
def cal(a,b):
    return a+b

a=4
b=2
cal(4,2)
6

def cal(a,b):
    c=a+b
    d=a-b
    return c, d

res=cal(a,b)
res
(6, 2)


def add(a,b):
    c=a+b
    return c
def add2(a,b):
    
SyntaxError: invalid syntax


KeyboardInterrupt



def add(a,b)
SyntaxError: expected ':'


def add(a,b):
    c=a+b
    return c

def add2(a,b):
    c=a+c
    d=add(a,b)
    return c+d
a=10
SyntaxError: invalid syntax
b=10
>>> 
>>> 
>>> a=10
>>> b
10
>>> 
>>> add2(a,b)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    add2(a,b)
NameError: name 'add2' is not defined. Did you mean: 'add'?
>>> 
>>> 
>>> def add2(a,b):
...     c=a+c
...     return c
... 
>>> a=10
>>> b=10
>>> 
>>> add2(z,b)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    add2(z,b)
NameError: name 'z' is not defined
>>> add2(a,b)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    add2(a,b)
  File "<pyshell#114>", line 2, in add2
    c=a+c
UnboundLocalError: cannot access local variable 'c' where it is not associated with a value
