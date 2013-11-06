'''
Created on 2013-3-31
@author: bohan.sj
'''

class BubbleSort():
    '''
    implement  
    '''

    def sort(self, data): 
        size = len(data)
        on = 0
        for i in range(0, size):
            for j in range(i+1, size):
                base_value = data[i]
                compare_value = data[j]
                on = on + 1
                if base_value > compare_value:
                    temp_value = data[i]
                    data[i] = compare_value
                    data[j] = temp_value
        print "0(n) = ", on            

if __name__ == "__main__":
    bubble_sort = BubbleSort()
    data = [2, 4, 7, 1, 1, 9]
    bubble_sort.sort(data)
    print data    
    