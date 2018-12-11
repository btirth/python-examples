Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def person(name,**data):
	print('name is ',name)
	print(data)
	print('or')
	for i,j in data.items():
		print(i,j)

		
>>> person('tirth',age=18,city=mhd,mobile_no=9106321002)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    person('tirth',age=18,city=mhd,mobile_no=9106321002)
NameError: name 'mhd' is not defined
>>> 
>>> 
>>> 
>>> person('tirth',age=18,city='mhd',mobile_no=9106321002)
name is  tirth
{'age': 18, 'city': 'mhd', 'mobile_no': 9106321002}
or
age 18
city mhd
mobile_no 9106321002
>>> 
