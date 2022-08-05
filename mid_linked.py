class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
    def add_begin(self,data):
        # import pdb;pdb.set_trace()
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode

    def mid(self):
        #create first and last pointing to head initially

        slow=self.head
        fast = self.head
        if self.head is not None:
            while (fast is not None and fast.next is not None):
                fast=fast.next.next
                slow=slow.next
            print("the middle node is:",slow.data)
        # #
        # slow_ptr = self.head
        # fast_ptr = self.head
        #
        # if self.head is not None:
        #     while (fast_ptr is not None and fast_ptr.next is not None):
        #         fast_ptr = fast_ptr.next.next
        #         slow_ptr = slow_ptr.next
        #     print("The middle element is: ", slow_ptr.data)





ob1 = linkedlist()
ob1.head = node(10)
sec = node(20)
third = node(30)
ob1.head.next = sec
sec.next = third
ob1.add_begin(69)
ob1.add_begin(70)
ob1.add_begin(80)
ob1.add_begin(90)
ob1.mid()
# ob1.printlist()