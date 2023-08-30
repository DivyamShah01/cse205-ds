class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        y=[]
        x=1
        while x<=1000000:
            if x not in arr:
                y.append(x)
            if len(y)==k:
                return y[k-1]
                break
            x+=1
