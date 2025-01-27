package main

import "fmt"

type stack []rune

func (s *stack) Push(ch rune) {
	*s = append(*s, ch)
}

func (s *stack) Pop() rune {
	if len(*s) == 0 {
		return 0
	}
	res := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return res
}

func isValid(s string) bool {
	newstack := stack{}

	for _, char := range s {
		if char == '(' || char == '[' || char == '{' {
			newstack.Push(char)
		} else {
			pop := newstack.Pop()
			if pop == 0 {
				return false
			}
			s2 := string(pop)
			s3 := string(char)
			if s2 == "(" {
				if s3 != ")" {
					return false
				}
			} else if s2 == "[" {
				if s3 != "]" {
					return false
				}
			} else if s2 == "{" {
				if s3 != "}" {
					return false
				}
			}
		}
	}

	return len(newstack) == 0
}

func main() {
	fmt.Println(isValid("(("))
}
