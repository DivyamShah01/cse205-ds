class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        self.x=[]

        for i in nums:
            y=i
            
            for j in range(len(nums)):
                if i<nums[j]:
                    #print(i)
                    y=nums[j]
                    #print(y)
                    self.x.append(y)
                    break
            
            #print(y)
            #print("-",i)
            #print("#",j)
            
            if i == y :
                y=-1
                
                self.x.append(y)
        return self.x