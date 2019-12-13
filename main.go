package main
import "C"
import "fmt"
//export Sum
func Sum(a, b int) int {    return a + b
}

//export Test
//
func Test() int {    var s int
	for i := 0; i < 1000000; i++ {
		s += i}
	return s
}

func main() {
	fmt.Println(Test())
}