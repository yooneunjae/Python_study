Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=['a','b','c','d']
a
['a', 'b', 'c', 'd']
a[0]
'a'
a[1]
'b'
a[2]
'c'
a[3]
'd'
a[4]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[4]
IndexError: list index out of range
b=['1','2','3','4']
b
['1', '2', '3', '4']
b[0]
'1'
b[1]
'2'
b[2]
'3'
b[3]
'4'
'4'
'4'
a[0]='aa'
a
['aa', 'b', 'c', 'd']
del a[0]
a
['b', 'c', 'd']
del a[3]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    del a[3]
IndexError: list assignment index out of range
del a[1]
a
['b', 'd']
c=list(range(4,20,3))
c[0:3]
[4, 7, 10]
c
[4, 7, 10, 13, 16, 19]
c[1:2]
[7]
c[3:5]=100,200
c
[4, 7, 10, 100, 200, 19]
c[0:5:2]
[4, 10, 200]
c
[4, 7, 10, 100, 200, 19]
c[::]
[4, 7, 10, 100, 200, 19]
x=list(range(1,20,5))
x[::]
[1, 6, 11, 16]
x[0:2]
[1, 6]
x[0:3]
[1, 6, 11]
e='python'
e[1:4]
'yth'
e[-3:-1]
'ho'
3[1:-1]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    3[1:-1]
TypeError: 'int' object is not subscriptable
e[1:-1]
'ytho'
len(c)
6
c[0:6]
[4, 7, 10, 100, 200, 19]
e[:-1]
'pytho'
e[:-2]
'pyth'
a[1:3]
['d']
a
['b', 'd']
a[1:2]
['d']
a[1:2]='안녕','hi'
a
['b', '안녕', 'hi']
a[1:3] = '안녕하세요'
ㅁ
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
cus = ['abc','서울','abc@gmail.com',1234]
cus
['abc', '서울', 'abc@gmail.com', 1234]
cus_d = {'고객ID' : 'abc','고객주소' : '서울' , '고객번호' : '1234}
         
SyntaxError: unterminated string literal (detected at line 1)
cus_d = {'고객ID' : 'abc','고객주소' : '서울' , '고객번호' : 1234}
         
cus_d
         
{'고객ID': 'abc', '고객주소': '서울', '고객번호': 1234}
cus_d = {'고객ID' : 'yej','고객주소' : '서울' , '고객번호' : 1110}
         
cus_d
         
{'고객ID': 'yej', '고객주소': '서울', '고객번호': 1110}

q=dict(고객='abc',지역='서울')
         
q1=dict([(고객='abc',지역='서울'),(고객='abc',지역='서울')])
         
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
q1=dict([('고객','abc'),('지역','서울')])
         
q
...          
{'고객': 'abc', '지역': '서울'}
>>> q1
...          
{'고객': 'abc', '지역': '서울'}
>>> q2=dict({'고객':'abc'),('지역':'서울'})
...          
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> q2=dict({'고객':'abc','지역':'서울'})
...          
>>> a2
...          
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a2
NameError: name 'a2' is not defined. Did you mean: 'a'?
>>> q2
...          
{'고객': 'abc', '지역': '서울'}
>>> '고객' in q
...          
True
>>> '지역' in q
...          
True
>>> '거주지' in x
...          
False
>>> len(q)
...          
2
