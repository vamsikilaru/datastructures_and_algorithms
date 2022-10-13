class Solution:
    def second_max(self,lst):
        first=second=float("-inf")
        for i in lst:
            if i > first:
                second =first
                first = i
            elif second < i and second < first:
                second = i
            else:
                continue
            #print(first,second,i)
        return second if second != float("-inf") else None


if __name__=='__main__':
    ob = Solution()
    ls = [3,6,1,2,9,7]
    print(ob.second_max(ls))
