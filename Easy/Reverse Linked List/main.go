package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var (
		prev *ListNode
		next *ListNode
		curr = head
	)
	for curr != nil {
		next = curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	return prev
}

func main() {
	reverseList(&ListNode{
		Val: 10,
		Next: &ListNode{
			11,
			&ListNode{
				Val:  34,
				Next: nil,
			},
		},
	})
}
