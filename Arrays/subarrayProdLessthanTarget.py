

def find_subarrays(arr, target):
  result = []
  for i in range(len(arr)):
    if arr[i] < target:
      result.append([arr[i]])
      temp = list([arr[i]])
      p = arr[i]
      start,end = i+1,len(arr)
      while start < end:
        p = p*arr[start]
        if p < target:
          temp.append(arr[start])
          result.append(temp)
          start +=1
        else:
          break
  return result

if __name__=='__main__':
    print(find_subarrays([8, 2, 6, 5], 50))
    print(find_subarrays([2, 5, 3, 10], 30))