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
>>> s = '我是%s，我有%s分喜欢%s' % ('tsj','100','汉堡')
我是tsj，我有100分喜欢汉堡
>>> s = '我是{}，我有{}分喜欢{}'.format('tsj','100','汉堡')
我是tsj，我有100分喜欢汉堡
>>> s = '我是{2}，我有{1}分喜欢{0}'.format('tsj','100','汉堡')
我是汉堡，我有100分喜欢tsj
>>> s = '我是{name}，我有{score}分喜欢{food}'.format(name='tsj',score='100',food='汉堡')
我是tsj，我有100分喜欢汉堡
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

#### **str.endswith(*suffix[, start[, end]]*)**

见str.startswith()。

#### **str.index(*sub[, start[, end]]*)**
Like find(), but raise ValueError when the substring is not found.

#### **str.isdigit()**
判断是否所有字符都为数字。
#### **str.isalpha()**
判断是否所有字符都为字母。
#### **str.isalnum()**
判断所有字符是否都为数字或字母。
#### **str.lower()**    
将所有字母转换为小写。
#### **str.lstrip(*[chars]*)**
见str.strip()。    
#### **str.replace(*old, new[, count]*)**
将所有*old*替换为*new*，执行*cound*次。
#### **str.rstrip(*[chars]*)**
见str.strip()。
#### **str.split(*sep=None, maxsplit=-1*)**
返回一个列表，列表元素为被*sep*切割的子字符串，共切割*maxsplit*次，生成*maxsplit*+1个元素。*sep*默认为空白，*maxsplit*默认为-1，即不限制切割次数。
```python
>>> '1,2,,3,'.split(',')
['1', '2', '', '3', '']
>>> '1<>2<>3'.split('<>')
['1', '2', '3'])
>>> 'tsj'.split('tsj')
['','']
>>> '          '.split()
[]
```
#### **str.startswith(*prefix[, start[, end]]*)**
判断字符串是否以*prefix*开始，*prefix*位置可以传入一个元祖。
#### **str.strip(*[chars]*)**    
以*chars*中字符组合为标准去掉字符串开头结尾，直到出现不是*chars*中的字符为止。
```python
>>> 'www.example.com'.strip('cmowz.')
'example'
>>> 'www.example.com'.strip('cmowz.e')
'xampl'
>>> 'www.example.com'.strip('cmowz.ea')
'xampl'
```
#### **str.title()**
返回字符串中每个字母首字母大写其余字母小写的形式。除字母外的符号都被定义为分隔符，分隔符两边被定义为字母。
```python
>>> "they're bill's friends from the UK".title()
"They'Re Bill'S Friends From The Uk"
```
python官方给出下面的解决办法:
>A workaround for apostrophes can be constructed using regular expressions:
```python
>>> import re
>>> def titlecase(s):
...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0).capitalize(),
...                   s)
...
>>> titlecase("they're bill's friends.")
"They're Bill's Friends."
```
#### **str.upper()**
将字符串中所有字母转化为大写。
***

### list类型

列表是一个可变的数据类型。
1. 索引index
2. 切片slice

***
### List Methods
#### list.append(x)

在列表末尾添加一个元素，等价于`a[len(a):] = [x]`.

#### list.extend(*iterable*)

对*iterable*中每个元素使用append()方法
```python
>>> ['tsj','zmy'].extend('孙悟空')
['tsj', 'zmy', '孙', '悟', '空']
>>> ['tsj','zmy'].extend(['孙悟空'])
['tsj', 'zmy', '孙悟空']
```
#### list.insert(*i, x*)
在索引为 *i* 的元素前添加一个元素

#### list.remove(*x*)
删除列表中第一个值为*x*的元素，找不到该元素则返回*ValueError*。

```python
#不可以迭代元素进行remove操作
>>> lst = ['one','two','three','four']
>>> for el in lst:
...     lst.remove(el)
>>> lst
['two', 'four']
```
#### list.pop(*[i]*)
删除索引为 *i* 的元素。如果不给定参数，则删除列表中最后一个元素。

#### list.clear()

清空列表 等价于 `del a[:]`。

#### del list[index/slice]
```python
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
```
#### list.index(*x[, start[, end]]*)
返回第一个值为*x*的元素的索引。如果找不到则返回*ValueError*。

#### list.count(*x*)
返回元素出现的次数。

#### list.sort(*key=None, reverse=False*)
对列表中元素进行排序。

#### list.reverse()
翻转列表。
#### list.copy()
返回一个列表的拷贝，等价于` a[:]`.
***


### 元组类型
只读列表，不支持增删改等操作，可以查询。
1. 元组为空或只有一个元素时:
`tu = tuple()   # 空元祖 不可以只用一个空括号表示`
`tu = (3,)   # 只有一个元素时要加‘，’`
2. 索引index
3. 切片slice
4. 元组的不可变指的是子元素不可变。而子元素内部元素是可变的，这取决于子元素是否是可变对象。
```python
>>> game = ('MMO',['以撒'])
>>> game[1].append('巫师3')
>>> game
('MMO', ['以撒', '巫师3'])
>>> game[0] = game[0].lower
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
***
### 字典类型
1. key要求具有可哈希的性质，不可变的数据类型才可以当做键。
2. 初始化字典。
```python
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
```

3. 没有索引和切片
4. 迭代时获取的是key
```python
dic = {'one':1,'two':2}
for i in dic:
       print(i)
