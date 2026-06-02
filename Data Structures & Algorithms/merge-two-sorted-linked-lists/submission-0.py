# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a starting node (dummy) to simplify edge cases.
        # 'tail' will always point to the last node in the merged list.
        dummy = ListNode(0)
        tail = dummy

        # While both input lists have nodes, pick the smaller current node
        # and append it to the merged list, advancing that list's pointer.
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1  # attach node from list1
                list1 = list1.next  # move forward in list1
            else:
                tail.next = list2  # attach node from list2
                list2 = list2.next  # move forward in list2
            tail = tail.next  # move the tail to the newly added node

        # One list may still have nodes left; attach the remainder.
        tail.next = list1 if list1 else list2
        # Return the merged list, skipping the dummy starter node.
        return dummy.next