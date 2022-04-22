# Python program to illustrate
# pickle.dump()
from errno import EL3RST
import pickle
import io

class SimpleObject(object):
    
    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return
    
data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last')) 

# Simulate a file with StringIO
# for o in data:
#     print('WRITING: %s (%s' % (o.name, o.name_backwards)) 
#     pickle.dumb(o, out_s)
#     out_s.flush()
    
# Python program to illustrate
# Pickle.dump()
import pickle

data = [ {'a':'A', 'b':2, 'c':3.0} ]
data_string = pickle.dump(data)
print('PICKLE: ', data_string)

# Python program to illustrate
# pickle.load()
import pickle
import io

class SimpleObject(object):
    def ___init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = '.join(l'
        return

data = []
dasta.append(SimpleObject('pickle'))
data.append(SimpleObject('cpickle'))
data.append(SimpleObject('last'))
# Simulate a file with String10
out_s = io.StringIO

# Write to the stream
for o in data :
    print('WRITING: %s (%s)' % (o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()
# set up a read-able stream
in_s = io.StringIO(out_s.getvalue())
# Read the data
while True:
    try:
        o = pickle.load(in_s)
    except E0FError:
        break
    else:
        print('READ: %s (%s)' % (o.name, o.name_backwards))
                  