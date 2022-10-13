class Solution:

    def mergeLists(self,lst1,lst2):
        i,j = 0,0
        while i < len(lst1) and j < len(lst2):
            #print(i,j,lst1[i],lst2[j])
            if lst1[i]>lst2[j]:
                lst1.insert(i,lst2[j])
                j = j+1
            i = i+1
        
            
        if j < len(lst2):
            lst1.extend(lst2[j::])

        return lst1

if __name__=='__main__':
    ob = Solution()
    print(ob.mergeLists([1,2,6,7],[3,4,8,9]))