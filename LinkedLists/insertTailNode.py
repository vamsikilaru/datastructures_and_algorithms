from typing import Tuple


class Node:
    def __init__(self,x):
        self.value= x
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head_node = None
    def get_head(self):
        return self.head_node
    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print(temp.value, "-> None")
        return True
    
class InsertTailNode:

    def insert_at_tail(self,lst,value):
        head = lst.get_head()
        first =head
        if head is None:
            lst.head_node = Node(value)
            return
        else:
            while head:
                node = head
                head = head.next
        node.next = Node(value)
        return

if __name__== '__main__':
    a =Node(1)
    lst = LinkedList()
    lst.head_node=a
    insert = InsertTailNode()
    insert.insert_at_tail(lst,10)
    lst.print_list()
    insert.insert_at_tail(lst,112)
    lst.print_list()
    insert.insert_at_tail(lst,90)
    lst.print_list()