# Input: [-3, 0, 1, 2, -1, 1, -2] find unique triplets 
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1] 

def triplet_zero_sum(arr):
    arr.sort()
    print(arr)
    ln = len(arr)
    results = []
    for i in range(ln-2):
        if arr[i]>0 or (arr[i]==arr[i+1]) :
            continue
        search_pair(arr,-arr[i],i+1,results)
    return results

def search_pair(arr,targetsum,start,results):
    end = len(arr)-1
    while start < end:
        current_sum = arr[start]+arr[end]
        if current_sum==targetsum:
            results.append([-targetsum,arr[start],arr[end]])
            start +=1
            while arr[start]==arr[start-1]: # skip if old start == new start
                start +=1
        elif current_sum > targetsum:
            end -=1
            while arr[end]==arr[end+1]:  # skip if old end == new end
                end -=1
        else:
            start +=1
            while arr[start]==arr[start-1]:  # skip if old start == new start
                start +=1

if __name__ =="__main__":
    print(triplet_zero_sum([-3, 0, 1, 2, -1, 1, -2]))