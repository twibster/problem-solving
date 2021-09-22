# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        length=self.length(head)
        if length %2 ==0:
            return self.get(length/2,head)
        else:
            return self.get(length//2,head)
    
    def get(self,index,head):
        curr = head
        for _ in range(index):
            curr = curr.next

        return curr
    
    def length(self,head):
        curr = head
        size =0
        while  curr:
            curr = curr.next
            size += 1
        return size
        