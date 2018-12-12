Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 13
>>> b = 20
>>> def smth():
	a = 10
	x = globals()['a']
	globals()['a'] = 34
	print(x)

	
>>> smth()
13
>>> a
34
>>> 
