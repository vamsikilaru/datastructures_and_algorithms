
class Solution:
    def productAll(self,lst):
        #cacluate left product of the element
        return [ele for ele in lst if ele%2==0]

if __name__=="__main__":
    ob = Solution()
    print(ob.productAll([1,2,3,4]))
