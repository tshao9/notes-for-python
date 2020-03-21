### **str类型**

字符串是不可变的数据类型，不论执行什么操作，源字符串不改变，每次操作会返回新字符串。
1. 索引index
2. 切片
* 左闭右开
* 不规定负向步长的情况下只能从左向右切  
*[-1: -3]会报错 [-1: -3: -1]不会报错

3. 可迭代
```python
s = 'tsj'
for x in s:
    print(s)
```
***
### **String Methods**
#### **str.capitalize()**    
返回一个字符串，第一个字母大写，其余字母全部小写。
#### **str.center(*width[,fillchar]*)**
返回一个长度为*width*的字符串，中间为str，由*fillchar*填充（默认为空格）。
如果所给*width*小于原字符串，则返回原字符串。
#### **str.count(*sub[, start[, end]]*)**
返回*sub*的个数
#### **str.find(*sub[, start[, end]]*)**
找到*sub*所在位置后返回最小的下标。如果没有*sun*则返回-1。
#### **str.format()**
format 函数可以接受不限个参数，位置可以不按顺序。
```python
>>> s = '我是%s，我有%s分喜欢%s' % ('tsj','100','白展堂')
我是tsj，我有100分喜欢白展堂
>>> s = '我是{}，我有{}分喜欢{}'.format('tsj','100','白展堂')
我是tsj，我有100分喜欢白展堂
>>> s = '我是{2}，我有{1}分喜欢{0}'.format('tsj','100','白展堂')
我是白展堂，我有100分喜欢tsj
>>> s = '我是{name}，我有{score}分喜欢{boyfriend}'.format(name='tsj',score='100',boyfriend='白展堂')
我是tsj，我有100分喜欢白展堂
​
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
```
也可以向 str.format() 传入对象：
```python
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的
​
#输出结果为:
value 为: 6
```
str.format() 格式化数字的多种方法:
数字 | 格式 | 输出 | 描述
-|-|-|-
3.1415926|	{:.2f}|	3.14|	保留小数点后两位
3.1415926|	{:+.2f}|	+3.14|	带符号保留小数点后两位
-1	|{:+.2f}	|-1.00|	带符号保留小数点后两位
2.71828	|{:.0f}|	3	|不带小数
5	|{:0>2d}	|05	|数字补零 (填充左边, 宽度为2)
5	|{:x<4d}	|5xxx	|数字补x (填充右边, 宽度为4)
10	|{:x<4d}	|10xx	|数字补x (填充右边, 宽度为4)
1000000|	{:,}|	1,000,000	|以逗号分隔的数字格式
0.25|	{:.2%}|	25.00%|	百分比格式
1000000000|	{:.2e}|	1.00e+09	|指数记法
13|	{:>10d}	  |      13	右对齐| (默认, 宽度为10)
13|	{:<10d}	|13	|左对齐 (宽度为10)
13|	{:^10d}	  |  13	|中间对齐 (宽度为10)
11	|'{:b}'.format(11) }|1011|	二进制
11|'{:d}'.format(11) |11|十进制
11|'{:o}'.format(11)}|13	|八进制
11|'{:x}'.format(11) |b	|十六进制
11|'{:#x}'.format(11)|0xb|十六进制
11|'{:#X}'.format(11)|0XB|十六进制
此外，可以在format()中使用大括号 {} 来转义大括号。
str.endswith(suffix[, start[, end]])

Like str.startswith(prefix[, start[, end]]).
str.index(sub[, start[, end]])

Like find(), but raise ValueError when the substring is not found.
str.isdigit()

Return True if all characters in the string are digits and there is at least one character, False otherwise.
str.isalpha()
Return True if all characters in the string are alphabetic and there is at least one character, False otherwise.
str.isalnum()
Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise.
str.lower()    
    Return a copy of the string with all the cased characters converted to lowercase.
str.lstrip([chars])

 Like str.strip([chars]).    
str.replace(old, new[, count])    
Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
str.rstrip([chars])

Like str.strip([chars]).
str.split(sep=None, maxsplit=-1)    
Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings.
>>> '1,2,,3,'.split(',')
['1', '2', '', '3', '']
>>> '1<>2<>3'.split('<>')
['1', '2', '3'])
>>> 'tsj'.split('tsj')
['','']
If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].
str.startswith(prefix[, start[, end]])
Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.
str.strip([chars])    

