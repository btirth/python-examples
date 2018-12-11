Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def greet():
	print('Hello')

>>> greet
<function greet at 0x00000216D32CC1E0>
>>> greet()
Hello
>>> 
>>> 
>>> 
>>> def add(x,y):
	c = x + y
	print(c)

>>> add(4,5.7)
9.7
>>> 
>>> 
>>> 
>>> def add(x,y):
	c = x + y
	return c

>>> result = add(3,7)
>>> print(result)
10
>>> 
>>> 
>>> 
>>> def fun(x,y):
	c = x + y
	d = x - y
	return c,d

>>> result1,result2 = fun(10,4)
>>> print(result1)
14
>>> print(result2)
6
>>> 
>>> 
>>> 
>>> def update(b):
	print(id(b))
	b[1] = 25
	print(id(b))
	print("b ",b)

	
>>> lst = [10,20,40]
>>> print(id(lst))
2297067159880
>>> update(lst)
2297067159880
2297067159880
b  [10, 25, 40]
>>> print("lst ",lst)
lst  [10, 25, 40]
>>> 
