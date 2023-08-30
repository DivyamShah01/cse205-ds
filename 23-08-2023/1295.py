class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        total=0
        for i in range(len(nums)):
            y=str(nums[i])
            
            if (len(y)%2==0):
                total+=1
        
        return total