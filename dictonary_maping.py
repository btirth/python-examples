Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d = {'tirth':'samsung','hem':'mi','s':25}
>>> d.keys()
dict_keys(['tirth', 'hem', 's'])
>>> d.values()
dict_values(['samsung', 'mi', 25])
>>> d['tirth']
'samsung'
>>> d.get('hem')
'mi'
>>> d['mi']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d['mi']
KeyError: 'mi'
>>> d.get('s')
25
>>> 
