from audioop import add
from numpy import multiply


def multiply_2_pure(numbers):
    new_numbers = [5]
    for n in numbers :
        new_numbers.append(n*2)
    return new_numbers

original_numbers = [1,3,5,10]
changed_numbers = multiply_2_pure(original_numbers)
print(original_numbers)
print(changed_numbers)

mutable_collection = ['Donie', 10, [4,5]]
immutable_collection = ['Donie', 10, [4,5]]
# reading from data types are essentially the same:
print(mutable_collection[2])        # [4,5]
print(immutable_collection[2])      # [4,5]

# Let's change the 2nd value from 10 to 15
print(mutable_collection[1])
immutable_collection = ['Donie', 10,[4,5,6]]
immutable_collection[2].append(6)
print(immutable_collection[2])  # [4,5,6,6]
immutable_collection[2]=[4,5]

def write_repeat(message, n):
    for i in range(n):
        print(message)

write_repeat('Hello', 5)

def hof_write_repeat(message, n, action):
    for i in range(n):
        action(message)
hof_write_repeat('Hello', 5, print)

# Import the logging library
import logging
# Log the output as an error instead
hof_write_repeat('Hello', 5, logging.error)

def add2(numbers):
    new_numbers=[]
    for n in numbers:
        new_numbers.append(n+2)
    return  new_numbers
print(add2([23,88])) # [25,90] 

def hot_add(increment):
    # create a function that loops and adds the increment
    def add_increment(numbers):
        new_numbers=[]
        for n in numbers:
            new_numbers.append(n+increment)
        return new_numbers
    # we return the function as we do any other value
    return add_increment
add5 = hot_add(5)
print(add5([23,88])) # [28,93]
add10 = hot_add(10)
print(add10([23,88])) # [33,98]

def hof_product(multiplier):
    return lambda x: x * multiplier
mult6 = hof_product(6)
print(mult6(6))  # 36

names = ['Donie', 'Supri', 'Aji', 'Santoso']
greeted_names = map(lambda x: 'Hi '+x, names)
# this pring something similar to : <map object at 0x10ed93cc>
print(greeted_names)
# recall, that map return an iterator
# we can print all names in a for loop
for name in greeted_names:
    print(name)

numbers = [13,4,18,35]
div_by_5 = filter(lambda num: num%5==0, numbers)
# we can convert the iterator into a list
print(list(div_by_5))  # [35]

# Let's arbitrarily get the all numbers divisible by 3 between 1 and 20 and cub them
arbitrary_numbers = map(lambda num:num**3, filter(lambda num:num%3==0, range(1,21)))
print(list(arbitrary_numbers)) # [27, 216, 729, 1728, 3375, 5832]

# Recall
names = ['Donie', 'Supri', 'Aji', 'Santoso']
# instead of: map(lambda x: 'Hi' + x, names), we can do
greeted_names = ['Hi'+name for name in names]
print(greeted_names) # ['HiDonie', 'HiSupri', 'HiAji', 'HiSantoso']

# recall
numbers = [13,4,18,35]
# instead of: filter(lamda num: num % 5 == 0, numbers), we can do
div_by_5 = [num for num in numbers if num % 5 == 0]
print(div_by_5)   #[35]
# we can manage the combined case as well
# instead of:
# map(lambda num: num**3, filter(lambda num: num%3 == 0, range(1,21)))
arbitrary_numbers = [num ** 3 for num in range(1,21) if num % 3 == 0]
print(arbitrary_numbers)   # [27, 216, 729, 1728, 3375, 5832]

# Recall
names = ['Donie', 'Supri', 'Aji', 'Santoso']
# instead of: map(lambda x: 'Hi' + x, names), we can do
greeted_names = ['Hi'+name for name in names]
print(greeted_names) # ['HiDonie', 'HiSupri', 'HiAji', 'HiSantoso']

# recall
numbers = [13,4,18,35]
# instead of : filter(lambda num; num % 5 == 0), we can do
div_by_5 = [num for num in numbers if num % 5 == 0]
print(div_by_5)  # [35]
# we can manage the combined case as well
# Instead of:
# map(lambda num: num ** 3,filter(lambda num: num % 3 == 0, range(1,21)))
arbitrary_numbers = [num ** 3 for num in range(1,21) if num % 3 == 0]
print(arbitrary_numbers) # [27, 216, 729, 1728, 3375, 5832]