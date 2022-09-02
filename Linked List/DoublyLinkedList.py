class Node:
    def __init__(self , data = None, prev = None , next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        if self.head != None:
            self.head.prev = Node(data ,None, self.head)
            self.head = self.head.prev
        else:
            node = Node(data , None ,self.head)
            self.head = node

    def print(self):    # this function is print from left to right to check the doubly linked list
        itr = self.head
        ll = ""
        while itr:
            itr = itr.next
            if itr.next == None:
                while itr:
                    ll += str(itr.data) +"->>"
                    itr = itr.prev
        print(ll)

    def insert_at_end(self, data):
        if self.head is None:
             self.head = Node(data)
             return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, itr, None)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return print(count)

    def insert_values(self , data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    def remove(self , index):
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            if count == index+1:
                itr.prev = itr.prev.prev
                break
            itr = itr.next
            count += 1

    def insert_at(self , index , data):
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = Node(data , None ,itr.next)
            if count == index+1:
                itr.prev = Node(data , itr.prev , None)
            count += 1
            itr = itr.next



vars = DoublyLinkedList()
vars.insert_at_end(23)
vars.insert_at_end(33)
vars.insert_at_end(43)
vars.insert_at_end(53)
vars.insert_at(2 ,5)
vars.print()