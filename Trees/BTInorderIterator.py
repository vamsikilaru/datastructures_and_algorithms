
from binaryTreeNode import BinaryTreeNode
import BTFunctions as bt

class InorderIterator:
    def __init__(self,root: BinaryTreeNode) -> None:
        self.stk =[]
        self.populate_iterator(root)
    
    def populate_iterator(self,root:BinaryTreeNode):
        while root:
            self.stk.append(root)
            root = root.left

    def hasNext(self):
        if self.stk:
            return True
        else:
            return False
    
    def getNext(self):
        if not self.hasNext:
            return None
        node = self.stk[-1]
        del self.stk[-1]
        if node.right:
            self.populate_iterator(node.right)
        return node

def inorder_interator(root: BinaryTreeNode):
        iter = InorderIterator(root)
        result = ''
        while iter.hasNext():
            node = iter.getNext()
            result += str(node.data) + " "
        return result

arr = [25,125,200,300,75,50,12,35,60,75]
root = bt.create_BST(arr)
print(inorder_interator(root))