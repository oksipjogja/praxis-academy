a = 2;
b = 2
print (a+b)
a = 4.5;
b = 2
print(a+b)

c = -50;
d = 6;
e = 4;
f = 5;
g = -57.5;
if c-f*d/e == g:
    print("Benar")
else:
    print("Salah")

width = 50;
height = 20;
print(width*height)

a = 4;
b = 3.75;
c = 1
print (a*b-c)  

a = 5;
b = 7;
print(a/b)

a = 17;
b = 3;
print(a//b)

a = 17;
b = 3;
print(b%a)

a = 5
b = 3
c = 2
print(a*b+c)

a = 5 # 5 squared
c = 2
print(a**c)

a = 2 # 5 squared
c = 7 # 2 to the power of 7
print(a**c)

api_itu_panas = False
if api_itu_panas :
    print('jangan dipegang')
else :
    print('kebakar')


tax = 12.5 / 100
price = 100.50;
print (tax*price)
# y = tax*price
print (price+y)
# x = price+y
print(round(x,1))


print ('spam eggs')  # single quotes
print ('doesn\'t')  # use \' to escape the single quote...
print ("doesn't" ) # ...or use double quotes instead
print ('"Yes," they said.')
print ("\"Yes,\" they said.")
print ('"Isn\'t," they said.')

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

prefix = 'py'
print (prefix + 'thon')

print(3*'un'+'ium')

print ('py' 'thon')

text = 'donie memang ganteng dan imut banget'
print(text)

word = 'Python'
print (word [0])
print(word [5])
print(word [-1])
print(word [-2])
print(word [-6])# 
print(word [0:2])
print(word [2:5])
print (word [:2])
print (word [4:])
print (word [-2:])

print (word [:2] + word [2:])
print (word [:4] + word [4:])
print (word [4:42])
# print (word [42:])
print ('J' + word [1:])

s = 'supercalifragilisticexpialidocious'
print (len(s))

squares = [1, 4, 9, 6, 25]
print (squares)
print (squares [0]) # indexing returns the item
print (squares [-1])
print (squares [-3:]) # slicing returns a new list
print (squares [:])
print (squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125] # something's wrong here
print (4**3) # the cube of 4 is 64, not 65!
cubes[3] = 64 # replace the wrong value
print (cubes)

cubes.append(216) # add the cube of 6
cubes.append(7**3) # add the cube of 7
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some value
letters[2:5]=['C', 'D', 'E']
print (letters)

letters [2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters [:] = []
print (letters)

letters = ['a', 'b', 'c', 'd'] 
print (len (letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x [0][1])

# Fibonacci series :
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print (a)
    a, b = b, a+b
i = 256*256
print ('the value of i is', i)
a, b = 0, 1
while a < 1000:
    print(a, end=',') 
    a, b = b, a+b