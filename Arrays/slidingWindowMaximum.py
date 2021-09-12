
from typing import  List
from collections import deque

class Solution:

    def find_max_sliding_window(self,arr: List[int],window_size: int):
        result = []
        window = deque()

        if not arr or window_size > len(arr):
            return None
        # compute the fist window
        for i in range(window_size):
            while window and arr[i] >= window[-1]: # pop if window left is < current element
                window.pop()
            window.append(i)
        result.append(arr[window[-1]])

        for i in range(window_size,len(arr)):
            while window and arr[i] >= window[-1]:
                window.pop()
            if window and window[0] <= i-window_size:
                window.popleft()
            window.append(i)
            result.append(arr[window[-1]])
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.find_max_sliding_window([1,2,3,4,5,6,7,8,9],3))