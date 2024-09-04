# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mapper = {}
        result = Optional[ListNode]
        while head is not None:
            if mapper.get(head.val) is None:
                mapper[head.val] = True
            head = head.next

        dummy = ListNode(0)
        current = dummy
        for key in mapper.keys():
            current.next = ListNode(key)
            current = current.next
        return dummy.next


print(Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, None)))))
