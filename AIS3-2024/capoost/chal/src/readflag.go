package main

import (
    "fmt"
    "os"
    "log"
    "strings"
    "syscall"
)

func main() {
    err := syscall.Setuid(syscall.Geteuid())
    if err != nil {
        log.Fatalln(err)
    }
    flag, err := os.ReadFile("/fl4g1337")
    if err != nil {
        log.Fatalln(err)
    }
    fmt.Println(strings.Trim(string(flag), " \n\t"))
}
