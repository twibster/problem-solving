class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution: # fast solution but high memory usage O(n)
    def getIntersectionNode(self, headA,headB):
        currentA,currentB =headA,headB
        A=set() #sets are way faster than lists if they were used for checking the membership of elements
        while currentA:
            A.add(currentA)
            currentA = currentA.next
            
        while currentB:
            if currentB in A:
                return currentB
            currentB = currentB.next
        return None


class Solution: # not as fast but lower memory usage
    def getIntersectionNode(self, headA, headB):
        currentA,currentB =headA,headB
        len_a,len_b =0,0

        while currentA:
            len_a +=1
            currentA = currentA.next
            
        while currentB:
            len_b +=1
            currentB = currentB.next
            
        currentA,currentB =headA,headB
            
        diff =len_a - len_b
        if len_a >len_b:
            i=0
            while i < diff:
                currentA=currentA.next
                i+=1
        else:
            i=0
            while i <-diff:
                currentB =currentB.next
                i+=1
                
        while currentB != currentA:
            currentA =currentA.next
            currentB =currentB.next
            
        return currentA