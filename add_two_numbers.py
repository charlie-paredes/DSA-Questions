# class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #dummy head set to ListNode's first node
        dummy_head = ListNode(0)
        #current node keeps track of current node added to result list
        current_node = dummy_head
        carry = 0 # carry-over variable in case the sum is greater than 9

        while l1 is not None or l2 is not None:
            #adds vals from both lists, as well as the carry-over int
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            sum = val1 + val2 + carry

            #carry-over int is updated with the first digit of the sum if
            #the sum is greater than 9. for example, if sum is 18, carry is 1
            carry = sum // 10
            #next node is updated to have the remainder of sum/10, so if sum is
            #18, 8 is passed in, then we move on to the next node
            current_node.next = ListNode(sum % 10)
            current_node = current_node.next

            #if l1 and l2 are not empty, we move on the the next ones
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        #if after adding all elements of l1 and l2 there is still a carry int, we
        #make a new node and add it at the end
        if carry > 0:
            current_node.next = ListNode(carry)
     