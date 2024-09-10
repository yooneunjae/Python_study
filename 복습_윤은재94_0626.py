Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(3):
    print (i, '안쪽', end = ' ')
    for j in range(4):
        print(j, ' 바깥쪽', end=' ')

        
0 안쪽 0  바깥쪽 1  바깥쪽 2  바깥쪽 3  바깥쪽 1 안쪽 0  바깥쪽 1  바깥쪽 2  바깥쪽 3  바깥쪽 2 안쪽 0  바깥쪽 1  바깥쪽 2  바깥쪽 3  바깥쪽 

for i in range(3)
SyntaxError: expected ':'
for i in range(3):
    for j in range(4):
        print('안: ', j, sep='',end=' ')
        print('바깥 : ',ㅑ,'\\n', sep='')

        
안: 0 Traceback (most recent call last):
  File "<pyshell#11>", line 4, in <module>
    print('바깥 : ',ㅑ,'\\n', sep='')
NameError: name 'ᅣ' is not defined
for i in range(3):
    for j in range(4):
        print('안: ', j, sep='',end=' ')
        print('바깥 : ',i,'\\n', sep='')

        
안: 0 바깥 : 0\n
안: 1 바깥 : 0\n
안: 2 바깥 : 0\n
안: 3 바깥 : 0\n
안: 0 바깥 : 1\n
안: 1 바깥 : 1\n
안: 2 바깥 : 1\n
안: 3 바깥 : 1\n
안: 0 바깥 : 2\n
안: 1 바깥 : 2\n
안: 2 바깥 : 2\n
안: 3 바깥 : 2\n

for i in range(3):
    for j in range(4):
        print(i, end=' ')

        
0 0 0 0 1 1 1 1 2 2 2 2 
for i in range(3):
    for j in range(5):
        print(i, end=' ')

        
0 0 0 0 0 1 1 1 1 1 2 2 2 2 2 

for i in range(5):
    for j in range(5):
        print ('j')
        print(i, end=' ')

        
j
0 j
0 j
0 j
0 j
0 j
1 j
1 j
1 j
1 j
1 j
2 j
2 j
2 j
2 j
2 j
3 j
3 j
3 j
3 j
3 j
4 j
4 j
4 j
4 j
4 
for i in range(3):
    for j in range(3):
        print('배고파')

        
배고파
배고파
배고파
배고파
배고파
배고파
배고파
배고파
배고파
for i in range(3):
    for j in range(3):
        print('나도 배고파')

        
나도 배고파
나도 배고파
나도 배고파
나도 배고파
나도 배고파
나도 배고파
나도 배고파
나도 배고파
나도 배고파

idx_value = []
for i in range(3):
    print(i)
    idx_value.append(i)

    
0
1
2

for j in range(2):
    for i in range(3):
        print(i)

        
0
1
2
0
1
2

for i in range(5):
    for j in range(5):
        print ('*", end='')
               
SyntaxError: unterminated string literal (detected at line 3)
for i in range(5):
    for j in range(5):
        print ('*', end=' ')
               print()
               
SyntaxError: unexpected indent
3)
for i in range(5):
    for j in range(5):
        print ('*', end=' ')
    print()
    
SyntaxError: unmatched ')'




for i in range(5):
    for j in range(5):
        print ('*', end=' ')
    print()

    
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end =' ')
        print('바깥: ',i,'\\n',sep=' ')

        
* 바깥:  0 \n
바깥:  0 \n
바깥:  0 \n
바깥:  0 \n
바깥:  0 \n
* 바깥:  1 \n
* 바깥:  1 \n
바깥:  1 \n
바깥:  1 \n
바깥:  1 \n
* 바깥:  2 \n
* 바깥:  2 \n
* 바깥:  2 \n
바깥:  2 \n
바깥:  2 \n
* 바깥:  3 \n
* 바깥:  3 \n
* 바깥:  3 \n
* 바깥:  3 \n
바깥:  3 \n
* 바깥:  4 \n
* 바깥:  4 \n
* 바깥:  4 \n
* 바깥:  4 \n
* 바깥:  4 \n
for i in a:
    print(i)
    for j in range(3):
        print(j)

        
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    for i in a:
NameError: name 'a' is not defined
a=['사과', '바나나', '딸기']
for i in a:
    print(i)
    for j in range(3):
        print(j)

        
사과
0
1
2
바나나
0
1
2
딸기
0
1
2

for i in range(10):
    if i % 2 ==0:
        for j in range(3):
            print (j, end=' ')
        print(i)

        
0 1 2 0
0 1 2 2
0 1 2 4
0 1 2 6
0 1 2 8

for i in range(1, 101):
    if i%3==0 and i % 5==0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print elif % == 0:
            
SyntaxError: invalid syntax
for i in range(1, 101):
    if i%3==0 and i % 5==0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

        
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizzbuzz
31
32
fizz
34
buzz
fizz
37
38
fizz
buzz
41
fizz
43
44
fizzbuzz
46
47
fizz
49
buzz
fizz
52
53
fizz
buzz
56
fizz
58
59
fizzbuzz
61
62
fizz
64
buzz
fizz
67
68
fizz
buzz
71
fizz
73
74
fizzbuzz
76
77
fizz
79
buzz
fizz
82
83
fizz
buzz
86
fizz
88
89
fizzbuzz
91
92
fizz
94
buzz
fizz
97
98
fizz
buzz
