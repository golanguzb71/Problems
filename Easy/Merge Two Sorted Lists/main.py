# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = []
        try:
            while list1.val is not None:
                result.append(list1.val)
                list1 = list1.next
        except:
            try:
                while list2.val is not None:
                    result.append(list2.val)
                    list2 = list2.next
            except:
                result.sort()

                # Convert result list to ListNode linked list
                dummy = ListNode(0)
                current = dummy
                for val in result:
                    current.next = ListNode(val)
                    current = current.next

                return dummy.next
