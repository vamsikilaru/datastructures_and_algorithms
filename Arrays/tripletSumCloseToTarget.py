# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target

def triplet_closest_targetsum(arr,target):
    arr.sort()
    smallest = float("inf")
    start = 0
    for i in range(len(arr)-2):
        end = len(arr)-1
        start = i+1
        while start<end:
            current_sum = arr[i]+arr[start]+arr[end]
            if target-current_sum ==0:
                return target
            if abs(target-current_sum)<abs(smallest) or (abs(target-current_sum)==abs(smallest) and target-current_sum>smallest):
                smallest = target-current_sum
            if target-current_sum > 0:
                start += 1
            else:
                end -=1        
    return target-smallest


if __name__ == '__main__':
    print(triplet_closest_targetsum([-3, -1, 1, 2], 1))
    print(triplet_closest_targetsum([-2, 0, 1, 2], 2))