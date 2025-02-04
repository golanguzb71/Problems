package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	checkerMapS := make(map[string]int)
	checkerMapT := make(map[string]int)
	for i := range s {
		checkerMapS[string(rune(t[i]))] = checkerMapS[string(rune(t[i]))] + 1
		checkerMapT[string(rune(s[i]))] = checkerMapT[string(rune(s[i]))] + 1
	}
	for _, harf := range s {
		if checkerMapT[string(harf)] != checkerMapS[string(harf)] {
			return false
		}
	}
	return true
}

func main() {
	print(isAnagram("anagram", "nagaram"))
}
