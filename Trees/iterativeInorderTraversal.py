from binaryTreeNode import BinaryTreeNode
import BTFunctions as bt

def inorder_traversal(root:BinaryTreeNode):
    stack = []
    res = []
    def populate_stack(root:BinaryTreeNode):
        while root:
            stack.append(root)
            root = root.left
    populate_stack(root)
    while stack:
        node = stack[-1]
        del stack[-1]
        if node.right:
            populate_stack(node.right)
        res.append(node.data)
    return res

arr = [25,125,200,300,75,50,12,35,60,75]
root = bt.create_BST(arr)
print(inorder_traversal(root))