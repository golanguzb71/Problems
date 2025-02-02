package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	values := make([]int, 0)
	for head != nil {
		values = append(values, head.Val)
		head = head.Next
	}
	if len(values) == 0 {
		return nil
	}
	dummy := &ListNode{}
	current := dummy
	for i := len(values) - 1; i >= 0; i-- {
		current.Next = &ListNode{Val: values[i]}
		current = current.Next
	}
	return dummy.Next
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
