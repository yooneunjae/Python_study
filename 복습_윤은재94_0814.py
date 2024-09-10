Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
re.match('a*b', 'b')
<re.Match object; span=(0, 1), match='b'>

re.match('a*b', 'ab')
<re.Match object; span=(0, 2), match='ab'>

re.match('a+b','ab')
<re.Match object; span=(0, 2), match='ab'>

re.match('i{3}','iiiloveu')
<re.Match object; span=(0, 3), match='iii'>

re.match('i{4}','iiiiloveu')
<re.Match object; span=(0, 4), match='iiii'>

re.match('(il){3}', 'ilililoveu')
<re.Match object; span=(0, 6), match='ililil'>

re.match('[0-9]*-[0-9]*-[0-9]*', '010-1234-5678')
<re.Match object; span=(0, 13), match='010-1234-5678'>

re.match('[0-9]*-[0-9]*-[0-9]*', '010-1234-512312678')
<re.Match object; span=(0, 18), match='010-1234-512312678'>

re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1234-512312678')
<re.Match object; span=(0, 13), match='010-1234-5123'>

re.match('[a-zA-Z0-9]+','231231Hello1231231')
<re.Match object; span=(0, 18), match='231231Hello1231231'>

re.search('\*+','2 ****** 3')
<re.Match object; span=(2, 8), match='******'>

re.search('[0-9]+$','Hello12312312asdf')

re.search('[0-9]+','Hello12312312asdf')
<re.Match object; span=(5, 13), match='12312312'>

re.match('[$()\w]+' '$(안녕)')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    re.match('[$()\w]+' '$(안녕)')
TypeError: match() missing 1 required positional argument: 'string'
re.match('[$()\W]+', '$(안녕)')
<re.Match object; span=(0, 2), match='$('>

re.match('[\w]+', 'Hello Python')
<re.Match object; span=(0, 5), match='Hello'>

re.match('[\w ]+', 'Hello Python')
<re.Match object; span=(0, 12), match='Hello Python'>

re.match('([0-9]+ ([0-9]+)', '50 60')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    re.match('([0-9]+ ([0-9]+)', '50 60')
  File "C:\Users\윤은재\AppData\Local\Programs\Python\Python312\Lib\re\__init__.py", line 167, in match
    return _compile(pattern, flags).match(string)
  File "C:\Users\윤은재\AppData\Local\Programs\Python\Python312\Lib\re\__init__.py", line 307, in _compile
    p = _compiler.compile(pattern, flags)
  File "C:\Users\윤은재\AppData\Local\Programs\Python\Python312\Lib\re\_compiler.py", line 745, in compile
    p = _parser.parse(p, flags)
  File "C:\Users\윤은재\AppData\Local\Programs\Python\Python312\Lib\re\_parser.py", line 979, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "C:\Users\윤은재\AppData\Local\Programs\Python\Python312\Lib\re\_parser.py", line 460, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "C:\Users\윤은재\AppData\Local\Programs\Python\Python312\Lib\re\_parser.py", line 864, in _parse
    raise source.error("missing ), unterminated subpattern",
re.error: missing ), unterminated subpattern at position 0

re.match('([0-9]+) ([0-9]+)', '50 60')
<re.Match object; span=(0, 5), match='50 60'>
m=re.match('([0-9]+) ([0-9]+)', '50 60')
m1=re.match('([0-9]+) ([a-z]+)', '50 abc')

m1.group(1)
'50'

m1.group(2)
'abc'

m1.group(0)
'50 abc'

m1.group()
'50 abc'

re.findall('[0-9]+', '1,2,3,4,5,육,7,8,9,십')
['1', '2', '3', '4', '5', '7', '8', '9']

ㅁ
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
a
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a
NameError: name 'a' is not defined
a=re.findall('[0-9]+', '1,2,3,4,5,육,7,8,9,십')

a
['1', '2', '3', '4', '5', '7', '8', '9']

a=['103호','502호','758호','523호','208호']
                       
a[0]
'103호'

for i in range(len(a)):
    print(re.findall('[0-9]+',a[i]), end=' ')

    
['103'] ['502'] ['758'] ['523'] ['208'] 

c='asldfjweifjadlkfjalkdfgjanlfjsldfvaslkdjfskdj;;asdfasj;dafv_고객넘버_민어리;ㅏ러닝럼ㅍ'

ㅊ
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    ㅊ
NameError: name 'ᄎ' is not defined
c
'asldfjweifjadlkfjalkdfgjanlfjsldfvaslkdjfskdj;;asdfasj;dafv_고객넘버_민어리;ㅏ러닝럼ㅍ'
re.findall('[가-힣]+',c)
['고객넘버', '민어리', '러닝럼']

'python@gmail.com'
'python@gmail.com'
re.match('[a-z0-9]+@[a-z]+\.[a-z]+','python@gmail.com')
<re.Match object; span=(0, 16), match='python@gmail.com'>

re.match('[a-z0-9]+@[a-z]+\.[a-z]+','python@gmail.com'.lower())
<re.Match object; span=(0, 16), match='python@gmail.com'>

emails=['python@gmail.com','123python@gmail.com','Python@gmail.com','--!python@gmail.com']

for i in range(len(emails)):
                       print(re.match('[a-z0-9]+@[a-z]+\.[a-z]+', emails[i]))

                       
<re.Match object; span=(0, 16), match='python@gmail.com'>
<re.Match object; span=(0, 19), match='123python@gmail.com'>
None
None



print('hi')
                       
hi

import re
re.match
<function match at 0x0000016659F774C0>

import re
>>> import math as m
>>> import pandas as pd
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
>>> math.pi
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    math.pi
NameError: name 'math' is not defined. Did you forget to import 'math'?
>>> 
>>> pi
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    pi
NameError: name 'pi' is not defined. Did you mean: 'i'?
>>> 
>>> 
>>> import seaborn as sns
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    import seaborn as sns
ModuleNotFoundError: No module named 'seaborn'
>>> import pandas as pd
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
>>> import re
