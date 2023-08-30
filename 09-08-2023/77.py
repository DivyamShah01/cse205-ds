class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def func(i,n,k,temp,ans):
            if(k==0):
                ans.append(temp.copy())
                return
            if i>n:
                return
            temp.append(i)
            func(i+1,n,k-1,temp,ans)

            
            temp.pop()
            func(i+1,n,k,temp,ans)