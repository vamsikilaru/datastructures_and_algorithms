class Solution:
    def mergeSort(self,lst):
        if len(lst) > 1:
            mid = len(lst)//2
            left = lst[:mid]
            right = lst[mid:]
            self.mergeSort(left)
            self.mergeSort(right)
            i,j,k=0,0,0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    lst[k]=left[i]
                    i = i+1
                else:
                    lst[k]=right[j]
                    j = j+1
                k = k+1
            
            while i < len(left):
                lst[k]=left[i]
                i =i+1
                k=k+1
            while j < len(right):
                lst[k] = right[j]
                j = j+1
                k = k+1

if __name__=='__main__':
    ob = Solution()
    ls = [3,6,1,2,9,7]
    ob.mergeSort(ls)
    print(ls)