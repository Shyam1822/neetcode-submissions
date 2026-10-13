# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use slow and fast pointers to identify half next time
        # 13/10

        cur1 = head
        n=0

        while cur1:
            n+=1
            cur1=cur1.next
        
        mid = (n+1)//2

        cur2 = head
        for i in range(mid-1):
            cur2 = cur2.next
        
        sec_half = cur2.next
        cur2.next = None # seperating the lists

        # now reverse 2nd half
        prev,curr = None,sec_half

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        rev_sec_half = prev
        first_half = head

        while rev_sec_half:
            temp1 = first_half.next
            temp2 = rev_sec_half.next
            first_half.next = rev_sec_half
            rev_sec_half.next = temp1
            first_half = temp1
            rev_sec_half = temp2 
            



