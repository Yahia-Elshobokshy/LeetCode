class Solution:
    def mergeKLists(self, head: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Creating a list from the given LinkNode
        new=[]
        for i in head:
            while(i):
                new.append(i.val)
                i = i.next

        # Sort the list and reverse it
        a=sorted(new,reverse=True)
    
        # Create a ListNode from list
        final=None
        for i in a:
            final=ListNode(i,final)
        return final
