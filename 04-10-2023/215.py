class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def merge(nums):
            if len(nums)<=1:
                return nums
            
            y=len(nums)//2
            left,right=nums[:y],nums[y:]
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
        y2=merge(nums)

        return y2[-k]