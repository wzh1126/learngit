from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)
"""装饰器会重写我们函数的名字和文档，@wraps接受一个函数进行装饰，它有复制函数的名称注释文档
参数列表等功能。可以让我们在装饰器里面访问被装饰的函数的属性。"""