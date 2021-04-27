package main

import "fmt"

type Stringer interface {
	String() string
}

type I int

func (n I) String() string {
	return "I"

}

func F(s Stringer) {
	switch v := s.(type) {
	case I:
		fmt.Println(int(v), "I")
	}
}
