# Input [2, 1, 5, 2, 3, 2] target sum = 7
# output : 2  array: [5, 2]


def smallest_subarray_with_given_sum(s, arr):
    global_min = float("inf")
    window_sum = window_start = 0
    ln = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        ln +=1
        while window_sum >=s:
            global_min = min (global_min,ln)
            ln -=1
            window_sum -=arr[window_start]
            window_start +=1
        
    return global_min

if __name__ == "__main__":
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
