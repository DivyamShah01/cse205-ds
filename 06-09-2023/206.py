class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        cur=head
        while cur:
            n=cur.next
            #print(n)
            cur.next=prev
            #print(cur.next)
            prev=cur
            #print(prev)
            cur=n
            #print(cur)
        
        return prev