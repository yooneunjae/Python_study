Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[[10,20],[30,40],[50,60]]
for i in a:
    for j in i:
        print(j,end=' ')
    print()

    
10 20 
30 40 
50 60 

a=[[10,20],[30,40],[50,60]]
a[0][0]
10

a=[]

for i in range(10):
    a.append(i)

a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b=[ i for i in range(10)]

b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[[j for j in range(3)]for i in range(4)]
[[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
[[1]*3 for i in range(4)]
[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
[1]*3
[1, 1, 1]
d=[]
e=[]
for j in range(1):
    for i in range(2):
        print(i)
        d.append(i)
    e.append(d)

    
0
1
d
[0, 1]
e
[[0, 1]]
for i in range(2):
    print(i)
    d.append(i)
    print(d)

    
0
[0, 1, 0]
1
[0, 1, 0, 1]


'Hello, world!'.replace('world!', 'Hello!!')
'Hello, Hello!!'

'Hello, world!'.replace('world!', '안녕하세요!')
'Hello, 안녕하세요!'
'Hello, world!'.replace('world!', '안녕~!')
'Hello, 안녕~!'

text='Hello, world!'
text.replace('world!','안녕하세요!')
'Hello, 안녕하세요!'


'a, b, c, d, e, f, g'.split()
['a,', 'b,', 'c,', 'd,', 'e,', 'f,', 'g']
'a,b,c,d,e,f,g'.split()
['a,b,c,d,e,f,g']
'a,b,c,d,e,f,g'.split(',')
['a', 'b', 'c', 'd', 'e', 'f', 'g']
sp=df['fare'].astype('str')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    sp=df['fare'].astype('str')
NameError: name 'df' is not defined. Did you mean: 'd'?



' '.join(a)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    ' '.join(a)
TypeError: sequence item 0: expected str instance, int found

'python'.upper()
'PYTHON'
'PYTHON'.lower()
'python'

a[0].upper()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a[0].upper()
AttributeError: 'int' object has no attribute 'upper'



>>> 'ppppython'.find('p')
0
>>> 'ppppython'.find('pppp')
0
>>> 'ppppython'.find('ppppython')
0
>>> 'ppppython'.find('n')
8
>>> 
>>> 
>>> 'ppppython'.count('p')
4
>>> 
>>> child_list=[]
>>> for i in child_list:
...     if i == 1:
...         print('있다!')
... 
...         
>>> 
>>> print('철수의 수학 점수는 10점 입니다.')
철수의 수학 점수는 10점 입니다.
>>> print('영희의 수학 점수는 5점 입니다.')
영희의 수학 점수는 5점 입니다.
>>> 
>>> '%s의 점수는 10점 입니다.' %'철수'
'철수의 점수는 10점 입니다.'
>>> 
>>> '%s의 점수는 10점 입니다.' %'영희'
'영희의 점수는 10점 입니다.'
>>> 
