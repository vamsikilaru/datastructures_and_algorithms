#input1 : 9 -> 9 -> 0 -> 1 -> None
#input2 : 2 -> 3 -> 7 -> None
#output : 1 -> 3 -> 8 -> 1 -> None

from node import Node
from linkedList import LinkedList

class Solution:
    def addIntegers(integer1: Node, integer2: Node) -> Node:
        if not integer1:
            return integer2
        if not integer2:
            return integer1
        carry = 0
        head = None
        while integer1 or integer2:
            v1 = integer1.value if integer1 else 0
            v2 = integer2.value if integer2 else 0
            summ = v1+v2 + carry
            res = Node(summ % 10)
            carry = summ // 10
            if not head:
                head = res
                node = res
            else:
                node.next = res
                node = node.next
            if integer1:
                integer1 = integer1.next
            if integer2:
                integer2 = integer2.next
        if carry:
            node.next = Node(carry)
        return head

if __name__ == '__main__':
    l1 = LinkedList()
    integer1 = l1.createLinkedList([9,9,0,1])
    l1.print_list()
    l2 = LinkedList()
    integer2 = l2.createLinkedList([2,3,7])
    l2.print_list()
    res = LinkedList()
    res.head_node = Solution.addIntegers(integer1,integer2)
    res.print_list()    