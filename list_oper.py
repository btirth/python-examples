Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num = [1,45,32,78,54,33,99]
>>> num[::2]
[1, 32, 54, 99]
>>> num[2:7:3]
[32, 33]
>>> num[::-3]
[99, 78, 1]
>>> num = reverse(num)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    num = reverse(num)
NameError: name 'reverse' is not defined
>>> num.reverse()
>>> num
[99, 33, 54, 78, 32, 45, 1]
>>> num += [2,3,4]
>>> num
[99, 33, 54, 78, 32, 45, 1, 2, 3, 4]
>>> num.sort()
>>> num
[1, 2, 3, 4, 32, 33, 45, 54, 78, 99]
>>> 
