Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a= ['사과','바나나','딸기','키위','수박']
ㅁ
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
a
['사과', '바나나', '딸기', '키위', '수박']
if a=='사과':
    print ('사과입니까?')
else:
    print('오작동')

    
오작동
if '사과' in a:
    print('사과입니까?')
else:
    print('오작동')

    
사과입니까?
'사과' in a
True
a
['사과', '바나나', '딸기', '키위', '수박']
print(a)
['사과', '바나나', '딸기', '키위', '수박']

for i in range(10):
    print('안녕하세요, i)
          
SyntaxError: unterminated string literal (detected at line 2)
for i in range(10):
          print('안녕하세요',i)

          
안녕하세요 0
안녕하세요 1
안녕하세요 2
안녕하세요 3
안녕하세요 4
안녕하세요 5
안녕하세요 6
안녕하세요 7
안녕하세요 8
안녕하세요 9
>>> for abc in range(1,10,2):
...           print('안녕하세요',abc)
... 
...           
안녕하세요 1
안녕하세요 3
안녕하세요 5
안녕하세요 7
안녕하세요 9
>>> for i in range(15,-1,-1):
...           print('안녕하세요',i)
... 
...           
안녕하세요 15
안녕하세요 14
안녕하세요 13
안녕하세요 12
안녕하세요 11
안녕하세요 10
안녕하세요 9
안녕하세요 8
안녕하세요 7
안녕하세요 6
안녕하세요 5
안녕하세요 4
안녕하세요 3
안녕하세요 2
안녕하세요 1
안녕하세요 0
