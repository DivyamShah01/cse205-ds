class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=head
        y=head
        while y!=None and y.next!=None:
            x=x.next
            y=y.next.next
        return x