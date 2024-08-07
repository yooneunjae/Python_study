Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def hi(a,b,c):
    print(a)
    print(b)
    print(c)
    print(a+b+c)

    
hi(1,2,3)
1
2
3
6

x=[10,20,30]

hi(*x)
10
20
30
60

hi(*[10,20,30])
10
20
30
60


def hi(*data):
    print(data)

    
hi(1)
(1,)

hi(1,2,3,4,5)
(1, 2, 3, 4, 5)

hi([1,2,3])
([1, 2, 3],)

def hi(*data):
    for i in data:
        print(i)

        
hi([10,20,30])
[10, 20, 30]

hi(*[10,20,30])
10
20
30

def info_bda(name, age, cls):
    print('이름', name)
    print('나이', age)
    print('분반', cls)

    
info_bda('홍길동',20,'Python 문법 기초반')
이름 홍길동
나이 20
분반 Python 문법 기초반

info_bda('윤은재',22,'Python 문법 기초반')
이름 윤은재
나이 22
분반 Python 문법 기초반

x
[10, 20, 30]

x= {'name':'윤은재', 'age':'22', 'cls':'Python 문법기초반'}
x
{'name': '윤은재', 'age': '22', 'cls': 'Python 문법기초반'}

info_bda(**x)
이름 윤은재
나이 22
분반 Python 문법기초반


SyntaxError: multiple statements found while compiling a single statement
info_bda(**x)
이름 윤은재
나이 22
분반 Python 문법기초반

def score(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)


score(10,20,30,40)
10
20
30
40

for i in x:
    if c < i:
        c=i
print(c)
SyntaxError: invalid syntax

def score(*data):
    c = data[0]
    for i in data:
        if c < i:
            c = i
    return c

x= [10,20,30,60,40]

score(*x)
60

def score1(*data):
    return max (data)

print(score(*x))
60

print(score1(*x))
60

y=[4425353,345465,234324234,34545467,87599545,5434655]

print(*y)
4425353 345465 234324234 34545467 87599545 5434655

>>> score(*y)
234324234
>>> 
>>> 
>>> def add(x):
...     return x+100
... add(100)
SyntaxError: invalid syntax
>>> 
>>> def add(x):
...     return x+100
... 
>>> add(100)
200
>>> 
>>> add2=lamda x : x+100
SyntaxError: invalid syntax
>>> add2=lambda x : x+100
>>> 
>>> add2(100)
200
>>> 
>>> (lambda x : x+100)(100)
200
>>> 
>>> (lambda x : y=200; x+y)(100)
SyntaxError: invalid syntax
>>> 
>>> y=200
(lambda x : x+y) (100)
300

map(lambda x: x+100,[100,200,300]))
SyntaxError: unmatched ')'
map(lambda x: x+100,[100,200,300])
<map object at 0x00000201CCE49BD0>

list(map(lambda x: x+100,[100,200,300]))
[200, 300, 400]

list(map(str,[100,200,300]))
['100', '200', '300']

list(map(lambda x : x if x>30 else, '이하', x))
SyntaxError: invalid syntax
list(map(lambda x : x if x>30 else '이하', x))
['이하', '이하', '이하', 60, 40]

