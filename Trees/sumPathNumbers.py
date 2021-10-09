class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  return find_paths_rec(root,0)

def find_paths_rec(node,total_sum):
  if not node:
    return 0
  total_sum = 10*total_sum + node.val
  print(total_sum)
  if not node.left and not node.right:
      return total_sum
  return find_paths_rec(node.left,total_sum) + find_paths_rec(node.right,total_sum)



def main():

  root = TreeNode(1)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(3)
  root.right.right = TreeNode(5)
  print("Total paths sum " + 
        ": " + str(find_sum_of_path_numbers(root)))


main()
