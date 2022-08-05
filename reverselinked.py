class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        current = self.head
        if current is None:
            print("linked list is empty")
        while current is not None:
            print(current.data)
            current = current.next

    # def reverse(self):
    #
    #     if self.head is None:
    #         print("linked list is empty")
    #     current = self.head
    #     last = None
    #
    #     while current is not None:
    #         after = current.next
    #         current.next = last
    #         last = current
    #         current = after
    #     self.head = last
    def reverse(self):

        if self.head is None:
            print("linked list is empty")
        current=self.head
        last=None
        while current is not None:
            after=current.next
            current.next=last
            last=current
            current=after
        self.head=last
ob1 = linkedlist()
ob1.head = node(10)
sec = node(20)
third = node(30)
fourth = node(40)
ob1.head.next = sec
sec.next = third
third.next = fourth
ob1.reverse()
ob1.printlist()
