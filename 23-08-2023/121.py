class Solution:
    def maxProfit(self, prices: List[int]) -> int:
	a=0
        for i in range(len(prices)-1,0,-1):
            for j in range(i,0,-1):
                if prices[i]-prices[j-1]>=0:
                    x=prices[i]-prices[j-1]
                    if x>a:
                        a=x
    
                    
        return a