# import reprlib
# print(reprlib.repr(set('supercalifragilisticexpiallidocious')))
# import pprint
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
# pprint.pprint(t, width=30)

# import textwrap
# doc = """The Wrap() method is just like fill() except that it returns 
# a list of string instead of one big string with newlines to separate
# the wrapped lines."""
# print(textwrap.fill(doc, width=40))

# import locale
# # locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# conv = locale.localeconv()
# x = 1234567.8
# locale.format("%d", x, grouping=True)
# locale.format_string("s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)

# from string import Template
# from this import d
# t = Template('${village} folk send $$10 to $cause.')
# print(t.substitute(village='Nottingham', cause='the ditch fund'))

## --> hasilnya error t = Template('Return the $item to $owner.')
                    # d = dict('item='unladen swallow')
                    # t.subsitute(d)

# t.safe_substitute(d)

# import time, os.path
# photofiles = ['kernel-linux.png']
# class BatchRename(Template):
#     delimeter = '%'
# fmt = input('Enter rename style (%d-date %n-segnum %f-format): ')
# t = BatchRename(fmt)
# date = time.strftime('%d%b%y')
# for i, filename in enumerate(photofiles) :
#     base, ext = os.path.splitext(filename)
#     newname = t.substitute(d=date, n=i, f=ext)
#     print('{0} --> {1}'. format(filename, newname))

# import struct
# with open('abricotine-1.0.0.zip') as f:
#     data = f.read()

# start = 0
# for i in range(2):
#     start += 14             # show the first 2 file headers
#     fields = struct.unpack('<IIIHH', data[start:start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

# start += 16             
# filename = data[start:start+filenamesize]
# start += filenamesize
# extra = data[start:start+extra_size]
# print(filename, hex(crc32), comp_size, uncomp_size)  # skip to the next header

# import threading, zipfile
# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile
# def run(self):
#     f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
#     f.write(self.infile)
#     f.close()
#     print("Finished background zip file: ", self.infile)


# background =AsyncZip('mydata', 'myarchive.zip')
# background.start()
# print('The main program continues to run in foreground.')

# background.join()       # Wait for the background task to finish
# print('Main program waited until background was done.')

## MASUK // IN

# import logging
# logging.debug('Debugging information')
# logging.info('Informational messange')
# logging.warning('Warning:config file %s not found', 'server.conf')
# logging.error('Error occured')
# logging.critical('Critical error -- shutting down')

## REFERENSI

from platform import node
import weakref
import gc
# class A:
#     def __init__(self,value):
#         self.value = value
#     def __repr__(self):
#         return str(self.value)

# a = A(10)                                           # create a reference
# d = weakref.WeakValueDictionary()
# d['primary'] = a                                    # doesn't create a reference 
# d['primary']                                        # fetch the object if it is still alive
# print(d['primary'])
# del a                                               # remove the one reference
# gc.collect()                                        # run garbage collection right way
# print(gc.collect())
# d[(d['primary'])

## ALAT UNTUK BEKERJA DENGAN

# from array import array
# a = array('H', [4000,10,700,22222])
# sum(a)
# print(sum(a))
# a[1:2]
# print(a[1:2])

from collections import deque
# d = deque(['task1', 'task2', 'task3'])
# d.append('task4')
# print('Handling', d.popleft())

# unsearched = deque([starting_node])
# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             return m
#         unsearched.append(m)

import bisect
scores =[(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)
    
from heapq import heapify, heappop, heappush
data = [1,3,5,7,9,2,4,6,8,0]
heapify(data)                               # rearrange the list into heap order
heappush(data, -5)                          # add a new entry
# [heappop(data) for i in range(3)]           # fetch the three smallest entries
print([heappop(data)for i in range(3)])

## ARITMATIKA TITIK MENGAMBANG
from decimal import *
a = round(Decimal('0.70') * Decimal('1.05'), 2)
print('Decimal', (a))
b = round(.70*1.05, 2)
print('Decimal', b)
c = Decimal('1.00') % Decimal ('.10')
print('Decimal', c)
d = 1.00 % 0.10
print('Decimal', d)
e = sum([Decimal('0.1')]*10) == Decimal('1.0')
print('Boolean', e)
f = sum([0.1]*100) == 1.01
print('Boolean', f)

getcontext().prec = 36
g = Decimal(1) / Decimal(7)
print('Decimal : ', g)