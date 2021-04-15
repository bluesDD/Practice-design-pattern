package main

import (
	"io"
	"os"
)

func main() {
	f, err := os.Create("notes.txt")
	if err != nil {
		return
	}

	defer f.Close()

	if _, err = io.WriteString(f, "Learning Go!"); err != nil {
		return
	}

	f.Sync()
}
