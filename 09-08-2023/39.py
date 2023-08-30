class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def func(i,can,tar,temp,ans):
            if tar==0:
                ans.append(temp.copy())
                return
            if i>=len(can) or tar<0:
                return
            temp.append(can[i])
            func(i,can,tar-can[i],temp,ans)

            temp.pop()

            func(i+1,can,tar,temp,ans)

        i=0
        can=candidates
        tar=target
        temp=[]
        ans=[]
        func(i,can,tar,temp,ans)
        return ans