class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next

        i, j = 0, len(arr) - 1
        while i < j:
            arr[i].next = arr[j]
            i += 1
            if i == j:
                break
            arr[j].next = arr[i]
            j -= 1
          
        arr[i].next = None

# Turn linked list into array, then use two pointers to reorder the list.