class Solution:

# Given array and target value, return list of index where sum of elements of the index is equal to target
# [1,2,3,4,5] target =9
# 4+5 = 9 return [3,4] index

    def sum_target(self,lst, target):

        self.mp ={}

        for i,v in enumerate(lst):
            self.mp[v]=i
        for i,v in enumerate(lst):
            remainder = target-v
            if remainder in self.mp and self.mp[remainder]!=i:
                return [i,self.mp[remainder]]

        return None

if __name__ == '__main__':
    ob = Solution()
    print(ob.sum_target([1,2,3,4,5],9))