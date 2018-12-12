Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def is_even(n):
	return n%2==0

>>> nums = [3,6,5,8,14]
>>> evens = list(filter(is_even,nums))
>>> evens
[6, 8, 14]
>>> 
>>> 
>>> doubles = list(map(lambda n:n*2,evens))
>>> doubles
[12, 16, 28]
>>> 
>>> 
>>> sum = reduce(lambda a,b:a+b,doubles)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    sum = reduce(lambda a,b:a+b,doubles)
NameError: name 'reduce' is not defined
>>> sum = list(reduce(lambda a,b:a+b,doubles))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    sum = list(reduce(lambda a,b:a+b,doubles))
NameError: name 'reduce' is not defined
>>> 
>>> import functools
>>> sum = functools.reduce(lambda a,b:a+b,doubles)
>>> sum
56
>>> 
