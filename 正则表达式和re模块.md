### 字符组
> [157]      
> #一个字符组只匹配一个字符。有几个符合要求的字符就会匹配到多少次。
> **57557**中有5处匹配。

> [0-9] 匹配所有数字
> [a-z] 匹配所有小写字母
> [A-Z] 匹配所有大写字母
> [a-zA-z] 匹配所有字母

有些元字符进入字符组中会失去其特殊意义: ***. | [ ] ( )***

***

### 元字符

字符|	描述
-|-
\ |将下一个字符标记为一个特殊字符、或一个原义字符、或一个 向后引用、或一个八进制转义符。例如，'n' 匹配字符 "n"。'\n' 匹配一个换行符。序列 '\\\\' 匹配 "\\" 而 "\\(" 则匹配 "("。
^	 |匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。
$	|匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。
\*	|匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。
\+	|匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
( )	|标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。要匹配这些字符，请使用 \\( 和 \\)。
{n}	|n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。
{n,}	|n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。
{n,m}	|m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。
?	|	匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 、 "does" 中的 "does" 、 "doxy" 中的 "do" 。? 等价于 {0,1}。当该字符紧跟在任何一个其他限制符 (*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的。非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。例如，对于字符串 "oooo"，'o+?' 将匹配单个 "o"，而 'o+' 将匹配所有 'o'。
.	|匹配除换行符（\n、\r）之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用像"(.\|\n)"的模式。
(pattern)	|匹配 pattern 并获取这一匹配。所获取的匹配可以从产生的 Matches 集合得到，在VBScript 中使用 SubMatches 集合，在JScript 中则使用 $0…$9 属性。要匹配圆括号字符，请使用 '\\(' 或 '\\)'。
(?:pattern)	|匹配 pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用。这在使用 "或" 字符 (\|) 来组合一个模式的各个部分是很有用。例如， 'industr(?:y\|ies) 就是一个比 'industry\|industries' 更简略的表达式。
(?=pattern)	|正向肯定预查（look ahead positive assert），在任何匹配pattern的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如，"Windows(?=95\|98\|NT\|2000)"能匹配"Windows2000"中的"Windows"，但不能匹配"Windows3.1"中的"Windows"。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。
(?!pattern)	|正向否定预查(negative assert)，在任何不匹配pattern的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如"Windows(?!95\|98\|NT\|2000)"能匹配"Windows3.1"中的"Windows"，但不能匹配"Windows2000"中的"Windows"。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。
(?<=pattern)	|反向(look behind)肯定预查，与正向肯定预查类似，只是方向相反。例如，"(?<=95\|98\|NT\|2000)Windows"能匹配"2000Windows"中的"Windows"，但不能匹配"3.1Windows"中的"Windows"。
(?<!pattern)|反向否定预查，与正向否定预查类似，只是方向相反。例如"(?<!95\|98\|NT\|2000)Windows"能匹配"3.1Windows"中的"Windows"，但不能匹配"2000Windows"中的"Windows"。
x\|y	|匹配 x 或 y。例如，'z\|food' 能匹配 "z" 或 "food"。'(z\|f)ood' 则匹配 "zood" 或 "food"。\|是有顺序的，如果前面的规则可以匹配上，则不会再匹配后面的。所以要将更复杂的规则写在前面。
[xyz]	|字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。
[^xyz]	|负值字符集合。匹配未包含的任意字符。例如， '[^abc]' 可以匹配 "plain" 中的'p'、'l'、'i'、'n'。
[a-z]	|字符范围。匹配指定范围内的任意字符。例如，'[a-z]' 可以匹配 'a' 到 'z' 范围内的任意小写字母字符。
[^a-z]	|负值字符范围。匹配任何不在指定范围内的任意字符。例如，'[^a-z]' 可以匹配任何不在 'a' 到 'z' 范围内的任意字符。
\b	|匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	|匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\cx	|匹配由 x 指明的控制字符。例如， \cM 匹配一个 Control-M 或回车符。x 的值必须为 A-Z 或 a-z 之一。否则，将 c 视为一个原义的 'c' 字符。
\d	|匹配一个数字字符。等价于 [0-9]。
\D	|匹配一个非数字字符。等价于 [^0-9]。
\f	|匹配一个换页符。等价于 \x0c 和 \cL。
\n	|匹配一个换行符。等价于 \x0a 和 \cJ。
\r	|匹配一个回车符。等价于 \x0d 和 \cM。
\s	|匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
\S	|匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
\t	|匹配一个制表符。等价于 \x09 和 \cI。
\v	|匹配一个垂直制表符。等价于 \x0b 和 \cK。
\w	|匹配字母、数字、下划线。等价于'[A-Za-z0-9_]'。
\W	|匹配非字母、数字、下划线。等价于 '[^A-Za-z0-9_]'。
\xn	|匹配 n，其中 n 为十六进制转义值。十六进制转义值必须为确定的两个数字长。例如，'\x41' 匹配 "A"。'\x041' 则等价于 '\x04' & "1"。正则表达式中可以使用 ASCII 编码。
\num	|匹配 num，其中 num 是一个正整数。对所获取的匹配的引用。例如，'(.)\1' 匹配两个连续的相同字符。
\n	|标识一个八进制转义值或一个向后引用。如果 \n 之前至少 n 个获取的子表达式，则 n 为向后引用。否则，如果 n 为八进制数字 (0-7)，则 n 为一个八进制转义值。
\nm	|标识一个八进制转义值或一个向后引用。如果 \nm 之前至少有 nm 个获得子表达式，则 nm 为向后引用。如果 \nm 之前至少有 n 个获取，则 n 为一个后跟文字 m 的向后引用。如果前面的条件都不满足，若 n 和 m 均为八进制数字 (0-7)，则 \nm 将匹配八进制转义值 nm。
\nml	|如果 n 为八进制数字 (0-3)，且 m 和 l 均为八进制数字 (0-7)，则匹配八进制转义值 nml。
\un	|匹配 n，其中 n 是一个用四个十六进制数字表示的 Unicode 字符。例如， \u00A9 匹配版权符号 (?)。

***

### 示例

正则|待匹配字符|匹配结果|说明
-|-|-|-
唐. |唐烧酒和唐雪见和堂堂唐家大小姐   |<br>唐烧</br><br>唐雪</br><br>唐家</br>    |
唐.?    |唐烧酒和唐雪见和堂堂唐家大小姐 |<br>唐烧</br><br>唐雪</br><br>唐家</br>    |贪婪匹配
唐.*    |唐烧酒和唐雪见和堂堂唐家大小姐 |唐烧酒和唐雪见和堂堂唐家大小姐 |
唐.{1,2} |唐烧酒和唐雪见和堂堂唐家大小姐 |<br>唐烧酒</br><br>唐雪见</br><br>唐家大</br> |
唐.*?和 |唐烧酒和唐雪见和堂堂唐家大小姐 |<br>唐</br><br>唐</br><br>唐</br>  |?在量词后，变为非贪婪匹配。
唐[烧酒雪见家大小姐]*   |唐烧酒和唐雪见和堂堂唐家大小姐 |<br>唐烧酒</br><br>唐雪见</br><br>唐家大小姐</br>  |
[\d]    |456werfj3  |<br>4</br><br>5</br><br>6</br><br>3</br>   |
[\d]+    |456werfj3  |<br>456</br><br>3</br>   |

***

### 转义符\
在正则表达式中，可以用`'\\n'`匹配`'\n'`。  
而在python中，`'\\n'`打印后本身就是`'\n'`，如果想要打印出`'\\n'`，只能用`'\\\\n'`表示。  
所以在python中正则表达式需要前加`r`，表示整个字符不转义。  
正则	|待匹配字符	|匹配结果	|说明
-|-|-|-
\n	|\n	 |False	|因为在正则表达式中\是有特殊意义的字符，所以要匹配\n本身，用表达式\n无法匹配
\\\\n	|\n	 |True	|转义\之后变成\\，即可匹配
`"\\\\n"`|`'\\n'`	 |True	|如果在python中，字符串中的'\'也需要转义，所以每一个字符串'\'又需要转义一次
`r'\\n'`	|`r'\n'`	 |True	|在字符串之前加r，让整个字符串不转义

***

### re模块
#### 正则表达式修饰符 - 可选标志

修饰符	|描述
-|-
re.I	|使匹配对大小写不敏感
re.L	|做本地化识别（locale-aware）匹配
re.M	|多行匹配，影响 ^ 和 $
re.S	|使 . 匹配包括换行在内的所有字符
re.U	|根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	|该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
***
### 匹配对象的方法
#### group()
可以使用group(*num*) 或 groups() 匹配对象函数来获取匹配表达式。

匹配对象方法	|描述
-|-
group(*num=0*)	|group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。
groups()	|匹配正则表达式整体结果

#### start()
用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0。

#### end()
用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0。

#### span()
返回 (start(), end())。

***
### 查找方法

#### findall()
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#### *findall(string[, pos[, endpos]])*
> *string* : 待匹配的字符串。
> *pos* : 可选参数，指定字符串的起始位置，默认为 0。
> *endpos* : 可选参数，指定字符串的结束位置，默认为字符串的长度。
```python
#查找字符串中所有数字
import re
 
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2)

#输出结果
```
#### *re.findall(pattern, string, flags=0)*
> *pattern*	匹配的正则表达式
> *string*	要匹配的字符串。
> *flags*	标志位
```python
import re

ret = re.findall('\d+','asef2374aer22')
print(ret)

#输出结果
['2374', '22']
```
#### finditer()
#### *re.finditer(pattern, string, flags=0)*
和 findall 类似，在字符串中找到所有正则表达式**匹配结果**，并把它们作为一个迭代器返回。**减少空间复杂度**
```python
import re
 
it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group() )

#输出结果
12 
32 
43 
3
```

#### search()
#### *re.search(pattern, string, flags=0)*
匹配成功re.search方法返回一个匹配的对象，否则返回None。
```python
import re
 
line = "Cats are smarter than dogs";
 
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)
else:
   print "Nothing found!!"

#输出结果:
searchObj.group() :  Cats are smarter than dogs
searchObj.group(1) :  Cats
searchObj.group(2) :  smarter
```

#### match()
#### *re.match(pattern, string, flags=0)*
尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。  
相当于自带 `^` 的search()方法。

***

### 更改（替换/切割）
#### split()
#### *re.split(pattern, string[, maxsplit=0, flags=0])*
按照能够匹配的子串将字符串分割后返回列表。
> *maxsplit* 分隔次数，maxsplit=1 分 隔一次，默认为 0，不限制次数。
```python
>>>import re
>>> re.split('\W+', 'runoob, runoob, runoob.')
['runoob', 'runoob', 'runoob', '']
>>> re.split('(\W+)', ' runoob, runoob, runoob.') 
['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
>>> re.split('\W+', ' runoob, runoob, runoob.', 1) 
['', 'runoob, runoob, runoob.']
 
>>> re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
['hello world']
```

#### sub()
#### *re.sub(pattern, repl, string, count=0, flags=0)*
替换字符串中的匹配项，返回一个新的字符串。
> *pattern* : 正则中的模式字符串。
> *repl* : 替换的字符串，也可为一个函数。
> *string* : 要被查找替换的原始字符串。
> *count* : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
```python
import re
phone = "2004-959-559 # 这是一个国外电话号码"
 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)  
```

#### subn()
#### *re.subn(pattern, repl, string, count=0, flags=0)*
行为与 sub() 相同，但是返回一个元组 (字符串, 替换次数)。

#### compile()
#### *re.compile(pattern[, flags])*
将正则表达式的样式编译为一个 正则表达式对象 （正则对象），可以用于匹配。**减少时间复杂度**
```python
>>>import re
>>> pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
>>> m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
>>> print m
None
>>> m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
>>> print m
None
>>> m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
>>> print m                                         # 返回一个 Match 对象
<_sre.SRE_Match object at 0x10a42aac0>
>>> m.group(0)   # 可省略 0
'12'
>>> m.start(0)   # 可省略 0
3
>>> m.end(0)     # 可省略 0
5
>>> m.span(0)    # 可省略 0
(3, 5)
```
***
### re模块和分组

```python
#通过分组获得真正想要的内容
import re
s = '<a>hellotsj</a>'
ret = re.search('<(\w+)>(\w+)</(\w+)>',s)
print('标签内容为:',ret.group(1)) #获取标签内容
print('文本内容为:',ret.group(2)) #获取文本内容

###输出内容为:
标签内容为: a
文本内容为: hellotsj
```

```python
#在findall()方法中，按照正则表达式中内容进行匹配，但是优先显示的是分组中的内容，而不是整个匹配内容。
>>> import re
>>> s = '<a>hellotsj</a>'
>>> ret = re.findall('>(\w+)<',s)
>>> ret
['hellotsj']
>>> ret = re.findall('(>)(\w+)<',s)
>>> ret
[('>', 'hellotsj')]
```

```python
#取消分组优先只需要将分组写为(:? )
>>> import re
>>> re.findall('\d+(\.\d+)?','1.234*4.3') #匹配小数
['.234', '.3']
>>> re.findall('\d+(?:\.\d+)?','1.234*4.3') #取消分组优先，获得正确匹配结果。
['1.234', '4.3']
```

```python
#split()方法中，分组内的内容被保留
>>>import re
>>> re.split('(\W+)', ' runoob, runoob, runoob.') 
['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']

#取消分组优先的方法同样有效
>>> re.split('(?:\W+)', ' runoob, runoob, runoob.')
['', 'runoob', 'runoob', 'runoob', '']
```

```python
#分组命名 (?P<>)
>>> import re
>>> ret = re.search('>(?P<content>\w+)<','<a>hellotsj</a>')
>>> ret.group('content')
'hellotsj'

#要求标签内容一致才匹配
>>> re.search('<(?P<tab>\w+)>(\w+)</(?P=tab)>','<a>hellotsj</a>').group()
'<a>hellotsj</a>'
```

***
### 正则表达式技巧
#### 匹配整数
```python
import re

ret=re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
print(ret) #['1', '2', '60', '40', '35', '5', '4', '3']
ret=re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
print(ret) #['1', '-2', '60', '', '5', '-4', '3']
ret.remove("")
print(ret) #['1', '-2', '60', '5', '-4', '3']
```