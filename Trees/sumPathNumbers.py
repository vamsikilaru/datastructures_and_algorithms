class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  total_sum = 0
  # TODO: Write your code here
  find_paths_rec(root,'',total_sum)
  return total_sum

def find_paths_rec(node,current_path,total_sum):
  if not node:
    return total_sum
  current_path += str(node.val)
  if not node.left and not node.right :
    total_sum = int(current_path)
  print("total:",total_sum,"curr:",current_path)
  find_paths_rec(node.left,current_path,total_sum)
  find_paths_rec(node.right,current_path,total_sum)
  current_path = current_path[:len(current_path)-2]
  return total_sum



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
