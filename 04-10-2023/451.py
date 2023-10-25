class Solution:
    def sort(self,nums: list)-> list:
        i=0
        while(i<len(nums)):
            swapped=0
            j=0
            while(j<len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    
                    nums[j+1],nums[j]=nums[j],nums[j+1]
                    swapped=1
                j+=1
            if swapped==0:
                break
            i+=1
        return(nums)

    def frequencySort(self, s: str) -> str:
        dic=dict()
        res=[]
        new=""
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            res.append(dic[i])
        res=Solution.sort(self,res)
        for i in res:
            for j in dic:
                if dic[j]==i:
                    if j not in new:
                        new+=j*i      
        return new[::-1]
