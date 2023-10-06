class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next
        
        length = len(arr)
        
        if n == length:
            temp = head
            head = head.next
            temp.next = None
            return head
        
        if n == 1:
            arr[length - 2].next = None

        temp = arr[length - n].next
        arr[(length-1)-n].next = temp

        return head
