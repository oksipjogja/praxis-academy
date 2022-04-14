def greeting(name):
    print('hello ' + name)
import mymodule
mymodule.greeting('donie')
person1 = {
    'name':'donie',
    'age' : 42,
    'country': 'indonesia'
}
a = mymodule.person1['age']
print(a)
# menamai ulang modul
import mymodule as mx
a = mx.person1['age']
print(a)
# modul bawaan
import platform
x = platform.system()
print(x)
# menggunakan fungsi dir()
import platform
x=dir(platform)
print(x)
# import dari modul
from mymodule import person1
print(person1['age'])
