'''
Created on 2013-2-25

@author: bohan.sj
'''


def add_self(size):
    print size.__add__(10)


size = int(10) 
add_self(size)
print size


#print os.sys.path


dig_array = [1, 2, 3]
print dig_array

def array_add(value):
    dig_array = [1]
    #dig_array.append(value)
    print dig_array
    

array_add(0)
print dig_array


