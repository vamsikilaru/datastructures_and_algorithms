class Solution:

    def find_sum(self,lst,k):
        m ={}
        for i,v in enumerate(lst):
            m[v]=i
        for i,v in enumerate(lst):
            if k-v in m and m[k-v]!=i:
                return [v,k-v]

if __name__=='__main__':
    ob = Solution()
    print(ob.find_sum([1,2,3,4,5],5))