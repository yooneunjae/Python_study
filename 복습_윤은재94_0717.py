Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'우리반 1등은 %s' %'영희'
'우리반 1등은 영희'

name= '철수'

'우리반 1등은 %s' %name
'우리반 1등은 철수'

'우리반 %d등은 영희다.' %1
'우리반 1등은 영희다.'

'우리반 평균은 %f.' %90.8
'우리반 평균은 90.800000.'

'우리반 평균은 %.2f.' %90.8
'우리반 평균은 90.80.'

'우리반 %d등은 %s이다.' %(1, '영희')
'우리반 1등은 영희이다.'

'우리반 %d등은 %s이다.' %('영희',1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    '우리반 %d등은 %s이다.' %('영희',1)
TypeError: %d format: a real number is required, not str


'우리반 1등은 {0}.'.format('영희')
'우리반 1등은 영희.'
'우리반 1등은 {0}다.'.format('영희')
'우리반 1등은 영희다.'
'우리반 1등은 {0}은 영희다.'format(1)
SyntaxError: invalid syntax
'우리반 1등은 {0}은 영희다.'.format(1)
'우리반 1등은 1은 영희다.'
'우리반 {0}은 영희다.'.format(1)
'우리반 1은 영희다.'

'우리반 1등은 {0}다. {0}는 우리반 회장이다. {0}랑 철수는 베프다.'.format('영희')
'우리반 1등은 영희다. 영희는 우리반 회장이다. 영희랑 철수는 베프다.'

'우리반 {2}등은 {0}다. {0}는 우리반 회장이다. {0}랑 {1}는 베프다.'.format('영희','철수',1)
'우리반 1등은 영희다. 영희는 우리반 회장이다. 영희랑 철수는 베프다.'

'{name}은 {name1}와 친구다.'.format(name='영희', name1='철수')
'영희은 철수와 친구다.'

accuary=0.98
precision=0.76
recall=0.57
'A 모델의 정확도는 {acc}'.format(acc=accury)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    'A 모델의 정확도는 {acc}'.format(acc=accury)
NameError: name 'accury' is not defined. Did you mean: 'accuary'?
'A 모델의 정확도는 {acc}'.format(acc=accuary)
'A 모델의 정확도는 0.98'

'우리반 {grade}등은 {name1}다. {name1}는 우리반 회장이다. {name1}랑 {name2}는 베프다.'.format(name1='영희',name2='철수', grade=1)
'우리반 1등은 영희다. 영희는 우리반 회장이다. 영희랑 철수는 베프다.'

x=
SyntaxError: invalid syntax

x={'a':1, 'b':2, 'c':3}
x.setdefault('d')

x
{'a': 1, 'b': 2, 'c': 3, 'd': None}
x.setdefault('e', 5)
5

x.update(d=4)
x
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
x.update(a=100)

x.update(zip(['a','b'],[1000,2000]))

x
{'a': 1000, 'b': 2000, 'c': 3, 'd': 4, 'e': 5}

x.setdefault('f',[1,2,3,4,5])
[1, 2, 3, 4, 5]

x
{'a': 1000, 'b': 2000, 'c': 3, 'd': 4, 'e': 5, 'f': [1, 2, 3, 4, 5]}
x.setdefault('A반 성적',[1,2,3,4,5,6,7,8,9,10])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ㅌ
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    ㅌ
NameError: name 'ᄐ' is not defined
x
{'a': 1000, 'b': 2000, 'c': 3, 'd': 4, 'e': 5, 'f': [1, 2, 3, 4, 5], 'A반 성적': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
A_class=[1,2,3,4,5,6,7,8,9,10]
x.pop('f')
[1, 2, 3, 4, 5]

x
{'a': 1000, 'b': 2000, 'c': 3, 'd': 4, 'e': 5, 'A반 성적': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}


del x['c']
x
{'a': 1000, 'b': 2000, 'd': 4, 'e': 5, 'A반 성적': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
x
{'a': 1000, 'b': 2000, 'd': 4, 'e': 5, 'A반 성적': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

x.update(a=1)
x
{'a': 1, 'b': 2000, 'd': 4, 'e': 5, 'A반 성적': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
x.update(A=1)
z
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    z
NameError: name 'z' is not defined
x
{'a': 1, 'b': 2000, 'd': 4, 'e': 5, 'A반 성적': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'A': 1}

x.popitem()
('A', 1)

x
{'a': 1, 'b': 2000, 'd': 4, 'e': 5, 'A반 성적': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
x.clear()
x
{}

x.get('a')


x.item()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    x.item()
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?



for i in x:
    print(i)

    

x=dict.fromkeys(new_key)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    x=dict.fromkeys(new_key)
NameError: name 'new_key' is not defined
>>> 
>>> 
>>> 
>>> new_key=list(x.key())
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    new_key=list(x.key())
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> new_key=list(x.keys())
>>> new_key[0]='A'
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    new_key[0]='A'
IndexError: list assignment index out of range
>>> new_key
[]
>>> 
>>> 
>>> 
>>> x={'a':1,'b':2,'c':3}
>>> 
>>> for i in x:
...     print(i)
... 
...     
a
b
c
