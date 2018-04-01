
#迭代器是一个定义了next方法的对象
"""而生成器是迭代器的一种，它并没有将所有的值存在内存中
而是在运行时生成值。遍历时需要用for循环或者是传递给可进行迭代的
函数或结构，经常yield一个值"""
#通常用于不需要立刻获取所有结果的情形


def generator_function():
       for i in range(3):
            yield i 


gen = generator_function()
print(next(gen))
#0
print(next(gen))
#1
print(next(gen))
#2

mystring = 'tomorrow'
#next(mystring)
#报错TypeError: 'str' object is not an iterator

"""字符串是可迭代对象，我们需要将它转换为迭代器对象"""
m = iter(mystring)
next(m)
# t
