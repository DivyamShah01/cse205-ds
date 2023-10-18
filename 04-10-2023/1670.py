class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        sum=0
        temp=0

        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                sum+=accounts[i][j]
                if sum>temp:
                    temp=sum
            sum=0
        return temp