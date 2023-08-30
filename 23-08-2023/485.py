class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        result=0

        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                if (result<=count):
                    result = count
                count=0
        if(count>=result):
            return count
        else:
            return result