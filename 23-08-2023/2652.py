class Solution:
    def sumOfMultiples(self, n: int) -> int:
        x=0
        for i in range(1,n+1):
            if i%3==0:
                x+=i
            elif i%5==0:
                x+=i
            elif i%7==0:
                x+=i
        return x