from typing import List
from node import Node
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

    def insert_at_head(self,value):
        node = Node(value)
        if self.head_node is None:
            self.head_node= node
            return self.head_node
        else:
            node.next = self.head_node
            self.head_node = node
            return self.head_node

    def insert_at_tail(self,value):
        head = self.head_node
        if not head:
            self.head_node = Node(value)
            return
        while head:
            node = head
            head = head.next
        node.next = Node(value)
        return

    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print(temp.value, "-> None")
    
    def createLinkedList(self,lst: List[int]) -> Node:
        if lst:
            for i in range(len(lst)):
                node = Node(lst[i])
                if not self.head_node:
                    self.head_node = node
                    start = node
                else:
                    start.next = node
                    start = start.next
        return self.head_node