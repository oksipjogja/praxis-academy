## 10.1 OPERATING SYSTEM INTERFACE
import os
print(os.getcwd())
print('/home/donie/praxis-academy')
print(os.system('mkdir learning_os'))
print(os.mkdir('/home/donie/coba'))
print(os.chdir('//home'))
print(os.chdir('..'))
print(dir(os))
print(help(os))
import shutil
print(shutil.copyfile('README.md'))
print(shutil.move('/home/donie/Documents/simple-landing-page', '/home/donie/coba'))
print(shutil.move('/home/donie/coba', '/home/donie/Documents/simple-landing-page'))
print(os.rmdir('/home/donie/coba'))
print(os.listdir('/home/'))


## 10.2 FILE WILDCARDS

import glob
print(glob.glob('*.py'))

## 10.3 COMMAND LINE ARGUMENT

import sys
print(sys.argv)
import argparse
parser = argparse.ArgumentParser(
     prog='top',
     description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

## ERROR OUTPUT REDIRECTION AND PROGRAM TERMINATION

# print(sys.stderr.write('Warning, log file not found starting a new one/n'))

## STRING PATTERN MATCHING

# import re
# print(re.findall(r'\bba[a-z]*', 'baby , bcdotol , bayam, foot , roger , tank , sasori , sanemi')) ## asumsi "b" artinya berawalan. Abjad selajutnya artinya kata yang abjad tsb misal f maka mencari awalan f
# # # print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat ini the hat'))
# # print('tea for too'.replace('too', 'two'))
# print(re.findall(r'\bf[a-z]*', 'mana foot or hand fell fastest'))

## MATHEMATIC

# import math
# print(math.cos(math.pi / 4))
# print(math.log(1024,2))

# import random
# print(random.choice(['apple', 'pear', 'banana']))
# print(random.sample(range(100), 10))  # sampling without replacement
# print(random.random())  # random float
# print(random.randrange(6)) # random integer chosen from range(6)

# import statistics
# data = [2,75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))
# print(statistics.variance(data))

## INTERNET ACCESS

# from urllib.request import urlopen
# with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
#     for line in response:
#         line = line.decode()             
#         if line.startswith('datetime'):
#             print(line.rstrip())  

            # datetime: 2022-01-01T01:36:47.689215+00:00       


# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('kapasansyafak@gmail.com', 'familybuah@gmail.com',
# """to: kapasansyafak@gmail.com
# from: familybuah@gmail.com
# Enaknya Ngopi Dulu Ah
# """)


## DATE AND TIMES
# dates are easyly constructed and formatted
# from datetime import date 
# now = date.today()
# print(now)
# print(now.strftime)
# # dates support calender arithmetic
# birthday = date(1964, 7, 31)
# age = now - birthday
# print(age.days)

## DATE COMPRESSION

# from optparse import Values
# from tkinter import W
# import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))

# t = zlib.compress(s)
# print(len(t))
# print(zlib.decompress(t))
# print(zlib.crc32(s))

# ## PERFORMANCE MEASUREMENT

# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b=b,a,', 'a=1; b=2'). timeit())

## QUALITY CONTROL

def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values) 
import doctest
# doctest.testmod()  # aoutomatically validate the embedded test

import unittest
class TestStatisticalFunctions(unittest.TestCase):

    def test_averange(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]),1),4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()

"""cara compile file python/.py
adalah dengan menulis 'python3 -m py_compile NamaFile.py' lalu klik enter
untuk run folder compile cukup dengan cd __pycache__ lalu ketik python3 namafile (tab) dan enter"""


# dengan cara compile maka akan lebih cepat dalam mengeksekusi bahasa program yakni dengan membuat bytecode