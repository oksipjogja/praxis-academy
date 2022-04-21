# # ## 4.1. if Statements¶
# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('Negative change to zero')
# elif x == 0 :
#     print('Zero')
# elif x == 1:
#     print('Single')
# else :
#     print ('More')

# ## 4.2. for Statements

# # Measure some strings :
# words = ['cat', 'window', 'defenestrate']
# for w in words :
#     print (w, len(w))

# Create a sample collection
# users = {'Hans': 'active', 'Eleonore': 'inactive', '景太郎': 'active'}
# # # # Strategy: Iterate over a copy
# # # for user, status in users.copy().items():
# # #     if status == 'inactive':
# # #         del users[user]
# # # print(status, users)
# # # # Strategy : Create a new collection
# # # active_users = {}
# # # for user, status in users.items():
# # #     if status == 'active' :
# # #         active_users[user] = status
# # # for i in range (5) :
# # #     print (i)
# # #     print (users)

# # #
# # for i in range (5,10):
# #     print (i)


# # list(range(5,10))
# # list(range(0, 10, 3))
# # A = ['Mary', 'had', 'a', 'little', 'lamb']
# # for i in range(len(A)):
# #     print(i)
# #     print(i, A[i])
# #     print(range(10))
# #     print(sum(range(4))) # 0+1+2+3
# # for n in range (2, 10):
# #     for x in range(2, n):
# #         if n % x == 0:
# #             print(n, 'equals', x, '*', n//x)
# #             break
# #     else:
# #         # loop fell through without finding a factor
# #         print(n, 'is a prime number')

# # for num in range(2, 10):
# #     if num % 2 == 0:
# #         print("Found an even number", num)
# #         continue
# #     print("Found an odd number", num)

# # while True:
# #     pass # Busy-wait for keyboard interrupt (Ctrl+C)
# # class MyEmptyClass:
# #     pass
# # def initlog(*args):
# #     pass # Remember to implement this!

# from tkinter.tix import STATUS


# def http_error(status):class point:
#     x : int
#     y : intest"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _ :
#             return "Something's wrong with the internet"

# print(http_error(STATUS))

# from ctypes.wintypes import POINT

# case 401 | 403 | 404:
#     return "Not allowed"
# point is an (x, y) tuple


# class point :
#     x: int
#     y: int
# match point:
#     case point(0, 0):
#         print("Origin")
#     case point(0, y):
#         print(f"Y={y}")
#     case point(x, 0):
#         print(f"X-{x}")
#     case point(x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a POINT")

# # x =(x, y, z)
# # point is an (x, y) # tuple

# class point :
#     x: float
#     y: float
# # point =(x, y)  
# # def func(point):
# match point :
#     case(0, 0):
#         print('origin')
#     case(0, y):class point:
#     x : int
#     y : int
#     case _:
#         raise ValueError('Not A Point')

# class point:
#     x : int
#     y : int
# Point (1, _var)
# Point (1, y=_var)
# # Point (x=1, y=_var)
# # Point (y=_var, x=1)
# def location(point):
#     match point :
#         case []:
#             print("No point")
#         case [point(0, 0)]:
#             print("The origin")
#         case [point(x, y)]:
#             print(f"Single point {x}, {y}")
#         case [point(0, yl), Point(0, y2)]:
#             print(f"Two on the Y axis at {y1}, {y2}")
#         case _:
#             print("Something else")



# match POINT :
#     case POINT(x, y) if x == y:
#         print(f"Y=X at {x}")
#     case POINT(x, y):
#         print(f"Not on the diagonal")

# from enum import Enum
# from tkinter.tix import FileSelectBox

# from jinja2 import FileSystemBytecodeCache
# # class Color(Enum):
# #     RED = 'red'
# #     GREEN = 'green'
# #     BLUE = 'blue'
# # color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
# # match color :
# #     case Color.RED:
# #         print("I see red!")
# #     case Color.GREEN:
# #         print("Grass is green")
# #     case Color.BLUE:
# #         print("I'm feeling the blues : (")
# # # ## 4.7. Defining Functions

# def fib(n):   # write Fibonacci series up to n
#     #"Print a Fibonacci series up to n."
#     a, b = 0, 1
#     while a < n :
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
# # Now call the function we just defined :
# fib(2000)
# fib 
# f = fib
# f(100)
# f = fib 
# print(fib(0))

