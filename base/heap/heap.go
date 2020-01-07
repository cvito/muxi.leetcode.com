package heap

type myHeap []int

func New() *myHeap {
	return new(myHeap)
}

//min-heap
func (h *myHeap) Less(i, j int) bool {
	return (*h)[i] < (*h)[j]
}

func (h *myHeap) Swap(i, j int) {
	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}

func (h *myHeap) Len() int {
	return len(*h)
}

func (h *myHeap) Top() (v interface{}) {
	v = (*h)[0]
	return
}

func (h *myHeap) Pop() (v interface{}) {
	*h, v = (*h)[:h.Len()-1], (*h)[h.Len()-1]
	return
}

func (h *myHeap) PopFront() (v interface{}) {
	*h, v = (*h)[1:h.Len()], (*h)[0]
	return
}

func (h *myHeap) Push(v interface{}) {
	*h = append(*h, v.(int))
}
