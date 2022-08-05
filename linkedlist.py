


'''for traversing the linkedlist'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        n=self.head
        if n is None:
            print("linkedlist is empty")
        while n is not None:
            print(n.data)
            n=n.next
ob1=linkedlist()
#creating the node
ob1.head=node(1)
sec=node(2)
third=node(3)
#linking the first node to second node
ob1.head.next=sec
sec.next=third
# ob1.printlist()

'''inserting the data at the begining'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        n=self.head
        if n is None:
            print("linked list empty")
        while n is not None:
            print(n.data)
            n=n.next
    def add_begin(self,data):
        #create new node
        newnode=node(data)
        #now head is first pointing to newnode
        newnode.next=self.head
        self.head=newnode

ob1=linkedlist()
#creating the node
ob1.head=node(1)
sec=node(2)
third=node(3)
#linking the first node to second node
ob1.head.next=sec
sec.next=third
ob1.add_begin(5)
# ob1.printlist()

'''inserting the node at the end of linkedlist'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        n=self.head
        if n is None:
            print("linked list empty")
        while n is not None:
            print(n.data)
            n=n.next

    def add_end(self,data):
        #create the new node
       newnode=node(data)
       n=self.head
        #check  the n is empty or not if it is empty add new node and if not move to the next node
       if n is None:
           n=newnode
       else:
           while n.next is not None:
               n=n.next
           n.next=newnode
ob1=linkedlist()
ob1.head=node(1)
sec=node(3)
third=node(4)
ob1.head.next=sec
sec.next=third
ob1.add_end(14)
# ob1.printlist()

''''inserting the node between two nodes'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        n=self.head
        if n is None:
            print("linked list empty")
        while n is not None:
            print(n.data)
            n=n.next

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.next
        if n is None:
            print("item is not present in list")
        else:
            newnode=node(data)
            n.next=newnode


ob1=linkedlist()
ob1.head=node(1)
sec=node(2)
third=node(3)
ob1.head.next=sec
sec.next=third
ob1.add_after(5,1)
ob1.printlist()



