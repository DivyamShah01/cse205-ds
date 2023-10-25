# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        y1=ListNode()
        temp=y1
        x=[]
        while head:
            x.append(head.val)
            head=head.next

        def merge(x):
            if len(x)<=1:
                return x
            
            y=len(x)//2
            left,right=x[:y],x[y:]
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
        y2=merge(x)


        
        for i in range(len(y2)):
            temp.next=ListNode(y2[i])
            temp=temp.next
        return y1.next
        