from binaryTreeNode import BinaryTreeNode
import BTFunctions as bt

def mirrorTree(root: BinaryTreeNode):
    if not root:
        return
    if root.left:
        mirrorTree(root.left)
    if root.right:
        mirrorTree(root.right)
    tmp = root.left
    root.left = root.right
    root.right = tmp

arr = [20,50,200,75,25,300]
root = bt.create_BST(arr)


bt.display_level_order(root)
mirrorTree(root)
print("\nMirrored Level Order Traversal:")
bt.display_level_order(root)