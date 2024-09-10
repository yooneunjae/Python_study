Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[1,2,3,4,5,6,7,8,9,10]

list(map(lambda x: float(x) if x % 2 !=0 else x,a))
[1.0, 2, 3.0, 4, 5.0, 6, 7.0, 8, 9.0, 10]

a=[1,2,3,4,5,6,7,8,9,10]
b=[11,12,13,14,15,16,17,18,19,20]
SyntaxError: multiple statements found while compiling a single statement

a=[1,2,3,4,5,6,7,8,9,10]

b=[11,12,13,14,15,16,17,18,19,20]

list(map(lambda x,y : x*y, a,b))
[11, 24, 39, 56, 75, 96, 119, 144, 171, 200]

list(filter(lambda x: x > 3 and x < 7, a))
[4, 5, 6]

from functools import reduce

def f(x,y)
SyntaxError: expected ':'
def f(x,y):
    return x-y

reduce(f,a)
-53



class bda:
    def hello_bda(self):
        print('bda 9기에 참여했습니다!')

        
bda_9=bda()

bda_9.hello_bda()
bda 9기에 참여했습니다!

type('a')
<class 'str'>

type(1)
<class 'int'>

type('1')
<class 'str'>
type(1.0)
<class 'float'>



class bda:
    def hello_bda(self):
        print('bda 9기에 참여했습니다!')
    def welcome_bda(self):
        print('bda 9기는 8월 10일부터 카톡방을 오픈합니다!')

        
bda_9=bda()

bda_9.welcome_bda()
bda 9기는 8월 10일부터 카톡방을 오픈합니다!



class customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

        
def hi(self):
    print('{0}의 나이는  {1}입니다.' .format(self.name, self.age))

    
cs1=custmoer('데이뱃',1,'데이터베이스')
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    cs1=custmoer('데이뱃',1,'데이터베이스')
NameError: name 'custmoer' is not defined. Did you mean: 'customer'?

cs1.hi()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    cs1.hi()
NameError: name 'cs1' is not defined

class customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def hi(self):
        print('{0}의 나이는  {1}입니다.' .format(self.name, self.age))

        
cs1=custmoer('데이뱃',1,'데이터베이스')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    cs1=custmoer('데이뱃',1,'데이터베이스')
NameError: name 'custmoer' is not defined. Did you mean: 'customer'?
>>> cs1.hi()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    cs1.hi()
NameError: name 'cs1' is not defined
>>> 
>>> 
>>> 
>>> 
>>> re.match('hi','hihihihiihihihihi')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    re.match('hi','hihihihiihihihihi')
NameError: name 're' is not defined. Did you forget to import 're'?
>>> import re
>>> 
>>> re.match('hi','hihihihiihihihihi')
<re.Match object; span=(0, 2), match='hi'>
>>> 
>>> re.match('hi123', 'hihhhihiiihihihhihihihi')
>>> 
>>> re.match('hi', 'hi12345')
<re.Match object; span=(0, 2), match='hi'>
>>> 
>>> 

>>> re.match('[0-9]+','123456')
<re.Match object; span=(0, 6), match='123456'>
>>> 
