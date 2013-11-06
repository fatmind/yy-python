'''
Created on 2013-1-2
@author: bohan.sj
'''

class Stack():
    '''
    stack simple implement
    '''
    max = 0
    index = -1; 
    data = []

    def __init__(self, max_size):
        self.max = max_size;
        
    def add(self, obj):
        if self.index == self.max:
            msg = "max size is", self.max
            raise IndexOverBoundException(msg)
        self.data.append(obj)
        self.index += 1
    
    def pull(self):
        res = self.data[self.index]
        self.data.__delitem__(self.index)
        self.index -= 1
        return res
    

    def display(self):
        for obj in self.data:
            print obj
    
class IndexOverBoundException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)



'''
--------- main ---------
'''

stack = Stack(3)
stack.add("hello")
stack.add("world")
stack.add("xiaopang")
# stack.add("pang")
stack.display()

stack.pull()
stack.display()
                
        