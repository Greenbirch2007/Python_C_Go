package main
import "C"
//  指定那些函数能被外部调用

//export test

func test() int{
	//计算0-10000的和
	var s int
	for s := 0; a<= 1000000; a++{
		s+=a
}
	return s
}

func main(){
}
