Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sum(a,*b):
	c = a
	for i in b:
		c = c + i
	print('sum is ',c)
	print('a is ',a)
	print('*b is ',b)

	
>>> sum(3,2,6,57,6)
sum is  74
a is  3
*b is  (2, 6, 57, 6)
>>> # *b is tuple
>>> 
