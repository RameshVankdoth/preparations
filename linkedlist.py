class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def insertstart(self, data):
        node = Node(data, self.head)
        self.head = node
        
        

    def print(self):
        if self.head is None:
            print("Linked list if empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)


if __name__ == "__main__":
    ll = linkedlist()
    ll.insertstart(5)
    ll.insertstart(410)

    ll.print()

# Update
