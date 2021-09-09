# input 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None
# for k = 5 rotate 5 nodes
# output 4 -> 5 -> 6 -> 7 -> 8 -> 1 -> 2 -> 3 -> None 

from node import Node
from linkedList import LinkedList

class Solution:

    def rotateList(self,head: Node,k:int) -> Node:
        if k == 0 or not head:
            return head
        start = head
        ln = 0
        while start:
            ln +=1
            last = start
            start = start.next
        if k >0:
            k = k % ln
        if k < 0:
            k = k + ln
        n = 1
        start = head
        while start and n< ln-k:
            start = start.next
            n +=1
        newhead = start.next
        start.next = None
        last.next = head
        return newhead

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    lst = LinkedList()
    lst.head_node = head
    lst.print_list()
    s = Solution()
    lst.head_node = s.rotateList(head,5)
    lst.print_list()