class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
       self.head = None

    def get(self, index):
        current = self.head
        count =0
        while current:
            if count == index:
                return current.val
            prev=current
            current = current.next
            count += 1
        
        return -1
        
    def content(self):
        content = []
        current = self.head
        while current:
            content.append(current.val)
            current =current.next
        return content
    
    def length(self):
        current= self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def addAtHead(self, val):
        new= Node(val)
        new.next =self.head
        self.head = new
        return
        
    def addAtTail(self, val):
        new =Node(val)
        current = self.head
        if current is None:
            self.head = new
        else:
            while current.next:
                current = current.next
            current.next = Node(val)
        
    def addAtIndex(self, index, val):
        current =self.head
        count = 0
        length = self.length()
        if index == length:
            self.addAtTail(val)
            return
        elif index ==0:
            self.addAtHead(val)
            return
        elif index > length or index < 0:
            return
        
        while current:
            if count == index:
                temp = current
                current = Node(val)
                prev.next = current
                current.next =temp
                return
            prev = current
            current = current.next
            count += 1
            

    def deleteAtIndex(self, index):
        current =self.head
        count =0 
        if index ==0 :
            self.head =current.next
            current = None
            return
        while current:
            if index ==count:
                prev.next =current.next
                current = None
                return
                
            prev = current
            current =current.next
            count += 1