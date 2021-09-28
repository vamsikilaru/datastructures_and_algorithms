from binaryTreeNode import BinaryTreeNode
import random
from collections import deque

def insert(root : BinaryTreeNode,d: int) -> BinaryTreeNode:
        node = BinaryTreeNode(d)
        if root is None:
            return node
        parent = tmp = root
        while tmp:
            parent = tmp
            if d < tmp.data:
                tmp = tmp.left
            else:
                tmp = tmp.right
        if d < parent.data:
            parent.left = node
        else:
            parent.right = node
        return root

def find_in_bst(root:BinaryTreeNode,d) -> BinaryTreeNode:
        tmp = root
        while tmp:
            if d == tmp.data:
                return tmp
            elif d < tmp.data:
                tmp = tmp.left
            else:
                tmp = tmp.right
        return None
    
    #find node inorder (BST and BinaryTree)
def find_node(root:BinaryTreeNode,d) -> BinaryTreeNode:
        if not root:
            return None
        if root.data == d:
            return root
        tmp = find_node(root.left,d)
        if tmp:
            return tmp
        return find_node(root.right,d)
    
    # print inorder
def display_inorder(node:BinaryTreeNode):
        if node == None:
            return
        display_inorder(node.left)
        print(str(node.data), end=", ")
        display_inorder(node.right)
    
    # create BST
def create_BST(arr) -> BinaryTreeNode:
        root = None
        for x in arr:
            root = insert(root,x)
        return root
    
def create_binary_tree(count):
        root = None
        for i in range(1, count):
            root = insert(root, random.randrange(1,100))
        return root

def create_random_BST(count):
        root = None
        for i in range(1, count):
            root = insert(root, random.randrange(200, 300))
        return root
        
def bst_to_list_rec(root, lst):
        if root == None:
            return

        bst_to_list_rec(root.left, lst)
        lst.append(root.data)
        bst_to_list_rec(root.right, lst)

def bst_to_list(root):
        lst = []
        bst_to_list_rec(root, lst)
        return lst

def display_level_order(root):
  if root == None:
    return
  q = deque()
  q.append(root)

  while q:
    temp = q.popleft()
    print(str(temp.data), end = ",")
    if temp.left != None:
      q.append(temp.left)
    if temp.right != None:
      q.append(temp.right)

def populate_parents_rec(root:BinaryTreeNode,parent):
    if root == None:
        return
    root.parent = parent
    populate_parents_rec(root.left,root)
    populate_parents_rec(root.right,root)

def populate_parents(root:BinaryTreeNode):
    populate_parents_rec(root,None)