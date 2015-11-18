class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        orig = n
        self.i = n
        self.copy = n
        self.length = 0
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        else:
            self.length+=1
            node = self.removeNthFromEnd(head.next,n)
            if(node == None):
                self.copy-=1
                if(self.copy == self.length and self.next != None):
                    self.next = self.next.next
                    self.val = self.next.val
                elif(self.copy == self.length and self.next == None):
                    self.next =None
                    self.val = self.next.val
            else :
                return node
