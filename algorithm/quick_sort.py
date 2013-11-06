'''
Created on 2013-3-23
@author: bohan.sj
'''
from test.test_iterlen import len

class QuickSort():
    '''
    implement quick sort by python
    '''
    
    def sort(self, data):
        
        if data == None or len(data) < 1:
            return data 
        
        print data
                
        base_value = data[0]
        left_array = []
        right_array = []
        
        for index in range(1, len(data)):
            compare_value = data[index]
            if(base_value > compare_value):
                left_array.append(compare_value)
            else:
                right_array.append(compare_value) 
        
        if len(left_array) > 1:
            sorted_array = self.sort(left_array)
            left_array = sorted_array
            
        
        if len(right_array) > 1:
            sorted_array = self.sort(right_array)
            right_array = sorted_array

        right_array.insert(0, base_value)
        left_array.extend(right_array)
        
        return left_array
        

        
if __name__ == "__main__":
    quick_sort = QuickSort()
    data = [3, 2, 5, 1, 4, 9]
    print quick_sort.sort(data)        
    

    