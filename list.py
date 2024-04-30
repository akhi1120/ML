Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=[1,2,3,4,5,6]
>>> print(list1)
[1, 2, 3, 4, 5, 6]
>>> #append
>>> list1.append(7)
>>> list1
[1, 2, 3, 4, 5, 6, 7]
>>> list1.insert(0,10)
>>> liat1
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    liat1
NameError: name 'liat1' is not defined. Did you mean: 'list1'?
>>> list1.insert(0,10)
>>> list1
[10, 10, 1, 2, 3, 4, 5, 6, 7]
>>> del list1[10]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    del list1[10]
IndexError: list assignment index out of range
>>> del list1[6]
>>> list1
[10, 10, 1, 2, 3, 4, 6, 7]
>>> list1.clear()
>>> list1
[]
>>> list3[1,2,3,4,5]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list3[1,2,3,4,5]
NameError: name 'list3' is not defined. Did you mean: 'list1'?
>>> list3=[1,2,3,4,5]
>>> list3
[1, 2, 3, 4, 5]
>>> list3.extend([6,7,8,9])
>>> list3
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list3.insert(2[2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    list3.insert(2[2,3,4,5])
TypeError: 'int' object is not subscriptable
>>> list3.insert(2,[2,3,4,5,6])
>>> list3
[1, 2, [2, 3, 4, 5, 6], 3, 4, 5, 6, 7, 8, 9]
list3[0:3]=['akhi']
list3
['akhi', 3, 4, 5, 6, 7, 8, 9]
list3.pop[3]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list3.pop[3]
TypeError: 'builtin_function_or_method' object is not subscriptable
list3.pop(3)
5
list3.remove(8)
list3
['akhi', 3, 4, 6, 7, 9]
list3.sort
<built-in method sort of list object at 0x000001E06A7EF3C0>
list3.sort()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list3.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
list3.remove(akhi)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list3.remove(akhi)
NameError: name 'akhi' is not defined
list3.remove('akhi')
list3
[3, 4, 6, 7, 9]
list3.sort()
list3
[3, 4, 6, 7, 9]
[3, 4, 6, 7, 9]
[3, 4, 6, 7, 9]
#iteration
list4=[1,2,3,4,5]
for i in list4:
    print(i)

1
2
3
4
5
