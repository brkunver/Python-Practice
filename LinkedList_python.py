#Burakhan Unver tarafindan yazildi | 14.12.2020

class node:
    def __init__(self,value):
        self.value = value
        self.next:node = None

class list:

    def __init__(self, head = None ):
        self.head:node = head

    #returns head node's value
    def get_head(self):
        return self.head.value

    #return the tail's value
    def get_tail(self):
        if self.head == None:
            return None

        temp = self.head
        while temp.next != None:
            temp = temp.next
        return temp.value

    #returns number of elements
    def count(self):
        if self.head == None:
            return 0
        else:
            count = 1
            temp = self.head
            while temp.next != None:
                temp = temp.next
                count += 1
            return count

    #prints whole list
    def print_list(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp!=None:
                print(temp.value)
                temp=temp.next

    #adds a value to the end of the list
    def add_last(self,value):
        if self.head == None:
            self.head = node(value)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node(value)

    #adds a value to the end of the list
    def add_first(self,value):
        if self.head == None:
            self.head = node(value)
        else:
            new_node = node(value)
            new_node.next = self.head
            self.head = new_node

    #removes the last node
    def remove_last(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None

    #removes the head node
    def remove_head(self):
        if self.head== None:
            print("List is empty")
        else:
            self.head = self.head.next

    #returns the element at given index
    def get_value_at_index(self, index:int ):
        if self.head == None:
            return None
        elif index > self.count() or index < 0:
            return None
        else:
            current = 0
            temp = self.head
            while current != index:
                temp = temp.next
                current += 1
            return temp.value

    #removes the element at given index
    def remove_at_index(self, index:int):
        if self.head == None:
            print("list is empty")

        elif index >= self.count():
            print("Index is bigger than the list's size")
        else:
            temp = self.head
            current = 0
            while current < index-1:
                temp = temp.next
                current += 1
            temp.next = temp.next.next

    #adds element at given index
    def add_at_index(self,index:int,value):
        if index >= self.count():
            print("Index is bigger than the list's size")

        else:
            current = 0
            temp = self.head
            while current < index-1:
                temp = temp.next
                current += 1
            new_node = node(value)
            new_node.next = temp.next
            temp.next = new_node



