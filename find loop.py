class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        n=self.head
        while n is not None:
            print(n.data)
            n=n.next
    def loop(self):
        fast=self.head
        slow=self.head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return 1
        return 0

ob1 = linkedlist()
# creating the node
ob1.head = node(1)
sec = node(2)
third = node(3)
fourth=node(4)
# linking the first node to second node
ob1.head.next = sec
sec.next = third
ob1.head.next.next.next.next=ob1.head
if (ob1.loop()):
    print("found loop")
else:
    print("not found")