'''     
one
two
'''
```
***
### Dic Methods
#### dic.setdefault(*key[, default]*)
如果*key*存在，则返回value。否则，插入元素，value为*default*，并返回*default*。不设置*default*值的情况下value为None。
```python
>>> game = {'MMO':'ff14','单机':'巫师3'}
>>> game.setdefault('养成','明星志愿3')
'明星志愿3'
>>> game
{'MMO': 'ff14', '单机': '巫师3', '养成': '明星志愿3'}
>>> game.setdefault('养成','牧场物语')
'明星志愿3'
>>> game
{'MMO': 'ff14', '单机': '巫师3', '养成': '明星志愿3'}
```
#### dic.pop(*key[, default]*)
如果*key*存在，删除该元素并且返回其value。否则，返回*default*。
如果*key*不存在且*default*为设置，返回*KeyError*错误。

#### del dic[key]
#### dic.clear()
清空字典。
#### dic.popitem()
删除一个元素，并返回一个元组`(key, value)`。删除元素遵照LIFO的顺序。
如果字典为空，则返回一个*KeyError*错误。
#### dic.update(*[other]*)

更新字典，为字典添加新元素，重复的元素则被新的元素替代。返回None。
*other*参数可以是字典，也可以是任何可迭代对象。如果参数为iterable，那么其每个元素都应该是长度为2的可迭代对象。
```python
>>> game = {'MMO':'ff14','单机':'巫师3'}
>>> game.update({'养成':'明星志愿','roguelike':'以撒'}) #传入一个字典
>>> game.update(养成='明星志愿',roguelike='以撒')   #传入关键字
>>> game.update([('养成','明星志愿'),('roguelike','以撒'),('休闲','大富翁')])#传一个包含一个或多个元组的列表 
>>> game.update((['养成','明星志愿'],))   #传一个包含一个或多个列表的元组 
```
### dic.get(*key[, default]*)
如果*key*存在则返回key值，否则返回*default*。如果*default*没有给定，则默认*default*为None。因此这个方法不会返回*KeyError*错误。
```python
>>> dic = {'one':1,'two':2}
>>> dic.get('three',3)
3
>>> dic
{'one': 1, 'two': 2}
>>> dic.get('three') == None
True
```

#### dic.keys() dic.values() dic.items()
返回一个新的view对象(类似列表)表示*keys*，*values*，*items*。
```python
>>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
>>> keys = dishes.keys()
>>> keys
dict_keys(['eggs', 'sausage', 'bacon', 'spam'])
>>> values = dishes.values()
>>> items = dishes.items()
```

view对象是动态的。当字典发生改变时，view也随之改变。
view对象支持yield迭代，也可以使用len()方法。并且有如下几种方法:

* **iter(dictview)**
Return an iterator over the keys, values or items (represented as tuples of (key, value)) in the dictionary.
Keys and values are iterated over in insertion order. This allows the creation of (value, key) pairs using zip(): pairs = zip(d.values(), d.keys()). Another way to create the same list is pairs = [(v, k) for (k, v) in d.items()].
Iterating views while adding or deleting entries in the dictionary may raise a RuntimeError or fail to iterate over all entries.
* **reversed(dictview)**
Return a reverse iterator over the keys, values or items of the dictionary. The view will be iterated in reverse order of the insertion.

```python
>>> n = 0
>>> for val in values:
...     n += val
...
>>> print(n)
504

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
```
***
### set类型
set本身是可变的。
1. set中的元素是无序，不重复，不可变的。
2. 没有索引和切片。
3. frozenset类型是不可变的set。
***

###Set Methods
#### clear()
#### copy()
#### add(*elem*)
添加一个元素。
#### remove(*elem)
删除一个元素。如果元素不存在则返回*KeyError*错误。 
#### discard(*elem)
如果元素存在则删除该元素。
#### pop()
删除一个任意的元素 如果set为空则返回*KeyError*错误。

#### 其他set方法
函数|	表达式|	描述
-|-|-
isdisjoint(*other*) ||判断是否有交集
<br>issubset(*other*)</br><br>issuperset(*other*)</br>	|<br>set <= other</br><br>set >= other</br><br>set < other</br><br>set > other</br>	|判断是否为子集
<br>union(**others*)</br><br>update(**others*)</br>|	<br>set \| other \| ...<br> <br>set \|= other \| ...</br>	|返回所有集合的并集。
<br>intersection(**others*)</br><br>intersection_update(**others*)</br>	|<br>set & other & ... </br>   <br>set &= other & ...</br>	|返回各个集合的交集只保留该集合和其他集合的交集元素。返回新的集合。
<br>difference(**others*)</br><br>difference_update(**others*)</br>	|<br>set - other - ...</br>   <br>set -= other | ...</br>	|返回该集合中存在但其他集合中不存在的差集。移除其他集合中存在的元素，返回新的集合。
<br>symmetric_difference(*other*)</br><br>symmetric_difference_update(*other*)</br>	|<br>set ^ other</br> <br>set ^= other</br>	|返回该集合及其他集合中独有的元素。返回一个集合，只保留其他集合中独有的元素。
