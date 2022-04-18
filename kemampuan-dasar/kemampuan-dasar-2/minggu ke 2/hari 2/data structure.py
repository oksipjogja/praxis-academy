## MORE ON LIST
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count("tangerine")
fruits.index('banana')
fruits.index('banana', 4)   # Find next banana starting a position 4
fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)
## USING LISTS AS STACKS
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
stack.pop()
stack.pop()
print(stack)
## USING LIST AS QUEUES
from collections import deque 
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")       # Terry arrives
queue.append("Graham")      # Graham arrives
print(queue.popleft())      # The first to arrives now leaves
print(queue.popleft())      # The second to arrive now leaves
print(queue)                # Remaining queue in order of arrival
## LIST COMPREHENSION
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
squares=[(x, y) for x in [1,2,3] for y in [3,1,4] if x !=y]
print(squares)
combs = []
for x in [1,2,3]:
    for y in[3,1,4]:
        if x != y:
            combs.append((x,y))
print(combs)
vec = [-4,-2,0,2,4]
# create a new list with the value doubled
[x*2 for x in vec]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
# apply a function to all the elements
[abs(x) for x in vec]
# call a method on each element
freshfruit = [' banana ', ' loganberry', 'passion fruit']
[weapon.strip() for weapon in freshfruit]
# create a list of 2-tuples like (number, square)
[(x,x**2) for x in range(6)]
# the tuples must be parenthesized, otherwise an error is raised
[x, s**2 for x in range(6)]
# flatten a list using a listcomp with two 'for
vec = [[1,2,3],[4,5,6],[7,8,9]]
print([num for elem in vec for num in elem])
from math import pi
[str(round(pi, i)) for i in range(1,6)]
## NESTED LIST COMPREHENSIONS
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
    
print(transposed)
list(zip(*matrix))
## THE DEL STATEMENT
a = [-1,1,66,25,333,333,1234.5]
del a[0]
a
a
del a[:]
a
del a
##   TUPLES AND SEQUENCES
t=12345, 54321, 'hello!'
t[0]
t
# Tuples are immutable :
u = t, (1,2,3,4,5)
u
t[0]= 88888
# but they can contain mutable objects :
v=([1,2,3],[3,2,1])
v
empty = ()
singleton='hello' # <---note trailing comma
len(empty)
len(singleton)
singleton
x, y, z = t
## SETS
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
'orange' in basket
'crabgrass' in basket
# Demonstrate set operations on unique letter from two words
a = set('abracadabra')
b = set('alacazam')
a
a-b
a|b
a&b
a^b
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
## DICTIONARIES
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
tel['jack']
del tel['sape']
tel['irv'] = 4127
tel
list(tel)
sorted(tel)
'guido' in tel
'jack' not in tel
dict([('sape', 4139),('guido', 4127), ('jack', 4098)])
{x: x**2 for x in (2,24,6)}
## LOOPING TECHNIQUE
knight = {'galland': 'the pure', 'robin': 'the brave'}
for k,v in knight.items():
    print(k,v)
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holly grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
for i in reversed(range(1,10,2)):
    print(i)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
filtered_data
## MORE ON CONDITION
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null
## COMPARING SEQUENCES AND OTHER TYPES
(1,2,3,)                < (1,2,4)
[1,2,3]                 < [1,2,4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1,2,3,4)               < (1,2,4)
(1,2)                   < (1,2,-1)
(1,2,3)                == (1.0, 2.0, 3.0)
(1,2,('aa','ab'))       < (1,2, ('abc', 'a'),4)