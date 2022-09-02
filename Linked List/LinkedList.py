class Node:
    def __init__(self , data = None , next = None ):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_begin(self , data):
            node = Node(data , self.head)
            self.head = node

    def print(self):
        if self.head == None:
            print("there is no linked list")
        else :
            itr = self.head
            ll = ""
            while itr:
                ll += str(itr.data) +">>-"
                itr = itr.next
            print(ll)

    def insert_at_end(self , data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data , None)

    def get_length(self):
        if self.head == None:
            print("there is no linked list")
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def insert_value(self , data_list):
        for i in data_list:
            self.insert_at_end(i)

    def remove_at(self , index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count+=1
            itr = itr.next

    def insert_at(self , index , data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_begin(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data , itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1




var = LinkedList()
var.insert_value(["banana" , "mango" , "Apple"])
var.insert_at(0 , "omar")
var.print()



























