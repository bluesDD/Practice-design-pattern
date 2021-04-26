package main

import (
	"bufio"
	"fmt"
	"os"
)

func getArgs() []string {
	return os.Args[1:]
}

func getFile(filename string) {
	sf, err := os.Open(filename)
	if err != nil {
		os.Exit(1)
	}

	scanner := bufio.NewScanner(sf)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}
func main() {
	args := getArgs()
	// fmt.Println(args)
	for i := 0; i < len(args); i++ {
		getFile(args[i])

	}
}
