############ DEFINING A NODE####################


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


#############DEFINING LINKLIST ####################


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ','.join(nodes) + ']'

    def prepend(self, data):
        self.head = Node(data, next=self.head)

    def repeated_elements(self, key):
        count = 0
        curr = self.head
        while curr:
            if curr.data == key:
                count += 1
            curr = curr.next
        return count

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def remove_all_ele(self, key):
        curr = self.head

        if curr == None:
            return

        while curr.data == key:
            self.head = curr.next
            curr = curr.next
            if curr == None:
                break

        while curr:
            while curr != None and curr.data != key:
                prev = curr
                curr = curr.next
            if curr == None:
                return
            prev.next = curr.next
            curr = prev.next

    def reverse_list(self):
        curr = self.head
        prev = None
        nex = curr.next

        while curr:
            curr.next = prev
            prev = curr
            curr = nex
            if nex:
                nex = nex.next
        self.head = prev




    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next


#
lst = LinkedList()

lst.append(1)
lst.prepend(3)
lst.prepend(2)
lst.prepend(4)
lst.prepend(7)

print(lst)

for items in lst:
    print(items)