Return a copy of the string with the leading and trailing characters removed. The chars  argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespac
The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:
>>> 'www.example.com'.strip('cmowz.')
'example'
>>> 'www.example.com'.strip('cmowz.e')
'xampl'
>>> 'www.example.com'.strip('cmowz.ea')
'xampl'
str.title()   

Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.For example:
>>> 'Hello world'.title()
'Hello World'
The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions and possessives form word boundaries, which may not be the desired result: (所有字母外的符号都算分隔符)
>>> "they're bill's friends from the UK".title()
"They'Re Bill'S Friends From The Uk"
A workaround for apostrophes can be constructed using regular expressions:
>>> import re
>>> def titlecase(s):
...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0).capitalize(),
...                   s)
...
>>> titlecase("they're bill's friends.")
"They're Bill's Friends."
str.upper()    
    Return a copy of the string with all the cased characters converted to uppercase.


list类型

列表是一个可变的数据类型。
1.索引index
2.切片slice


List Methods
list.append(x)


Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)

Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

>>> ['tsj','zmy'].extend('孙悟空')
['tsj', 'zmy', '孙', '悟', '空']
>>> ['tsj','zmy'].extend(['孙悟空'])
['tsj', 'zmy', '孙悟空']
list.insert(i, x)

Insert an item at a given position. The first argument is the index of the element before which to insert.

list.remove(x)

Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

>>> lst = ['one','two','three','four']
>>> for el in lst:
...     lst.remove(el)
>>> lst
['two', 'four']
list.pop([i])

Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. 

list.clear()

Remove all items from the list. Equivalent to del a[:].

del list[index/slice]
>>> game = ['星露谷物语','lol','以撒','ff14','undertale']
>>> del game[1]
>>> game
['星露谷物语', '以撒', 'ff14', 'undertale']
>>> del game[1:3]
>>> game
['星露谷物语', 'undertale']
list的更改
>>> game = ['星露谷物语','lol','以撒','ff14','undertale']
>>> game[1] = '古剑奇谭'
>>> game
['星露谷物语', '古剑奇谭', '以撒', 'ff14', 'undertale']
>>> game[1:3] = ['巫师3']
>>> game
['星露谷物语', '巫师3', 'ff14', 'undertale']
>>> game[1:3] = '巫师3'
>>> game
['星露谷物语', '巫', '师', '3', 'undertale']
>>> game[1::2] = ['黑暗料理王']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 1 to extended slice of size 2
>>> game[1::2] = ['黑暗料理王','赛博朋克酒保']
>>> game
['星露谷物语', '黑暗料理王', '师', '赛博朋克酒保', 'undertale']
>>> game[1::2] = ['明星志愿','大富翁','仙剑奇侠传']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 3 to extended slice of size 2
list.index(x[, start[, end]])


Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

list.count(x)

Return the number of times x appears in the list.

list.sort(key=None, reverse=False)

Sort the items of the list in place.

list.reverse()

Reverse the elements of the list in place.

list.copy()

Return a shallow copy of the list. Equivalent to a[:].



元组类型
只读列表，不支持增删改等操作，可以查询。
1元组为空或只有一个元素时:
tu = tuple()    # 空元祖 不可以只用一个空括号表示
tu = (3,)   # 只有一个元素时要加‘，’
2.索引index
3.切片slice
4.元组的不可变指的是子元素不可变。而子元素内部元素是可变的，这取决于子元素是否是可变对象。
>>> game = ('MMO',['以撒'])
>>> game[1].append('巫师3')
>>> game
('MMO', ['以撒', '巫师3'])
>>> game[0] = game[0].lower
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


字典类型
1.key要求具有可哈希的性质，不可变的数据类型才可以当做键。
2.初始化字典。
>>>dict()                        # 创建空字典
{}
​
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True
3.没有索引和切片
4.迭代时获取的是key
dic = {'one':1,'two':2}
for i in dic:
       print(i)
'''     
one
two
'''
Dic Methods
dic.setdefault(key[, default])

If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
>>> game = {'MMO':'ff14','单机':'巫师3'}
>>> game.setdefault('养成','明星志愿3')
'明星志愿3'
>>> game
{'MMO': 'ff14', '单机': '巫师3', '养成': '明星志愿3'}
>>> game.setdefault('养成','牧场物语')
'明星志愿3'
>>> game
{'MMO': 'ff14', '单机': '巫师3', '养成': '明星志愿3'}
dic.pop(key[, default])
If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised.
del dic[key]
dic.clear()
Remove all items from the dictionary.
dic.popitem()

Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO order. If the dictionary is empty, calling popitem() raises a KeyError.

