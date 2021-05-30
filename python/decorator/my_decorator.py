# def my_decorator(func):
#     '''Decorator function'''
#     def wrapper():
#         '''Return string'''
#         return 'F-I-B-N-C-I'
#     return wrapper
def get_param(start, end):
    def munch_decorator(func, start, end):
        def wrapper(start, end):
            fibo_str = func()
            fibo_list = list(fibo_str)
            for i in range(start, end + 1):
                fibo_list[i] = 'x'

            return ''.join(fibo_list)
        return wrapper
    return munch_decorator

@get_param
def pfib():
    return 'Fibonacci'

print(pfib(1,2))


# def name_decorator(func):
#     def wrapper(name):
#         name = func(name)
#         name += ' YO!!'
#         return name
#     return wrapper

# @name_decorator
# def say_my_name(name):
#     return name

# print(say_my_name('Abrar'))


