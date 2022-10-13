class Solution:
    def rotateRight(self,lst,k):
        k = k % len(lst)
        rotatedList = []
        if k == len(lst):
            return lst
        for i in range(len(lst)-k,len(lst)):
            rotatedList.append(lst[i])
        for i in range(len(lst)-k):
            rotatedList.append(lst[i])
        return rotatedList


if __name__=='__main__':
    ob = Solution()
    ls = [3,6,1,2,9,7]
    print(ob.rotateRight(ls,3))