# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        current= head
        prev =ListNode(0)
        prev.next =head
        record = prev
        while current:
            next =current.next
            if current.val ==val:
                prev.next =next
                current=next
            else:
                prev=current
                current =next
        return record.next
            
        