package sum

import "C"

// asottile:
// The comment below is necessary for "exporting" a function to C
// comments as code +-
// Also it cannot be "// export Sum". yay.

//export Sum
func Sum(a, b int) int {
	return a + b
}

func main() {}
