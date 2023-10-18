class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        x=[]

        for i in range(len(nums)):
            x.append(nums[i])
        x.sort()

        print(x)
        sum=0

        for i in range(0,len(nums),2):
            sum+=min(x[i],x[i+1])
            #print(nums[i])
            #print(nums[i+1])
        
        return sum