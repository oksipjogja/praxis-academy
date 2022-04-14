## REFERENSI
# 'r' => read - default value (open a file for reading)
# 'a' => append - (open file for appending,creates the file if it doesn't exist)
# 'w' => write - (open file for writing)
# 'x' => create -(create the specified file, returns an error)
# 't' => text 
# 'b' => binary

## OPEN FILE
f = open('demofile.txt', 'r')
print(f.read())

# Read only part of the file
f = open('demofile.txt', 'r')
print(f.read(5))

# read line
f = open('demofile.txt', 'r')
print(f.readline())
print(f.readline())

# looping through the lines of the file, you can read the whole file, line by line
f = open('demofile.txt', 'r')
for x in f:
    print(x)

## CLOSE FILE
# f = open('demofile.txt', 'r')
# print(f.readline())
# f.close()

f = open('demofile2.txt', 'a')
f.write('Now the file has more content')
f.closed
# open and read the file after the appending
f = open('demofile2.txt', 'r')
print(f.read())

f = open('demofile3.txt', 'w')
f.write('Woops! I have delete the contenct!')
f.close()
 # open and read the file after the appending
f = open('demofile3.txt', 'r')
print(f.read())

# # CREATE A NEW FILE
# f = open('myfile.txt', 'x')

## DELETE A FILE
import os
os.remove('demofile3.txt')
import os
if os.path.exists('demofile3.txt'):
    os.remove('demofile3.txt')
else :
    print('The file does not exist')