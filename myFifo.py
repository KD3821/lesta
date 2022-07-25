'''
Python 2.7
https://documentation.help/Python-2.7/datastructures.html#tuples-and-sequences
It is possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”)
'''    
class Fifo1(object):
    buffer = []
    
    def put_in(self, x):
        self.buffer.append(x)
        return self.buffer
        
    def take_out(self):
        if len(self.buffer) > 0:
            self.buffer.pop(0)
        return self.buffer
        
    def check(self):
        return self.buffer


'''
however, lists are not efficient for this purpose.
While appends and pops from the end of list are fast, doing inserts or pops
from the beginning of a list is slow (because all of the other elements
have to be shifted by one)
To implement a queue, use collections.deque which was designed to have
fast appends and pops from both ends.
'''
from collections import deque
class Fifo2(object):
    buffer = deque()
    
    def put_in(self, x):
        self.buffer.append(x)
        return self.buffer
        
    def take_out(self):
        if len(self.buffer) > 0:
            self.buffer.popleft()
            return self.buffer
    
    def check(self):
        return self.buffer
