from binaryTreeNode import BinaryTreeNode
import BTFunctions as bt

def concat_lists(head1:BinaryTreeNode,head2:BinaryTreeNode):
    if not head1:
        return head2
    if not head2:
        return head1

    tail1 = head1.left
    tail2 = head2.left
    #left for previous and right for next
    tail1.right = head2
    head2.left = tail1

    head1.left = tail2
    tail2.right = head1

    return head1

def convert_to_linked_list_rec(node:BinaryTreeNode):
    if not node:
        return None
    list1 = convert_to_linked_list_rec(node.left)
    list2 = convert_to_linked_list_rec(node.right)
    node.left = node.right = node  # used to go tail from head, list connect head and tail which are removed at the final result
    result = concat_lists(list1,node)
    result = concat_lists(result,list2)
    return result

def convert_to_linked_list(root:BinaryTreeNode):
    head = convert_to_linked_list_rec(root)
    if head.left:
        head.left.right = None
        head.left = None
    return head

def get_list(head:BinaryTreeNode):   # used to print result based on linked list
    res = []
    if not head:
        return res
    while True:
        res.append(head.data)
        head = head.right
        if head is None:
            break
    return res

data = [100,50,200,25,75,350, 30, 60]
root = bt.create_BST(data)
head = convert_to_linked_list(root)
v = get_list(head)
print(v)