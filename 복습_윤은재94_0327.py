Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
' ' '123' ' '
' 123 '
"""1110"""
'1110'
"1110"
'1110'
'1110'
'1110'
1110
1110
bda='''1110'''
bda
'1110'
ej='''1110'''
ej
'1110'
yej=031110
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
yej=94
yej
94
print(type(ej))
<class 'str'>
print(type(yej))
<class 'int'>
ej = '''1110''', 1110, 11110
ej
('1110', 1110, 11110)
type([1,11,111])
<class 'list'>
[1,11,111,1111,11111]
[1, 11, 111, 1111, 11111]
a=['ej'11'1.11,True]
   
SyntaxError: unterminated string literal (detected at line 1)
a=['ej',11,1.11,True]
   
type (a)
   
<class 'list'>
[1,11]
   
[1, 11]
range(1110)
   
range(0, 1110)
list(range(1110))
   

range (7)
   
range(0, 7)
list(range(7))
   
[0, 1, 2, 3, 4, 5, 6]
list(range(3,15))
   
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list(range(0,99))
   
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]
list(range(3,30,3))
   
[3, 6, 9, 12, 15, 18, 21, 24, 27]
list(range(5,10,-2))
   
[]
list(range(10,5,-2))
   
[10, 8, 6]
[10, 8, 6]
   
[10, 8, 6]
ej = 5, 10, 15
   
ej
   
(5, 10, 15)
tuple(range(5))
   
(0, 1, 2, 3, 4)
list(range(5))
   
[0, 1, 2, 3, 4]
tuple(range(10))
   
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
list(range(10))
   
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tuple(range(10,20))
   
(10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
(10,'10',1.0,True)
   
(10, '10', 1.0, True)
list(range(11))
   
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
['안녕하세요']
   
['안녕하세요']
a=[1,10,100]
   
b=[2,20,200]
   
print(a)
   
[1, 10, 100]
print(b)
   
[2, 20, 200]
a+b
   
[1, 10, 100, 2, 20, 200]
a+a
   
[1, 10, 100, 1, 10, 100]
b+b
   
[2, 20, 200, 2, 20, 200]
b*b
   
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    b*b
TypeError: can't multiply sequence by non-int of type 'list'
a+3+b
   
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a+3+b
TypeError: can only concatenate list (not "int") to list
a+4
   
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a+4
TypeError: can only concatenate list (not "int") to list
a*3
   
[1, 10, 100, 1, 10, 100, 1, 10, 100]
a*3*b
   
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a*3*b
TypeError: can't multiply sequence by non-int of type 'list'
(10,11,12)*2
...    
(10, 11, 12, 10, 11, 12)
>>> len('ejejej')
...    
6
>>> len(a)
...    
3
>>> len(1,2,3,4,5)
...    
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    len(1,2,3,4,5)
TypeError: len() takes exactly one argument (5 given)
>>> len((1,2,3,4,5))
...    
5
>>> a='yooneunjae'
...    
>>> a[0]
...    
'y'
>>> a[7]
...    
'j'
>>> a[-1]
...    
'e'
>>> a[-10]
...    
'y'
