### Built-in Functions

<i>

a-c|d-h|h-m|m-r|r-z
:---|:---|:---|:---|:---
<br>**abs()**</br><br>返回int/float的绝对值</br>|<br>**delattr()**</br><br></br>|<br>**hash()**</br><br>获取一个对象的哈希值</br>|<br>**memoryview()**</br><br></br>|<br>**set()**</br><br>创建一个set类型</br>
<br>**all(iterable)**</br><br>当iterable中全部元素为True时返回True</br>|<br>**dict()**</br><br>创建一个字典（见dict部分</br>|<br>**help()**</br><br>用于查看函数或模块用途的详细说明</br>|<br>**min()**</br><br>返回给定参数或iterable的最小值</br>|<br>****</br><br></br>
<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>
<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>
<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>
<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>
<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>
<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>
<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>
<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>|<br>****</br><br></br>


</i>


	setattr()
any(iterable)
当iterable中任意元素为True时返回True
	dir()
不带参数时，返回当前范围内的变量、方法和定义的类型列表。带参数时，返回参数的属性、方法列表。
	hex()
返回一个int的十六进制字符串
>>>hex(255)
'0xff'
	next()
获得生成器的下一个值
	slice()
>>> lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> s = slice(1,8,2)
>>> lst[s]
['1', '3', '5', '7']
ascii()	divmod(a,b)
返回一个包含商和余数的元组(a // b, a % b)	id()
获取对象的内存地址
	object()	sorted()
见下
bin()
返回一个int的二进制字符串
>>>bin(10)
'0b1010'
	enumerate(sequence, [start=0])
将一个可遍历的数据对象组成为一个索引序列，下标从start开始
>>>l = ['a', 'b']
>>>list(enumerate(l, start=1))
[(1, 'a'), (2, 'b')]
	input()
输入
	oct()
返回一个int的八进制字符串
>>>oct(10)
'0o12'
	staticmethod()
bool()
返回数据的布尔类型	eval(expression[, globals[, locals]])
执行一个字符串表达式并返回表达式的值。globals 必须是一个字典对象。locals 可以是任何映射对象。
	int()
将数据转换为int型
	open()
打开一个文件	str()
返回对象的string格式

breakpoint()	exec()
见下	isinstance()	ord()
返回一个字符对应的 ASCII 或者 Unicode 数值
	sum(iterable, /, start=0)
求和
bytearray()
返回一个新字节数组，元素可变
	filter()	issubclass()	pow(x, y[, z])
返回pow(x,y) %z
	super()
bytes()
返回一个不可变的bytes对象。
	float()
将数据转换为float型	iter()
生成迭代器	print()
输出	tuple()
callable()
检查对象是否可调用	format()
见下
	len()
返回对象的长度
	property()	type()
见下
chr()
返回一个ASCII 或者 Unicode 数值对应的字符	frozenset()
创建一个不可变set
	list()	range()
创建一个整数列表	vars()
classmethod()	getattr()	locals()
以字典的类型返回当前位置全部局部变量
	repr()
原样输出字符串
>>>s = 'RUNOOB'
>>> repr(s)
"'RUNOOB'"	zip()
见下
compile()
见下	globals()
以字典的类型返回当前位置全部全局变量
	map()	reversed()
将一个可翻转对象进行翻转
返回一个迭代器	__import__()
complex()
见下
	hasattr()	max()
返回给定参数或iterable的最大值
	round(x.[,n])
见下	





compile(source, filename, mode[, flags[, dont_inherit]])
将一个字符串编译为字节代码，返回表达式执行结果。
source -- 字符串或者AST（Abstract Syntax Trees）对象
filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
mode -- 指定编译代码的种类。可以指定为 exec[逻辑语句]，eval[求值表达式]，single[交互代码]
flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象
flags和dont_inherit是用来控制编译源码时的标志
>>>str = "for i in range(3): print(i)" 
>>> c = compile(str,'','exec')   # 编译为字节代码对象 
>>> c
<code object <module> at 0x10141e0b0, file "", line 1>
>>> exec(c)
0
1
2
​
>>> str = "3 * 4 + 5"
>>> a = compile(str,'','eval')
>>> eval(a)
17
​
s = "content = input('请输入你的名字:')"
c = compile(s,'','single')  #交互代码用single
exec(c) #这里没有single()，执行要用exec()
print(content)
​
#输出结果:
请输入你的名字:tsj
tsj
complex()
class complex([real[, imag]])
Return a complex number with the value real + imag*1j or convert a string or number to a complex number.
>>>complex(1, 2)
(1 + 2j)
 
>>> complex(1)    # 数字
(1 + 0j)
 
>>> complex("1")  # 当做字符串处理
(1 + 0j)
 
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
>>> complex("1+2j")
(1 + 2j)
exec(object[, globals[, locals]])
相比于 eval()，exec()可以执行更复杂的 Python 代码。并且exec()没有返回值。
>>>exec('print("Hello World")') # 单行语句字符串
Hello World
​
>>> exec("print ('runoob.com')")    #  多行语句字符串
runoob.com
​
>>> exec ("""for i in range(3):
...     print ("iter time: %d" % i)
... """)
iter time: 0
iter time: 1
iter time: 2
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
func()
​
#输出结果
60
33
34
format(value[, format_spec])
#指定对齐方式，<是左对齐， >是右对齐，^是居中对齐
print(format('test', '<20'))
print(format('test', '>20'))
print(format('test', '^20'))
​
#整形数值可以提供的参数有 'b' 'c' 'd' 'o' 'x' 'X' 'n' None
>>> format(3,'b') #转换成二进制
'11'
>>> format(97,'c') #转换unicode成字符
'a'
>>> format(11,'d') #转换成10进制
'11'
>>> format(11,'o') #转换成8进制
'13'
>>> format(11,'x') #转换成16进制 小写字母表示
'b'
>>> format(11,'X') #转换成16进制 大写字母表示
'B'
>>> format(11,'n') #和d一样
'11'
>>> format(11) #默认和d一样
'11'
​
#浮点数可以提供的参数有 'e' 'E' 'f' 'F' 'g' 'G' 'n' '%' None
>>> format(314159267,'e') #科学计数法，默认保留6位小数
'3.141593e+08'
>>> format(314159267,'0.2e') #科学计数法，指定保留2位小数
'3.14e+08'
>>> format(314159267,'0.2E') #科学计数法，指定保留2位小数，采用大写E表示
'3.14E+08'
>>> format(314159267,'f') #小数点计数法，默认保留6位小数
'314159267.000000'
>>> format(3.14159267000,'f') #小数点计数法，默认保留6位小数
'3.141593'
>>> format(3.14159267000,'0.8f') #小数点计数法，指定保留8位小数
'3.14159267'
>>> format(3.14159267000,'0.10f') #小数点计数法，指定保留10位小数
'3.1415926700'
>>> format(3.14e+1000000,'F')  #小数点计数法，无穷大转换成大小字母
'INF'
​
'''
g的格式化比较特殊，假设p为格式中指定的保留小数位数，先尝试采用科学计数法格式化，
得到幂指数exp，如果-4<=exp<p，则采用小数计数法，并保留p-1-exp位小数，
否则按小数计数法计数，并按p-1保留小数位数
'''
>>> format(0.00003141566,'.1g') #p=1,exp=-5 ==》 -4<=exp<p不成立，按科学计数法计数，保留0位小数点
'3e-05'
>>> format(0.00003141566,'.2g') #p=1,exp=-5 ==》 -4<=exp<p不成立，按科学计数法计数，保留1位小数点
'3.1e-05'
>>> format(0.00003141566,'.3g') #p=1,exp=-5 ==》 -4<=exp<p不成立，按科学计数法计数，保留2位小数点
'3.14e-05'
>>> format(0.00003141566,'.3G') #p=1,exp=-5 ==》 -4<=exp<p不成立，按科学计数法计数，保留0位小数点，E使用大写
'3.14E-05'
>>> format(3.1415926777,'.1g') #p=1,exp=0 ==》 -4<=exp<p成立，按小数计数法计数，保留0位小数点
'3'
>>> format(3.1415926777,'.2g') #p=1,exp=0 ==》 -4<=exp<p成立，按小数计数法计数，保留1位小数点
'3.1'
>>> format(3.1415926777,'.3g') #p=1,exp=0 ==》 -4<=exp<p成立，按小数计数法计数，保留2位小数点
'3.14'
>>> format(0.00003141566,'.1n') #和g相同
'3e-05'
>>> format(0.00003141566,'.3n') #和g相同
'3.14e-05'
>>> format(0.00003141566) #和g相同
'3.141566e-05'
lambda 
lambda [arg1 [,arg2,.....argn]]:expression
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )
​
#也可以把匿名函数作为返回值返回
>>> def build(x, y):
...     return lambda: x * x + y * y
>>> build(1,2)
<function build.<locals>.<lambda> at 0x00000211699FF0D0>
​
#lambda也可以使用可变参数
fn = lambda *args: max(args)
round()

