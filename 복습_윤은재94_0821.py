Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time

time.time()
1724753253.662397

time.localtime(time.time())
time.struct_time(tm_year=2024, tm_mon=8, tm_mday=27, tm_hour=19, tm_min=8, tm_sec=2, tm_wday=1, tm_yday=240, tm_isdst=0)

time.localtime(1724241810.312791)
time.struct_time(tm_year=2024, tm_mon=8, tm_mday=21, tm_hour=21, tm_min=3, tm_sec=30, tm_wday=2, tm_yday=234, tm_isdst=0)

time.localtime(500)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=9, tm_min=8, tm_sec=20, tm_wday=3, tm_yday=1, tm_isdst=0)

time.strftime('%Y-%m-%d',time.localtime(time.time()))
'2024-08-27'

import datetime

datetime.datetime.today()
datetime.datetime(2024, 8, 27, 19, 10, 38, 762625)

datetime.datetime.now()
datetime.datetime(2024, 8, 27, 19, 10, 56, 438137)

from datetime import timezone

datetime.datetime.now(timezone.utc)
datetime.datetime(2024, 8, 27, 10, 11, 50, 12075, tzinfo=datetime.timezone.utc)


to_day=datetime.datetime(2024,8,27, hour=19, minute=14)

to_day
datetime.datetime(2024, 8, 27, 19, 14)

time.strfttime('%Y-%m-%d', '2024-08-27')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    time.strfttime('%Y-%m-%d', '2024-08-27')
AttributeError: module 'time' has no attribute 'strfttime'. Did you mean: 'strftime'?


datetime.datetime(2024, 1, 1, 0, 0)
datetime.datetime(2024, 1, 1, 0, 0)

datetime.datetime('2024','%Y')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    datetime.datetime('2024','%Y')
TypeError: 'str' object cannot be interpreted as an integer

datetime.datetime.strptime('2024','%Y')
datetime.datetime(2024, 1, 1, 0, 0)



to_day=datetime.datetime(2024,8,25)
to_Day
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    to_Day
NameError: name 'to_Day' is not defined. Did you mean: 'to_day'?
to_day
datetime.datetime(2024, 8, 25, 0, 0)

>>> from datetime import timedelta
>>> 
>>> to_day - timelta(days=151)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    to_day - timelta(days=151)
NameError: name 'timelta' is not defined. Did you mean: 'timedelta'?
>>> 
>>> datetime.datetime(2024,8,25) - datetime.datetime(2024,3,10)
datetime.timedelta(days=168)
>>> 
>>> datetime.datetime(2024,3,10) - datetime.datetime(2024,8,25)
datetime.timedelta(days=-168)
>>> 
>>> 
>>> a=[1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> b
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> b=[['파이썬 문법 기초'],['sql 문법기초'],['ams 클라우드 기초']]
>>> ㅠ
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    ㅠ
NameError: name 'ᅲ' is not defined
>>> b
[['파이썬 문법 기초'], ['sql 문법기초'], ['ams 클라우드 기초']]
