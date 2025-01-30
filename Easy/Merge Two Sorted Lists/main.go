package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}

	var head, tail *ListNode

	for list1 != nil && list2 != nil {
		var node *ListNode
		if list1.Val < list2.Val {
			node = list1
			list1 = list1.Next
		} else {
			node = list2
			list2 = list2.Next
		}
		if head == nil {
			head = node
			tail = node
		} else {
			tail.Next = node
			tail = node
		}

		if list1 != nil {
			tail.Next = list1
		}
		if list2 != nil {
			tail.Next = list2
		}
	}
	return head
}

func main() {
	mergeTwoLists(&ListNode{
		Val:  1,
		Next: &ListNode{2, &ListNode{4, nil}},
	}, &ListNode{
		Val:  1,
		Next: &ListNode{3, &ListNode{4, nil}},
	})
}