round(x,[,n])
返回一个浮点数的四舍五入值，默认到小数点后n位。n默认为0，即返回一个int型。

在python2.7的doc中，round()的最后写着，保留值将保留到离上一位更近的一端（四舍六入），如果距离两端一样远，则保留到离0远的一边。所以round(0.5)会近似到1，而round(-0.5)会近似到-1。

但是到了python3.5的doc中，文档变成了，如果距离两边一样远，会保留到偶数的一边。比如round(0.5)和round(-0.5)都会保留到0，而round(1.5)会保留到2。

并且round()有浮点数精度准确的问题。所以对精准度要求较高时不要用round()。
sorted()
sorted(iterable, *, key=None, reverse=False)


sorted() 函数对所有可迭代的对象进行排序操作。

sort 与 sorted 区别：

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

iterable -- 可迭代对象。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
#只利用key进行倒序排序
>>> example_list = [5, 0, 6, 1, 2, 7, 3, 4]
>>> sorted(example_list, key=lambda x: x*-1)
[7, 6, 5, 4, 3, 2, 1, 0]
type（）

class type(object)
class type(name, bases, dict)
With one argument, return the type of an object. The return value is a type object.
The isinstance() built-in function is recommended for testing the type of an object, because it takes subclasses into account. 
isinstance() 与 type() 区别：
    type() 不会认为子类是一种父类类型，不考虑继承关系。
    isinstance() 会认为子类是一种父类类型，考虑继承关系。
zip()

zip(*iterables)

将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。
利用 * 号操作符，可以将元组解压为列表。
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 返回一个对象
>>> zipped
<zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c))              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
 
>>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]