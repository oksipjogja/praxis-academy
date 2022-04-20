from functools import partial
from unittest import result


def add(a, b):
    return a + b
plus = add
print(plus(3,4))        # return 7

(lambda a,b: a+b)(3,4)  # return 7
addition = lambda a,b: a+b
print(addition(3,4))  # return 7

authors = ['Donie Umbara', 'Hari Susanto', 'Isac Newton','Neil Amstrong','Adam Sadler','Ursula K Prime']
print(sorted(authors, key=len)) # return list ordered by length of author name
print(sorted(authors, key=lambda name: name.split()[-1])) # return list ordered alphabetically by last name

val = [1,3,3,4,5,6,6]
# multiply every item by two
print(list(map(lambda x: x * 2, val))) # [2, 6, 6, 8, 10, 12, 12]
# take the factorial by multiplying the value so far to the next item
# print(reduce(lambda: x,y: x * y, val, 1))  # error --> 1 *1*2*3*4*5*6

def power(base, exp):
    return base ** exp
cube = partial(power, exp=3)
print(cube(5))  # return 125

def retry(func):
    def retried_function(*args, **kwargs):
        exc = None
        for _ in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                print("Exception raised while calling %s with args: %s, kwargs: %s. retrying % (func, args, kwargs)")
                raise exc
            return retried_function

        # @retry
        # def do_something_risky()
        #  ...
        # retried_function = retry(do_something_risky) # No need to use '@'          

dictionary = ['burung', 'ikan', 'jeruk', 'jempol', 'dongeng', 'gelas']  
def puralize(words):
    for i in range(len(words)):
        word = words[i]
        if word.endswith('s') or word.endswith('x'):
            word += 'es'
        if word.endswith('y'):
            word = word[:-1] + 'ies'
        else:
            word += 's'
        words[i] = word
    def test_pluralize():
        pluralize(dictionary) 
        assert dictionary == ['foxes', 'bosses', 'toeses', 'fairy', 'cup']
    dictionary = ['fox', 'boss', 'orange', 'toes', 'fairy', 'cup']
    def puralize(words):
        result = []
        for word in words:
            word = words[]
            if word.endswith('s') or word.endswith('x'):
                plural = word + ('es')
            if word.endswith('y'):
                plural = word[:-1] + 'ies'
        else:
            plural = + 's'
        result.append(plural)
        return result
    def test_pluralize():
        result = pluralize(dictionary)
        assert result == ['foxes', 'bosses', 'oranges', 'toeses', 'fairies', 'cup']
    def add_bar(items=[]):
        items.append('bar')
        return items
    a = add_bar() # 1 is ['bar']
    a.append('foo')
    add_bar() # return ['bar', 'foo', 'bar']

    from collections import namedtuple
    VerbTenses = namedtuple('Verbtenses', ['past', 'present', 'future'])         
    #versus
    class VerbTenses(object):
        def __init__(self, past, present, future):
            self.past = past
            self.present = present
            self.future = future

class Bus(object):
    passengers = set()
    def add_passenger(self,person):
        self.passengers.add(person)
bus1 = Bus()
bus2 = Bus()
bus1.add_passenger('abe')
bus2.add_passenger('bertha')
bus1.passengers
bus2.passengers