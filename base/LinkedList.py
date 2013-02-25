
class LinkedList:
    
    head = None
    tail = None
    count = 0
    
    def __init__(self):
        self.head = Entry()
        self.tail = Entry()
        self.head.next = self.tail
        self.tail.pre = self.head
    
    def add(self, data):
        e = Entry()    
        e.data = data
        self.tail.pre.next = e
        e.pre = self.tail.pre
        e.next = self.tail
        self.tail.pre = e
        self.count += 1

    def display(self):
        e = self.head.next
        while e and e.next:
            print e.data
            e = e.next

class Entry:
    pre = None
    next = None
    data = None


linked_list = LinkedList()
linked_list.add("hello")
linked_list.add("world")

linked_list.display()
 
