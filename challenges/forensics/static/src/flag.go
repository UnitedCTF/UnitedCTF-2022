package main

import (
  "fmt"
  "encoding/base64"
)

// We are using Go here since it builds a HUGE binary from nothing
func main() {
    // Add a bit of complexity to protect from strings
    data, err := base64.StdEncoding.DecodeString("$BASE64_FLAG")
    if err != nil {
      panic(err)
    }
    fmt.Println(string(data))
}
