Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(10):
    print('안녕하세요?',i)

    
안녕하세요? 0
안녕하세요? 1
안녕하세요? 2
안녕하세요? 3
안녕하세요? 4
안녕하세요? 5
안녕하세요? 6
안녕하세요? 7
안녕하세요? 8
안녕하세요? 9
idx
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    idx
NameError: name 'idx' is not defined. Did you mean: 'id'?
idx = 0
while idx<10:
    print ('안녕하세요?',idx)
    idx+=1

    
안녕하세요? 0
안녕하세요? 1
안녕하세요? 2
안녕하세요? 3
안녕하세요? 4
안녕하세요? 5
안녕하세요? 6
안녕하세요? 7
안녕하세요? 8
안녕하세요? 9
i=50
while i>0:
    print('루프인덱스를 감소시키자!',i)
    i-=1

    
루프인덱스를 감소시키자! 50
루프인덱스를 감소시키자! 49
루프인덱스를 감소시키자! 48
루프인덱스를 감소시키자! 47
루프인덱스를 감소시키자! 46
루프인덱스를 감소시키자! 45
루프인덱스를 감소시키자! 44
루프인덱스를 감소시키자! 43
루프인덱스를 감소시키자! 42
루프인덱스를 감소시키자! 41
루프인덱스를 감소시키자! 40
루프인덱스를 감소시키자! 39
루프인덱스를 감소시키자! 38
루프인덱스를 감소시키자! 37
루프인덱스를 감소시키자! 36
루프인덱스를 감소시키자! 35
루프인덱스를 감소시키자! 34
루프인덱스를 감소시키자! 33
루프인덱스를 감소시키자! 32
루프인덱스를 감소시키자! 31
루프인덱스를 감소시키자! 30
루프인덱스를 감소시키자! 29
루프인덱스를 감소시키자! 28
루프인덱스를 감소시키자! 27
루프인덱스를 감소시키자! 26
루프인덱스를 감소시키자! 25
루프인덱스를 감소시키자! 24
루프인덱스를 감소시키자! 23
루프인덱스를 감소시키자! 22
루프인덱스를 감소시키자! 21
루프인덱스를 감소시키자! 20
루프인덱스를 감소시키자! 19
루프인덱스를 감소시키자! 18
루프인덱스를 감소시키자! 17
루프인덱스를 감소시키자! 16
루프인덱스를 감소시키자! 15
루프인덱스를 감소시키자! 14
루프인덱스를 감소시키자! 13
루프인덱스를 감소시키자! 12
루프인덱스를 감소시키자! 11
루프인덱스를 감소시키자! 10
루프인덱스를 감소시키자! 9
루프인덱스를 감소시키자! 8
루프인덱스를 감소시키자! 7
루프인덱스를 감소시키자! 6
루프인덱스를 감소시키자! 5
루프인덱스를 감소시키자! 4
루프인덱스를 감소시키자! 3
루프인덱스를 감소시키자! 2
루프인덱스를 감소시키자! 1
for i in range(10):
    print('무한루프를 끝내자!',i)
    if i==5:
        break

    
무한루프를 끝내자! 0
무한루프를 끝내자! 1
무한루프를 끝내자! 2
무한루프를 끝내자! 3
무한루프를 끝내자! 4
무한루프를 끝내자! 5
i=0
while i <20:
    print('while 반복',i)
    i+=1

    
while 반복 0
while 반복 1
while 반복 2
while 반복 3
while 반복 4
while 반복 5
while 반복 6
while 반복 7
while 반복 8
while 반복 9
while 반복 10
while 반복 11
while 반복 12
while 반복 13
while 반복 14
while 반복 15
while 반복 16
while 반복 17
while 반복 18
while 반복 19
i=0
while i <20:
    i +=1
    if i == 10:
        continu
        print ('while반복',i)

        
Traceback (most recent call last):
  File "<pyshell#30>", line 4, in <module>
    continu
NameError: name 'continu' is not defined
i=0
while i <20:
    i +=1
    if i == 10:
        continue
    print('while 반복',i)

    
while 반복 1
while 반복 2
while 반복 3
while 반복 4
while 반복 5
while 반복 6
while 반복 7
while 반복 8
while 반복 9
while 반복 11
while 반복 12
while 반복 13
while 반복 14
while 반복 15
while 반복 16
while 반복 17
while 반복 18
while 반복 19
while 반복 20
i=0
while i <20:
    i+=1
    if i %2==0:
        continue
    print('while 반복'.i)

    
Traceback (most recent call last):
  File "<pyshell#41>", line 5, in <module>
    print('while 반복'.i)
AttributeError: 'str' object has no attribute 'i'
i=0
while i <20:
    i+=1
    if i %2==0:
        continue
    print('while 반복',i)
    
SyntaxError: multiple statements found while compiling a single statement

i=0
while i <20:
    i+=1
    if i %2==0:
        continue
    print('while 반복',i)

    
while 반복 1
while 반복 3
while 반복 5
while 반복 7
while 반복 9
while 반복 11
while 반복 13
while 반복 15
while 반복 17
while 반복 19
i = 0
while i <20:
    i+=1
    print('while 반복',i)
    if i %2==1:

        continue

    
while 반복 1
while 반복 2
while 반복 3
while 반복 4
while 반복 5
while 반복 6
while 반복 7
while 반복 8
while 반복 9
while 반복 10
while 반복 11
while 반복 12
while 반복 13
while 반복 14
while 반복 15
while 반복 16
while 반복 17
while 반복 18
while 반복 19
while 반복 20
>>> import seaborn as sns
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    import seaborn as sns
ModuleNotFoundError: No module named 'seaborn'
>>> 
>>> fare_list=list(df['fare'])
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    fare_list=list(df['fare'])
NameError: name 'df' is not defined
>>> df=sns.load_dataset('titanic')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    df=sns.load_dataset('titanic')
NameError: name 'sns' is not defined
>>> fare_list=list(df['fare'])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    fare_list=list(df['fare'])
NameError: name 'df' is not defined
>>> for i in fare_list:
...     if i >50:
...         print(i)
... 
...         
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    for i in fare_list:
NameError: name 'fare_list' is not defined
