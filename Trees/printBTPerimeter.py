from binaryTreeNode import BinaryTreeNode
import BTFunctions as bt

# left perimeter
def print_left_perimeter(root:BinaryTreeNode,result):
    if root:
        if root.left:
            result.append(str(root.data))
            print_left_perimeter(root.left,result)
        elif root.right:
            result.append(str(root.data))
            print_left_perimeter(root.right,result)

# right perimeter
def print_right_perimeter(root:BinaryTreeNode,result):
    if root:
        if root.right:
            result.append(str(root.data))
            print_left_perimeter(root.right,result)
        elif root.left:
            result.append(str(root.data))
            print_left_perimeter(root.left,result)

# leaf nodes
def print_leaf_nodes(root:BinaryTreeNode,result):
    if root:
        print_leaf_nodes(root.left,result)
        if root.left is None and root.right is None:
            result.append(str(root.data))
        print_leaf_nodes(root.right,result)

def display_tree_perimeter(root:BinaryTreeNode):
    result =[]
    if root:
        result.append(str(root.data))
        print_left_perimeter(root.left,result)
        print_leaf_nodes(root.left,result)
        print_leaf_nodes(root.right,result)
        print_right_perimeter(root.right,result)
    return ' '.join(result)

arr = [100,50,200,25,60,350,10,70,400]
root = bt.create_BST(arr)
print("\nPrint tree perimeter\n")
print(display_tree_perimeter(root)) 