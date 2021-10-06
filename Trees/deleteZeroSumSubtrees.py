from binaryTreeNode import BinaryTreeNode
import BTFunctions as bt

def delete_zero_sum_subtree(root:BinaryTreeNode):
  if not root:
    return
  if root.left:
    if root.left.left and root.left.right:
        print("at left",root.left.data,root.left.left.data,root.left.right.data)
        if root.left.data + root.left.left.data + root.left.right.data ==0:
            root.left = None
    delete_zero_sum_subtree(root.left)
  if root.right:
    if root.right.left and root.right.right:
        print("at right: ",root.right.data,root.right.left.data,root.right.right.data)
        if root.right.data + root.right.left.data + root.right.right.data ==0:
            root.right = None
    delete_zero_sum_subtree(root.right)
  return

root = BinaryTreeNode(7)
root.left = BinaryTreeNode(5)
root.right = BinaryTreeNode(6)
root.left.left = BinaryTreeNode(-3)
root.left.right = BinaryTreeNode(-2)
root.right.left = BinaryTreeNode(-5)
root.right.right = BinaryTreeNode(-1)


bt.display_level_order(root)
delete_zero_sum_subtree(root)
print("\nLevel Order Traversal:")
bt.display_level_order(root)