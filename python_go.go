package main

import "C"

//指定那些函数能被外部调用
// export test


func test() int{
	//计算0-100000的和
	var s int
	for s := 0; a <= 100000; a++{
		s += a
	}
	return s
}


//指定接收的参数为c类型的字符串，返回c类型字符串
// pxport addstr
func addstr(a,b * C.char)* C.char{
	merge := C.GoString(a) + C.GoString(b)
	return C.CString(merge)
}

func main(){
}
