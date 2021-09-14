
def move_zeros_to_front(arr):
    if len(arr)<1:
        return
    read = write = len(arr)-1
    while read >=0:
        if arr[read] !=0:
            arr[write]=arr[read]
            read -=1
            write -=1
        else:
            read -=1
    while write >= 0:
        arr[write]=0
        write -=1

if __name__ == '__main__':
    arr = [10,11,0,-4,7,0,6,9,0,3]
    print("before:",arr)
    move_zeros_to_front(arr)
    print("after:",arr)