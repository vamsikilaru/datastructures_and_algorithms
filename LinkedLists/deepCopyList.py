
from linkedList import LinkedList
class Node:
    def __init__(self,x):
        self.value= x
        self.next = None
        self.arbitrary_pointer = None

class Solution:
    def deepCopy(self,head: Node) -> Node:
        start = head
        hashmap = dict()
        while start:
            val = start.value
            hashmap[val]= Node(val)
            start = start.next
        start = head
        while start:
            val = start.value
            if start.next:
                nextval = start.next.value
                hashmap.get(val).next = hashmap.get(nextval)
            if start.arbitrary_pointer:
                arbitrary_pointer = start.arbitrary_pointer.value
                hashmap.get(val).arbitrary_pointer = hashmap.get(arbitrary_pointer)
            start = start.next
        return hashmap.get(head.value)

    
if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    lst = LinkedList()
    lst.head_node = head
    lst.print_list()
    s = Solution()
    head_node = s.deepCopy(head)
    lst.print_list()