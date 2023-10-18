class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        def merge(prices):

            if len(prices)<=1:
                return prices
            
            mid=len(prices)//2
            left,right=prices[:mid],prices[mid:]
            left,right=merge(left),merge(right)

            result,i,j=[],0,0

            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
                
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        x=merge(prices)     
        
        cost=x[0]+x[1]
        return money if cost>money else (money-cost)
            