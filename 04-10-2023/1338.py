class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d=dict(Counter(arr))
        d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        n=len(arr)//2
        res=0
        for x,y in d.items():
            if(n>0):
                n-=y
                res+=1
            else:
                break
        return res