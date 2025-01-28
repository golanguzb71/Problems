package main

import (
	"sort"
)

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
	var (
		resultArray []int
	)
	for list1 != nil {
		resultArray = append(resultArray, list1.Val)
		list1 = list1.Next
	}
	for list2 != nil {
		resultArray = append(resultArray, list2.Val)
		list2 = list2.Next
	}
	sort.Ints(resultArray)
	dummy := &ListNode{}
	current := dummy
	for _, num := range resultArray {
		current.Next = &ListNode{Val: num}
		current = current.Next
	}
	return dummy.Next
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
