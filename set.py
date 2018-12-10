Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> s = {25,6.3,'tirth'}
>>> 
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s[0]
TypeError: 'set' object does not support indexing
>>> s[1] = 45
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s[1] = 45
TypeError: 'set' object does not support item assignment
>>> 
