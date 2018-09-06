class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        samp_list = []
        curr = self.head
        while curr:
            samp_list.append(str(curr.data))
            curr = curr.next
        return '[' + ','.join(samp_list)+']'


    def prepend(self,data):
        curr = self.head
        self.head = Node(data,curr)



def merge_list(l1,l2):
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data <= l2.data:
        temp = l1
        temp.next = merge_list(l1.next,l2)
    else:
        temp = l2
        temp.next = merge_list(l1,l2.next)
    return temp


def merge_sort(head):
    if head is None or head.next is None:
        return head
    l1,l2 = divide_list(head)
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    head = merge_list(l1,l2)
    return head





def divide_list(head):
    slow = head
    fast = head
    if fast:
        fast = fast.next
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head,mid






lst = Linkedlist()
lst.prepend(1)
lst.prepend(2)
lst.prepend(3)

print(lst)
lst.head = merge_sort(lst.head)
print(lst)





