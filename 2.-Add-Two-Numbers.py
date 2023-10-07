class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #turn the linked lists into lists of char
        curr1 = l1
        arr1 =[]
        while curr1:
            arr1.append(str(curr1.val))
            curr1 = curr1.next

        curr2 = l2
        arr2 = []
        while curr2:
            arr2.append(str(curr2.val))
            curr2 = curr2.next
        
        #reverse the lists
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]

        #join and turn to int then add and turn to str again so that we can reverse again
        one = int("".join(arr1))
        two = int("".join(arr2))
        ans = str(one + two)
        ans = ans[::-1]

        #turn str into linked list, turn the char into int while you are creating nodes 
        head = linked = ListNode(int(ans[0])) 

        for i in range(1,len(ans)):
            linked.next = ListNode(int(ans[i]))
            linked = linked.next
            
        return head 