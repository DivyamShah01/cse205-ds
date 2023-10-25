class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(1,len(nums)):
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    continue
                else:
                    x=nums[j]
                    nums[j]=nums[i]
                    nums[i]=x