from binaryTreeNode import BinaryTreeNode
import BTFunctions as bt

def inorder_successor_bst(root:BinaryTreeNode,d: int):
    if not root:
        return
    successor = None
    while root:
        if root.data < d:
            root = root.right
        elif root.data >d:
            successor = root
            root = root.left
        else:
            if root.right != None:      # return left most of the right subtree which is the successor
                successor = find_min(root.right)
            break
    return successor
def find_min(node:BinaryTreeNode):
    if node == None:
        return None
    while node.left:
        node = node.left
    return node


arr = [25,125,200,300,75,50,12,35,60]
root = bt.create_BST(arr)
print(inorder_successor_bst(root,75).data)