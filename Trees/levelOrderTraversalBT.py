from typing import Deque
from binaryTreeNode import BinaryTreeNode
import BTFunctions as bt
from collections import deque

def level_order_traversal(root:BinaryTreeNode):
    if not root:
        return None
    q = deque()
    q.append(root)
    result = ''
    while q:
        for i in range(len(q)):
            node = q.popleft()
            result += str(node.data) + " "
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result += "\n"
    return result

arr = [25,125,200,300,75,50,12,35,60]
root = bt.create_BST(arr)
print(level_order_traversal(root))
        