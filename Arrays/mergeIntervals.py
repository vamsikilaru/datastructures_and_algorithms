 # intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

from typing import List


class Solution:

    def mergeIntervals(self,lst :List[List[int]]):
        lst.sort(key = lambda x: x[0])
        merged =[]
        for interval in lst:
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][1]=interval[1]
        print(merged)


if __name__=='__main__':
    s = Solution()
    intervals = [[1,3],[15,18],[2,6],[8,10]]
    s.mergeIntervals(intervals)