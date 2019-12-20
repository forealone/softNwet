


#输出
print('100 + 200 =', 100 + 200)

#输入
name = input('please enter your name: ')

#字符串的合并
a='testing'+'test'

#转义字符\
'I\'m \"OK\"'

#浮点数1.2e3 16进制0xff00

#换行\n 制表符\t 不转义r"内容"
#另一种换行
print("'line1
	...line2'")
	
#true false的运算 and or not
#空值none
	
#除法/ 地板除// 余数%
		
#字符编码
#字符转数字ord('A')  编码转字符chr(65) 或'/编码' 
#10转16进制hex()
#直接输入16进制编码出字符'\u4e2d\u6587'
#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'

#或者通过encode()方法可以编码为指定的bytes，例如：
'ABC'.encode('ascii')
'中文'.encode('utf-8')

#在bytes中，无法显示为ASCII字符的字节，用\x##显示。反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

#要计算str包含多少个字符，可以用len()函数：[
len('ABC')

#Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#格式化和占位符
 'Hi, %s, you have $%d.' % ('Michael', 1000000)
 #整数%d 浮点数%f 字符串%s 十六进制%x
 #格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
 print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
#%需要转义的话输入%%
	#另一种转义format()
	'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)

#有序集合list和tuple
 classmates = ['Michael', 'Bob', 'Tracy']  #list L=[]
 #len()可获得list的元素个数
 #索引访问list元素
 classmate[0]  #取0,1,2或者-1,-2,-3取倒数
 #追加元素
 classmates.append('Adam')
 classmates.insert(1, 'Jack')
classmates.pop()  #删除元素。删除指定元素在括号内加数字
classmates[1] = 'Sarah'  #直接赋]值
#list可嵌套、可有多个数据类型
 s = ['python', 15}, ['asp', 'php'], true]
 s[2][1]
 
 classmates2 = ('Michael', 'Bob', 'Tracy')  #元组tuple里的元素不可修改
 #定义tuple中如果只有一个元素，写成 t = (1,)
 
 #条件判断
 age = 3
if age >= 18:  #不要少冒号
    print('your age is', age)
    print('adult')  #会执行所有缩进语句
elif age >= 6:
    print('teenager')
else:
    print('your age is', age)
    print('kid')

#str转整数int()

#循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#range(101)生成0开始整数序列

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#break跳出循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#continue跳过当前循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

#字典dict (key必须是不可变对象)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  #可直接给key赋值d['Jack'] = 88
d['Michael']  #查询结果95

d.get('Thomas', -1)  #如果对应value不存在，返回指定值

#另一种dict：set()
s = set([1, 2, 3])  #以一个list作为set的key，set不会有重复值，无序
s.add(4)  #添加和删除key
s.remove(4)
#两个set可做交集&和并集|

a = ['c', 'b', 'a']  #list的排序
a.sort()

#函数 绝对值abs() 最大值max()
数据类型转换int() str() float() bool()
#定义函数
def my_abs(x):
    if x >= 0:
        return x  #一旦执行到return时，函数就执行完毕返回结果。如返回空值return none
    else:
        return -x
#如果已经把my_abs()的函数定义保存为abstest.py文件，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数

def nop():  #定义一个什么都不做的空函数
    pass  #相当于占位符，让程序先运行下去
    
#函数返回多个值
import math  #导入math包，可使用sin等函数

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
    
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)  #结果151.96152422706632 70.0。本质其实是一个tuple，括号被省略

#函数的参数
def power(x, n=2):  #求x的n次方，n默认等于2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#定义一个可变参数
def calc(*numbers):  #加*，这样调用函数的时候参数不用是一个list，输入多个值即可
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
    
nums = [1, 2, 3]  #或者有一个list，作为参数传入时可以简化
calc(*nums)

#关键字参数
def person(name, age, **kw):  #允许传入0或任意个含参数名的参数(组成一个dict)
    print('name:', name, 'age:', age, 'other:', kw)
    
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)  #**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数

def person(name, age, *, city, job):  #如果要限制关键字参数的名字，就可以用命名关键字参数，*后面的参数被视为命名关键字参数。
    print(name, age, city, job)
    
def fact(n):  #n的阶乘
    if n==1:
        return 1
    return n * fact(n - 1)

#切片    
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[0:3]  #切片操作符，取list的一部分

L[::5]  #每隔5个数取一个

 (0, 1, 2, 3, 4, 5)[:3]  #tuple也可以
 
  'ABCDEFG'[:3]  #字符串也可做切片
  
#python的迭代算法for...in循环可用于list tuple dict 字符串等
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
#对value迭代for value in d.values()
#同时对key和value迭代for k, v in d.items()

from collections import Iterable
isinstance('abc', Iterable) # 通过collections模块的iterable类型判断str是否可迭代，返回结果true false

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)  #enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
    
list(range(1, 11))  #列表生成式 生成包含1~10的list

[x * x for x in range(1, 11) if x % 2 == 0]  #求偶数的平方

[m + n for m in 'ABC' for n in 'XYZ']  #两层循环

#显示当前目录下所有目录和文件
import os 
[d for d in os.listdir('.')] # os.listdir可以列出文件和目录

#for循环可以同时使用多个变量(比如迭代dict的key和value)
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
     print(k, '=', v)
#所以列表生成式可这么写  
 [k + '=' + v for k, v in d.items()]
 
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]  #把list所有字符变小写

#生成器可以在循环的过程中不断推算出后续的元素呢，不必创建完整的list，从而节省大量的空间。
L = [x * x for x in range(10)]   #列表生成式是[]

g = (x * x for x in range(10))  #生成器generater

for n in g:
    print(n)   #一个一个打印出来g的元素还可使用next(g)

#定义一个斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

#ptint替换成yield就是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
    
#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
     try:
       x = next(g)
       print('g:', x)
     except StopIteration as e:
       print('Generator return value:', e.value)
       break

#可以直接作用于for循环的对象统称为可迭代对象：Iterable。(集合数据类型和生成器)
#可以使用isinstance()判断一个对象是否是Iterable对象
isinstance('abc', Iterable)   #返回true

#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
...     return x * x
...
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#一个str转换为int的函数
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

##一个str转换为int的函数


#filter()函数用于过滤序列。
#和map()类似，filter()也接收一个函数和一个序列。filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))




