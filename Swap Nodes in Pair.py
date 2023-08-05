class Solution:
    def swapPairs(self, head):

        if not(head and head.next): return head 

        newHead = head.next
        head.next, newHead.next = self.swapPairs(head.next.next), head

        return newHead
