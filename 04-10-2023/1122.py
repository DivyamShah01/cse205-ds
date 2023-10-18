class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x=[]
        for i in range(len(arr1)):
            x.append(arr1[i])
        x.sort()
        res=[]
        
        for i in range(len(arr2)):

            for j in range(len(x)):

                if arr2[i]==x[j]:
                    res.append(x[j])
                
        for i  in range(len(x)):
            if x[i] not in arr2:
                res.append(x[i])
        return res