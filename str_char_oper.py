Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> msg = 'tirth'
>>> msg1 = "tirth"
>>> msg.upper()
'TIRTH'
>>> msg2 = 'TBharatiya'
>>> msg2.lower()
'tbharatiya'
>>> msg.is lower()
SyntaxError: invalid syntax
>>> msg.isupper()
False
>>> 'Tirth'.istitle()
True
>>> 'tirth'.istitle()
False
>>> '123'.isdigit()
True
>>> 'hello'.capitalize()
'Hello'
>>> msg.endwith('th')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    msg.endwith('th')
AttributeError: 'str' object has no attribute 'endwith'
>>> 'hello'.endwith('lo')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    'hello'.endwith('lo')
AttributeError: 'str' object has no attribute 'endwith'
>>> import string
>>> msg.endwith('th')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    msg.endwith('th')
AttributeError: 'str' object has no attribute 'endwith'
>>> 
>>> 
>>> msg.find('h')
4
>>> msg.find('t')
0
>>> 
>>> 
