
class Solution:
    def productAll(self,lst):
        #cacluate left product of the element
        result = []
        left =1
        for ele in lst:
            result.append(left)
            left = left * ele
        print("left result:",result)
        right =1
        for i in range(len(lst)-1,-1,-1):
            result[i]=result[i]*right
            right = right*lst[i]
        return result

if __name__=="__main__":
    ob = Solution()
    print(ob.productAll([1,2,3,4]))
