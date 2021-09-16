
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# ouput max subarray = [4, -1, 2, 1] = 6
# Kandane Alogithm

def max_subarray(arr):
    local_max = float("-inf")
    global_max = float("-inf")
    for i in range(len(arr)):
        local_max = max(arr[i],local_max+arr[i])
        if local_max > global_max:
            global_max = local_max
    return global_max

if __name__ == '__main__':
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))