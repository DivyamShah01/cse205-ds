class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        self.x=[]

        for i in nums1:
            #print(i)
            if i in nums2:
                for j in range(len(nums2)):
                    if i == nums2[j]:
                        temp=i
                        #print(temp)
                        #print(j)
                        if temp!=nums2[-1]:
                            #print(temp)
                            for k in range(j+1,len(nums2)):
                                #print(k)
                                #print(nums2[k])
                                #for z in range(nums2[k],len(nums2)):

                                if temp<nums2[k]:
                                    temp=nums2[k]
                                    self.x.append(temp)
                                    print(self.x)
                                    print(temp)
                                    break
                                #else:
                                #    temp=-1
                                #    self.x.append(temp)
                                    
                            if temp==i:
                                temp=-1

                                self.x.append(temp)
                            
                                    
                                #else:
                                #    temp=-1
                        
                                #    self.x.append(temp)
                                #    break
                                    
                            #self.x.append(temp)
                        else:
                            temp=-1
                            self.x.append(temp)
        return self.x