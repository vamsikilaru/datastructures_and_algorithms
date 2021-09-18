
def can_attend_all(intervals):
    intervals.sort(key = lambda x: x[0])
    for i in range(len(intervals)-1):
        if intervals[i][1]<intervals[i+1][0]:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    print(can_attend_all([[6,7], [2,4], [8,12]]))
    print(can_attend_all([[4,5], [2,3], [3,6]]))