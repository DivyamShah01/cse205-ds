class Solution:
    def backtrack(self,lst,k,ans,temp,idx):
        if len(temp) == k:
            ans.append(temp.copy())
            return
        for i in range(idx,len(lst)):
            temp.append(lst[i])
            self.backtrack(lst,k,ans,temp,i+1)
            temp.pop()
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        lst = [i for i in range(1,n+1)]
        self.backtrack(lst,k,ans,[],0)
        return ans