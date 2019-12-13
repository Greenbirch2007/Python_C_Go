package main

// #include<stdlib.h>

import "C"
import "unsafe"


//export Concat


func Concat(str1,str2 *C.char) *C.char{
	goStr1 :=C.GoString(str1)
	goStr2 :=C.GoString(str2)

	concatStr := goStr1 + goStr2


	//return cgo string
	cStr := C.CString(concatStr)
	defer C.free(unsafe.Pointer(cStr))

	return cStr
}


func main(){}



