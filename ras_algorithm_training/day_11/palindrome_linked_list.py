class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def isPalindrome(self, head):
        current =head
        nodes =[]
        while current:
            nodes.append(current.val)
            current =current.next
        return all([i ==nodes[(-idx)-1] for idx,i in enumerate(nodes)])