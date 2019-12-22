package link

type ListNode struct {
	Val int
	Next *ListNode
}

func GenLinkList(input []int) *ListNode {
	if len(input) == 0 {
		return nil
	}

	listNode := &ListNode{}
	for i, v := range input {
		newNode := &ListNode{}
		newNode.Val = v
		tmpl := listNode
		for j := 0; j < i; j++ {
			if tmpl.Next == nil {
				tmpl.Next = &ListNode{}
			}
			tmpl = tmpl.Next
		}
		*tmpl = *newNode
	}
	return listNode
}