# # def fib2(n): # return Fibonacci series up to n
# #     #"""Return a list containing the Fibonacci series up to n."""
# #     result = []
# #     a, b = 0, 1
# #     while a < n :
# #         result.append(a)   # see below
# #         a, b = b, a+b
# #     return result

# # f100 = fib2(100)
# # f100

# # def ask_ok(prompt, retries=4, reminder='Please try again!'):
# #     while True :
# #         ok = input(prompt)
# #         if ok in ('y', 'ye', 'yes'):
# #             return True
# #         if ok in ('n', 'no', 'nop', 'nope'):
# #             return False
# #         retries = retries - 1
# #         if retries < 0:
# #             raise ValueError('invalid user response')
# #         print(reminder)   
# i = 5

# # # # def f(arg=i):
# # # #     print(arg)

# # # # i = 6
# # # # f()
# # # # def f(a, L=[]):
# # # #     L.append(a)
# # # #     return L
# # # # print(f(1))
# # # # print(f(2))
# # # # print(f(3))

# # def parrot(voltage, state='a stiff', action='voom', type='Moskow White'):
# #     print("-- This parrot wouldn't", action, end=' ')
# #     print("if you put", voltage, "volts througt it")
# #     print("-- Lovely plumage, the", type)
# #     print("-- It's", state, "!")
# # parrot(100)                                            # 1 positional argument
# # parrot(voltage=1000)                        # import pandas as pd           # 3 positional arguments
# # parrot('a thousand', state='pushing up the daisies')    # 1 positional, 1 keyword
# # parrot(voltage=5.0, action='dead')                      # non-keyword argument after a keyword argument
# # parrot()                                                # required argument missing
# # parrot(voltage=5.0, action='dead')                      # non-keyword argument after a keyword argument
# # parrot(110, voltage=220)                                # duplicate value for the same argument
# # parrot(actor='John Cleese')                             # unknown keyword argument

# # def function(a):
# #     pass

# # function(0, a=0)
# # Traceback (most recent call last):
# #     File "<stdin>", line 245, in <module>
# # TypeError: function() got multiple value for argument 'a'

# from os import link


# def cheeseshop(kind, *arguments, **keyword):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-"*40)
#     for kw in keyword:
#         print(kw, ":", keyword[kw])
# cheeseshop ("Limburger", "It's very runny, sir.",
#             "It's realy very, VERY runny, sir",
#             shopkeeper="Michael Palin",
#             client="John Cleese",
#             sketch="Cheese Shop Sketch")
# def standard_arg(arg):
#     print(arg)
# def pos_only_arg(arg, /) :
#     print(arg)
# def kwd_only_arg(*, arg) :
#     print(arg)
# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)
# standard_arg('badak')
# standard_arg(arg=2)
# pos_only_arg(0.8)
# pos_only_arg(link)
# kwd_only_arg(arg=6)
# # combined_example(1, 2, 3)
# combined_example(1, 2, kwd_only=6)
# combined_example(pos_only=1, standard=2, kwd_only=3)

# import pandas as pd

# def foo(name, /, **kwds):
#     return 'name' in kwds
# # foo(1, **{"name": 2})
# print(foo(1, **{'name':2}))


# def concat(*args, sep="/"):
#     return sep.join(args)
# print(concat("earth", "mars", "venus"))

# print(list(range(3, 9))) # normal call with separate arguments
# args=[2, 6]
# print(list(range(*args))) # call with arguments unpacked from a list

# def parrot(voltage, state='a stiff', action='voom'):
#     print("--This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's'", state, "!")
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

# def make_incrementor(a):
#     return lambda  y:y+a
# f = make_incrementor(42)
# print(f(0))
# print(f(5))

# pairs = [(8, 'eight'), (9, 'nine'), (7, 'seven'), (6, 'six')]
# pairs.sort(key=lambda pair: pair[0])
# print(pairs)

# def my_function():
#     """Do Nothing, but document it.
#     No, really, it doesn't di anything"""
#     pass
# print(my_function.__doc__)

# def f(ham: str, eggs:str = "eggs") -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs
# print(f('spam'))

