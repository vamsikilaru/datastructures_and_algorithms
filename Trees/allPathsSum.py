class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
  allPaths = []
  find_paths_rec(root,sum,[],allPaths)
  return allPaths

def find_paths_rec(node,required_sum,current_path,allPaths):
  if not node:
    return
  current_path.append(node.val)
  if required_sum == node.val and  not node.left and not node.right :
    allPaths.append(list(current_path))
  else:
    find_paths_rec(node.left,required_sum-node.val,current_path,allPaths)
    find_paths_rec(node.right,required_sum-node.val,current_path,allPaths)
  del current_path[-1]



def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()
