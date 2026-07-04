# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        prev , curr = None , slow
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        lag , lead = head , prev
        while lead != None:
            if lag.val != lead.val:
                return False
            lag = lag.next
            lead = lead.next  

        return True