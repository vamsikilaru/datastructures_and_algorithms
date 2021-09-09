from node import Node
from linkedList import LinkedList

# Input  1 > 2 > 3 > 4 > 5 > 6 > 7 > 8 
# k = 3
# Output 3 > 2 > 1 > 6 > 5 > 4 > 8 > 7

class Solution:

    def reverse_every_K_Elements(self,head : Node,k : int) -> Node:
        if k<=1 or not head:
            return head
        curr, prev = head, None
        while True:
            n = 0
            prev_sublist_last = prev
            curr_sublist_last = curr
            tmp = None
            while curr and n < k:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                n +=1
            #connect current sublist last node
            curr_sublist_last.next = curr
            
            if prev_sublist_last is not None:
                prev_sublist_last.next = prev
            else:
                head = prev
            if curr == None:
                break
            prev = curr_sublist_last
        return head

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
    node = s.reverse_every_K_Elements(head,3)
    lst.head_node= node
    lst.print_list()
