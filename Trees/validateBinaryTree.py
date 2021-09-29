from binaryTreeNode import BinaryTreeNode
import BTFunctions as bt

def valiate_binary_tree(root):
    return validate_binary_tree_rec(root,float("-inf"),float("inf"))

def validate_binary_tree_rec(node:BinaryTreeNode,min_val_range,max_val_range):
    if not node:
        return True
    if node.data < min_val_range or node.data > max_val_range:
        return False
    return validate_binary_tree_rec(node.left,min_val_range,node.data) and validate_binary_tree_rec(node.right,node.data,max_val_range)

arr = [25,125,200,300,75,50,12,35,60]
root = bt.create_BST(arr)
print(valiate_binary_tree(root))