dic.update([other])


Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.

update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two). If keyword arguments are specified, the dictionary is then updated with those key/value pairs: d.update(red=1, blue=2).

>>> game = {'MMO':'ff14','单机':'巫师3'}
>>> game.update({'养成':'明星志愿','roguelike':'以撒'}) #传入一个字典
>>> game.update(养成='明星志愿',roguelike='以撒')   #传入关键字
>>> game.update([('养成','明星志愿'),('roguelike','以撒'),('休闲','大富翁')])#传一个包含一个或多个元组的列表 
>>> game.update((['养成','明星志愿'],))   #传一个包含一个或多个列表的元组 
dic.get(key[, default])
Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.
>>> dic = {'one':1,'two':2}
>>> dic.get('three',3)
3
>>> dic
{'one': 1, 'two': 2}
>>> dic.get('three') == None
True
dic.keys() dic.values() dic.items()
Return a new view of the dictionary's keys/views/items.
Dictionary view objects
The objects provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes. Dictionary views can be iterated over to yield their respective data, and support membership tests:
len(dictview)

Return the number of entries in the dictionary.
iter(dictview)
Return an iterator over the keys, values or items (represented as tuples of (key, value)) in the dictionary.

Keys and values are iterated over in insertion order. This allows the creation of (value, key) pairs using zip(): pairs = zip(d.values(), d.keys()). Another way to create the same list is pairs = [(v, k) for (k, v) in d.items()].

Iterating views while adding or deleting entries in the dictionary may raise a RuntimeError or fail to iterate over all entries.

reversed(dictview)
Return a reverse iterator over the keys, values or items of the dictionary. The view will be iterated in reverse order of the insertion.

>>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
>>> keys = dishes.keys()
>>> keys
dict_keys(['eggs', 'sausage', 'bacon', 'spam'])
>>> values = dishes.values()
>>> items = dishes.items()
​
>>> n = 0
>>> for val in values:
...     n += val
...
>>> print(n)
504
​
>>> list(keys)
['eggs', 'sausage', 'bacon', 'spam']
>>> list(items)
[('eggs', 2), ('sausage', 1), ('bacon', 1), ('spam', 500)]
​
>>> del dishes['eggs']
>>> del dishes['sausage']
>>> list(keys)
['bacon', 'spam']
​
>>> # set operations
>>> keys & {'eggs', 'bacon', 'salad'}
{'bacon'}
>>> keys ^ {'sausage', 'juice'}
{'juice', 'sausage', 'bacon', 'spam'}
dic.fromkeys(iterable[, value]) 
Create a new dictionary with keys from iterable and values set to value.
>>> dic = {}
>>> lst = ['one','two','three']
>>> dic.fromkeys(lst)
{'one': None, 'two': None, 'three': None}
>>> dic.fromkeys(lst,'num') 
{'one': 'num', 'two': 'num', 'three': 'num'}
set类型
set本身是可变的。
1.set中的元素是无序，不重复，不可变的。
2.没有索引和切片。
3.frozenset类型是不可变的set。


Set Methods
isdisjoint(other)

Return True if the set has no elements in common with other. 
issubset(other)

set <= other/set >= other

set < other/set > other

issuperset(other)

union(*others)

set | other | ...    #并集

Return a new set with elements from the set and all others.
intersection(*others)

set & other & ...    #交集

Return a new set with elements common to the set and all others.
difference(*others)

set - other - ...   #差集

Return a new set with elements in the set that are not in the others
symmetric_difference(other)

set ^ other

Return a new set with elements in either the set or other but not both.
copy()

update(*others)

set |= other | ...

Update the set, adding elements from all others.
intersection_update(*others)

set &= other & ...

Update the set, keeping only elements found in it and all others.
difference_update(*others)

set -= other | ...

Update the set, removing elements found in others.
symmetric_difference_update(other)

set ^= other

Update the set, keeping only elements found in either set, but not in both.
add(elem)

Add element elem to the set.
remove(elem)

Remove element elem from the set. Raises KeyError if elem is not contained in the set.
discard(elem)

Remove element elem from the set if it is present.
pop()

Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
clear()