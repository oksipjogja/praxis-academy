from bdb import effective
import fibo 

# # Fibonacci number module
def fib(n):                 # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
print()
def fib2(n):                # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))

print(fibo.fib(1000))
print(fibo.fib2(100))
print(fibo.__name__)
print(fib(500))
fib = fibo.fib
print(fib(500))

## more on modules
from fibo import fib, fib2
print(fib(500))
from fibo import *
print(fib(500))
# import fibo as fib
# print(fib.fib(500))
from fibo import fib as fibonacci
print(fibonacci(500))

# # # ekseskusi modul menjadi scripts
# # eksekusi melalui terminal

# # # the module search path

# # import platform
# # x = platform.system()
# # print(x)

# # Standard Module
# import sys
# sys.ps1
# sys.ps2
# sys.ps1 ='C> '
import sys
sys.path.append(' /home/donie/praxis-academy /python tutorial/python.py')

# # # # the dir() function
import fibo, sys
dir(fibo)
print(fibo)
print(dir(sys))

a = [1,2,3,4,5]
import fibo
fib = fibo.fib
print(dir())

# ## builtins
import builtins
print(dir(builtins))

#  package
import sound.effects.echo 
from sound.effects import echo
from sound.effects.echo import echofilter
import sound.effects.surround
from sound.effects import *


