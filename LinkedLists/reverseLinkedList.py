from node import Node
from linkedList import LinkedList

class Solution:

    def reverseList(self,lst):
        head = lst.get_head()
        if not head:
            return None
        
        def helper(node):
            if node is None or node.next is None:
                return node
            fornext = node.next
            current = helper(fornext)
            fornext.next = node
            node.next = None
            return current
        reverse_head = helper(head)
        lst.head_node = reverse_head
        return lst
    
if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_at_tail(2)
    lst.insert_at_head(5)
    lst.insert_at_tail(10)
    lst.print_list()
    s= Solution()
    s.reverseList(lst)
    lst.print_list()

