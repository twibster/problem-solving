class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        '''this removes any duplicated nodes neglecting any order'''
        current = head
        list=[]
        while current:
            list.append(current.val)
            current = current.next
        current =head
        previous=None
        while current:
            if list.count(current.val) >1 and previous:
                previous.next =current.next
                list.remove(current.val)
                current=current.next
            else:
                previous =current
                current=current.next
        return head

    def deleteDuplicates(self, head):
        '''this does the same but the nodes must be in ascending order'''
        current = head
        while current:
            while current.next and current.val==current.next.val:
                current.next = current.next.next
            current=current.next
        return head
            
            
        
        
            