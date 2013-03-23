'''
Created on 2013-2-25

@author: bohan.sj
'''
import os


def add_self(size):
    print size.__add__(10)


size = int(10) 
add_self(size)
print size


print os.sys.path


dig_array = [1, 2, 3]
print dig_array

def array_add(array, value):
    array.append(value)

array_add(dig_array, 0)
print dig_array


