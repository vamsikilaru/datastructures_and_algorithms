from binaryTreeNode import BinaryTreeNode
import random

class BTFunctions:
    def insert(self,root : BinaryTreeNode,d: int) -> BinaryTreeNode:
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

    def find_in_bst(self,root:BinaryTreeNode,d) -> BinaryTreeNode:
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
    def find_node(self,root:BinaryTreeNode,d) -> BinaryTreeNode:
        if not root:
            return None
        if root.data == d:
            return root
        tmp = self.find_node(root.left,d)
        if tmp:
            return tmp
        return self.find_node(root.right,d)
    
    # print inorder
    def display_inorder(self,node:BinaryTreeNode):
        if node == None:
            return
        self.display_inorder(node.left)
        print(str(node.data), end=", ")
        self.display_inorder(node.right)
    
    # create BST
    def create_bst(self,arr) -> BinaryTreeNode:
        root = None
        for x in arr:
            root = self.insert(root,x)
        return root
    
    def create_binary_tree(self,count):
        root = None
        for i in range(1, count):
            root = self.insert(root, random.randrange(1,100))
        return root

    def create_random_BST(self,count):
        root = None
        for i in range(1, count):
            root = self.insert(root, random.randrange(200, 300))
        return root
        
    def bst_to_list_rec(self,root, lst):
        if root == None:
            return

        self.bst_to_list_rec(root.left, lst)
        lst.append(root.data)
        self.bst_to_list_rec(root.right, lst)

    def bst_to_list(self,root):
        lst = []
        self.bst_to_list_rec(root, lst)
        return lst