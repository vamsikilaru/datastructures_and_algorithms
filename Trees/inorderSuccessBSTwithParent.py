from binaryTreeNode import BinaryTreeNode
import BTFunctions as bt

def inorder_successor_with_parent_pointer(node:BinaryTreeNode):
    if not node:
        return None
    if node.right != None:
        return find_min_left(node)
    while node.parent != None:
        if node.parent.left == node:
            return node.parent
        node = node.parent
    return None

def find_min_left(node:BinaryTreeNode):
    if not node:
        return None
    while node.left != None:
        node = node.left
    return node

def find_successor(root:BinaryTreeNode,d):
    while root:
        if root.data > d:
            root = root.left
        elif root.data < d:
            root = root.right
        else:
            return inorder_successor_with_parent_pointer(root)
    return None

arr = [25,125,200,300,75,50,12,35,60]
root = bt.create_BST(arr)
bt.populate_parents(root)
print(find_successor(root,75).data)