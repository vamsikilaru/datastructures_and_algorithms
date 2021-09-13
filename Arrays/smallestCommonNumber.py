
def find_smallest_common_number(a,b,c):
    i = j = k = 0
    while i <len(a) and j < len(b) and k < len(c):

        if a[i]== b[j] and b[j] == c[k]:
            return a[i]
        if a[i]<= b[j] and a[i] <= c[k]:
            i +=1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j +=1
        elif c[k] <= a[i] and c[k] <= b[j]:
            k +=1
    return -1

if __name__ == '__main__':
    v1 = [6, 7, 10, 25, 30, 63, 64]
    v2 = [0, 4, 5, 6, 7, 8, 50]
    v3 = [1, 6, 10, 14]
    print(find_smallest_common_number(v1,v2,v3))