class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0

        while temp:
            temp=temp.next
            count+=1
        
        temp=head
        c=count-n-1
        count=0
        if c==-1:
            return temp.next

        while temp:
            if count==c:
                temp.next=temp.next.next
                break
            temp=temp.next
            count+=1
        return head