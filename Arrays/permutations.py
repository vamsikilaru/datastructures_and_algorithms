
# Input : [1, 2, 3]
# Output : [[3, 1, 2], [1, 3, 2], [1, 2, 3], [3, 2, 1], [2, 3, 1], [2, 1, 3]]

from collections import deque
def permutations(arr):
    results =[]
    ln = len(arr)
    permutations = deque()
    permutations.append([])
    for i in arr:
        for _ in range(len(permutations)):
            item = permutations.pop()
            for j in range(len(item)+1):
                newitem = list(item)
                newitem.insert(j,i)
                if len(newitem)==ln:
                    results.append(newitem)
                else:
                    permutations.append(newitem)
    return results

if __name__=="__main__":
    print(permutations([1,2,3]))