#!/usr/bin/env python
# encoding: utf-8

#分开打印 'Python' 字符串并在每个字母后面加一个+,去掉所有的t
#列表综合， != 代表不等于，用于比较的情况
print [i + '+' for i in 'Python' if i != 't']

#

#列表的 join 方法
#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串.
#也就是说 join方法只是将列表中的每个元素用指定字符链接起来并生成一个字符串，只生成一个字符串，开头和结尾都没有这个指定分割字符。
t = []
for letter in 'Python':
    if letter == 't':
        continue
    t.append(letter)
print 'The letter is :', t
s = "+ ".join(t)
print 'Current letter is : ', s

#列表的 split() 方法
#Python split()通过指定分隔符对字符串进行切片，生成列表，如果参数num 有指定值，则仅分隔 num 个子字符串)
#str.split(str="", num=string.count(str)).)) str 分隔符，默认为空格。num分割次数
print s.split()

#列表中添加元素的几种方法
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
#直接打印 print list1.append('x')没有返回值,但是已经添加了x

print list1.append('x')
list1.append('x')
print list1
list1.extend(list2)
print list1
list1.insert(0,'y')
print list1
print list1 + list2

#输出
#['P+', 'y+', 'h+', 'o+', 'n+']
#The letter is : ['P', 'y', 'h', 'o', 'n']
#Current letter is :  P+ y+ h+ o+ n
#['P+', 'y+', 'h+', 'o+', 'n']
#None
#['a', 'b', 'c', 'x', 'x']
#['a', 'b', 'c', 'x', 'x', 'd', 'e', 'f']
#['y', 'a', 'b', 'c', 'x', 'x', 'd', 'e', 'f']
#['y', 'a', 'b', 'c', 'x', 'x', 'd', 'e', 'f', 'd', 'e', 'f']
