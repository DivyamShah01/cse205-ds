class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode()
        ans=temp
        carry=0
        while l1!=None or l2!=None or carry:
            s=0
            if l1!=None:
                s+=l1.val
                #print(s)
                l1=l1.next
                #print(l1)
            if l2!=None:
                s+=l2.val
                #print(s)
                l2=l2.next
                #print(l2)
            
            s+=carry
            #print(s)
            carry=s//10
            x=s%10
            temp.next=ListNode(x)
            #print(temp.next.val)
            temp=temp.next
            #print(temp.val)

        return ans.next