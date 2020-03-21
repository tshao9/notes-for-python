### **循环语句/异常处理后接else语句**
如果else子句紧接在循环语句的后面，那么在以下两种情况将会执行else子句的代码：
 
当循环体没有执行break的时候，即循环体正常结束
```python
print("两次输入机会")
for i in range(2):
        num = int(input("请输入一个数字："))
        if 10 == num:
                print("10 == num,触发break，不会执行else子句")
                break
else:
       print("循环体没有执行break语句，执行else子句")
```
当while循环体完全不执行时也会执行紧跟在后面的else子句
```python
while False:
       pass
else:
        print("循环体不执行，我也会执行")
```
当没有发生异常的时候会执行紧跟在异常处理代码后面的elsSe子句
```python
a=10
b=0
try:
        c = b/ a
        print(c)
except  IOError ,ZeroDivisionError:
        pass
else:
        print ("no error")
print("done")
```
***
### **函数返回多个返回值**

当return多个返回值时，返回的是一个元祖。
```python
>>> def test():
...     return '1','2','3'
>>> test = test()
>>> test
('1', '2', '3')
```
