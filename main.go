package main

import (
    "fmt"
    "time"
)

func main() {
    for i := 1; i <= 10; i++ {
        fmt.Printf("GoLang program calculating step %d out of 10\n", i)
        time.Sleep(time.Second)
    }
}

