class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        def merge(nums):
            if len(nums)<=1:
                return nums
            
            x=len(nums)//2

            left,right=nums[:x],nums[x:]
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
        y=merge(nums)

        min=y[0]
        max=y[-1]

        for i in range(1,len(y)):
            if y[i]!=min and y[i]!=max:
                return y[i]
                
        return -1