Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9

c=[]
for i in range(10):
    c.append(i)

    
c
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

d=[i+10 for i in range(10)]
d
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

d=[i for i in range(10) if i % 2 == 0)]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
d=[i for i in range(10) if i % 2 == 0]

d
[0, 2, 4, 6, 8]

for i in range(10):
    if i % 2 == 0:
        print(i)

        
0
2
4
6
8
[i for i in range(3)]
[0, 1, 2]

[i for i in range(10) if i % 2 == 0 for j in range(20) j % 2 == 0 ]
SyntaxError: invalid syntax
[i for i in range(10) if i % 2 == 0 for j in range(20) if j % 2 == 0 ]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]


a= ['1','2','3','4']
b=[1,2,3,4]
a=
SyntaxError: invalid syntax
a
['1', '2', '3', '4']

for i in a:
    print(type(i))

    
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>

for i in b:
    print(type(i))

    
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>

c=['사과', '딸기','바나나','키위']
for i in c:
    print(i)

    
사과
딸기
바나나
키위
len(c)
4
for i in range len(c)):
    
SyntaxError: unmatched ')'
for i in range (len(c)):
    print(i)

    
0
1
2
3

for i in range(4):
    print(i)

    
0
1
2
3
for i in a:
    print(i)

    
1
2
3
4

for i in range(len(a)):
    print(i,a[i])

    
0 1
1 2
2 3
3 4

for i in range(len(a)):
    a[i] = int(a[i])

    
for i in a:
    print(type(i))

    
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
b=[list(a[i]) for i in range(len(a))]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    b=[list(a[i]) for i in range(len(a))]
TypeError: 'int' object is not iterable
b=[int(a[i]) for i in range(len(a))]

b
[1, 2, 3, 4]

list(map(int,a))
[1, 2, 3, 4]
c=map(int, input().split())

list(c)
[]


df= [['아이폰','삼성폰'],['애플','삼성전자']]
df
[['아이폰', '삼성폰'], ['애플', '삼성전자']]
df_1=[['아이폰','삼성폰','애플','삼성전자']
      df_1
      
SyntaxError: '[' was never closed
df_1=['아이폰','삼성폰','애플','삼성전자']
      
df_1
      
['아이폰', '삼성폰', '애플', '삼성전자']

df_1[0]
      
'아이폰'
df[0][0]
      
'아이폰'

df_1[3]
      
'삼성전자'
df[0][3]
      
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    df[0][3]
IndexError: list index out of range
df[0][2]
      
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    df[0][2]
IndexError: list index out of range
df[1][1]
      
'삼성전자'

matrix=np.array([['아이폰','삼성폰'],['애플','삼성전자']])
      
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    matrix=np.array([['아이폰','삼성폰'],['애플','삼성전자']])
NameError: name 'np' is not defined
import numpy as np
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> df[0][1]='아이팟'
>>> ㅇㄹ
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    ㅇㄹ
NameError: name 'ᄋᄅ' is not defined
>>> df
[['아이폰', '아이팟'], ['애플', '삼성전자']]
>>> df[0]
['아이폰', '아이팟']
>>> df[0]
['아이폰', '아이팟']
>>> df[0]='아이팟'
>>> 
>>> df[0][0]
'아'
>>> 
>>> len(df[1][0])
2
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> matrix=np.array([['아이폰','삼성폰'],['애플','삼성전자']])
... 
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    matrix=np.array([['아이폰','삼성폰'],['애플','삼성전자']])
NameError: name 'np' is not defined
