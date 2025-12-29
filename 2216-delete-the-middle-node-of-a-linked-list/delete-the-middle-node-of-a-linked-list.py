# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0 
        mid = 0 
        current = head
        while current is not None: 
            current = current.next
            count = count + 1
        print(count)
        current = head
        temp = None

        if not head or not head.next: 
            return None
        else : 
            while mid <= count//2 - 1:
                    temp = current
                    current = current.next
                    mid = mid +1
            temp.next = current.next
        return head
            
        
        











        