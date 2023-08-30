class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        y=[]
        for i in range(len(nums)):
            x=nums[nums[i]]
            y.append(x)
        return y