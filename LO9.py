#can multiply lists and add lists 
"""
cloeceva@Cloes-MacBook-Air cs2100practice % source "/Users/cloeceva/Documents/CS Northeastern/CS2100 repository/cs21
00practice/.venv/bin/activate"
(.venv) cloeceva@Cloes-MacBook-Air cs2100practice % python3
Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Cmd click to launch VS Code Native REPL
>>> mylst = [1,2,3]
>>> mytuple = (4, 5, 6)
>>> tyoe(mylst)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tyoe' is not defined. Did you mean: 'type'?
>>> type(mylst)
<class 'list'>
>>> type(mytuple)
<class 'tuple'>
>>> mylst[1]= 100
>>> mylst
[1, 100, 3]
>>> mytuple[1]=100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> myset = {1,2,3,4,5,3,2,1,1}
>>> myset
{1, 2, 3, 4, 5}
>>> mydict = {'a':2, 'b':2, 'c':3}
>>> mydict['d'] = 4
>>> mydict
{'a': 2, 'b': 2, 'c': 3, 'd': 4}
>>> mydict['c'] = 25
>>> mydict
{'a': 2, 'b': 2, 'c': 25, 'd': 4}
>>> mydict['c'] =[1,2,3]
>>> mydict
{'a': 2, 'b': 2, 'c': [1, 2, 3], 'd': 4}
>>> mydict[[1,2,3]]= "weird"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> mydict[(1,2,3)] = "weird"
>>> mydict
{'a': 2, 'b': 2, 'c': [1, 2, 3], 'd': 4, (1, 2, 3): 'weird'}
>>> mydict2: dict[str, int] = {}
>>> mylst
[1, 100, 3]
>>> len(mylst)
3
>>> myset
{1, 2, 3, 4, 5}
>>> len(myset)
5
>>> mydict
{'a': 2, 'b': 2, 'c': [1, 2, 3], 'd': 4, (1, 2, 3): 'weird'}
>>> len(mydict)
5
>>> mytuple
(4, 5, 6)
>>> len(mytuple)
3
>>> mysquares = [ n ** 2 for n in range(1,11)
... mysquares
  File "<stdin>", line 2
    mysquares
    ^^^^^^^^^
SyntaxError: invalid syntax
>>> mysquares
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mysquares' is not defined
>>> mysq = [n ** 2 for n in range(1,11)
... mysq
  File "<stdin>", line 2
    mysq
    ^^^^
SyntaxError: invalid syntax
>>> names = "alice, bob, chris"
>>> names
'alice, bob, chris'
>>>  names = "alice, bob, chris",split(',')
  File "<stdin>", line 1
    names = "alice, bob, chris",split(',')
IndentationError: unexpected indent
>>> names = "alice, bob, chris".split(',')
>>> names
['alice', ' bob', ' chris']
>>> names[2]
' chris'
>>> names[-1]
' chris'
>>> names[-2]
' bob'
>>> mynums
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mynums' is not defined
>>> mynums = {0,1,2,3,4,5}
>>> mynums_l = [1,2,2,3,4,5,5]
>>> mynums_l[2:5]
[2, 3, 4]
>>> mynums_l[3:5}
  File "<stdin>", line 1
    mynums_l[3:5}
                ^
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> mynums_l[3:5]
[3, 4]
>>> names
['alice', ' bob', ' chris']
>>> names.append('dan')
>>> names
['alice', ' bob', ' chris', 'dan']
>>> names.insert(0, 'z')
>>> names
['z', 'alice', ' bob', ' chris', 'dan']
>>> mynums_l
[1, 2, 2, 3, 4, 5, 5]
>>> names + mynums_l
['z', 'alice', ' bob', ' chris', 'dan', 1, 2, 2, 3, 4, 5, 5]
>>> ['a'] * 3
['a', 'a', 'a']
>>> 'alice' in names
True
>>> 'edgar' in names
False """