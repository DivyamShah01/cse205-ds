lass Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def func(nums,y,z):
            if len(nums)==0:
                z.append(y)
                return
            out1=y[:]
            out2=y[:]
            out2.append(nums[0])
            func(nums[1:],out1,z)
            func(nums[1:],out2,z)
            return
        z=[]
        y=[]
        func(nums,y,z)
        return z