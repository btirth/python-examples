Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> nums=[5,45,98]
>>> names=['kiran','tirth','hem']
>>> values=['tirth',5,2.3]
>>> mil=[names,nums]
>>> mil
[['kiran', 'tirth', 'hem'], [5, 45, 98]]
>>> nums.append(45)
>>> nums
[5, 45, 98, 45]
>>> nums.remove(5)
>>> nums
[45, 98, 45]
>>> nums.insert(2,1)
>>> nums
[45, 98, 1, 45]
>>> del.nums[1:3]
SyntaxError: invalid syntax
>>> del nums[1:3]
>>> nums
[45, 45]
>>> nums.extend([34,87,99,101])
>>> nums
[45, 45, 34, 87, 99, 101]
>>> min(nums)
34
>>> max(nums)
101
>>> sum(nums)
411
>>> nums.sort()
>>> num
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    num
NameError: name 'num' is not defined
>>> nums
[34, 45, 45, 87, 99, 101]
>>> 
