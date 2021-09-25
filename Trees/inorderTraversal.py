from binaryTreeNode import BinaryTreeNode
import BTFunctions as bt

def inorder_traversal(res,root:BinaryTreeNode):
    if not root:
        return
    inorder_traversal(res,root.left)
    res.append(root.data)
    inorder_traversal(res,root.right)
    return res

arr = [25,125,200,300,75,50,12,35,60,75]
root = bt.create_BST(arr)
res = []
print(inorder_traversal(res,root))