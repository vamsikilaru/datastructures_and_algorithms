
class Solution:

    def binary_search(self,arr,key,start,end):
        if start >end:
            return -1
        mid = (start + end)//2
        if arr[mid]==key:
            return mid
        if arr[start] <= arr[mid] and key <=arr[mid] and key >= arr[start]:
            return self.binary_search(arr,key,start,mid-1)
        elif arr[mid] <= arr[end] and key <=arr[end] and key >= arr[mid]:
            return self.binary_search(arr,key,mid+1,end)
        elif arr[end]<= arr[mid]:
            return self.binary_search(arr,key,mid+1,end)
        elif arr[start] >= arr[mid]:
            return self.binary_search(arr,key,start,mid-1)
        return -1

    def find_rotated_array_search(self,arr,key):
        return self.binary_search(arr,key,0,len(arr)-1)

if __name__=='__main__':
    s = Solution()
    print(s.find_rotated_array_search([4, 5, 6, 1, 2, 3],5))