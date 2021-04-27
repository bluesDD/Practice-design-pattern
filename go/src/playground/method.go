package main

import "fmt"

type Calc struct{ a1, a2 int }

func (p Calc) Add() int   { return p.a1 + p.a2 }
func (p Calc) Sub() int   { return p.a1 - p.a2 }
func (p Calc) Multi() int { return p.a1 * p.a2 }
func (p Calc) Div() int {
	if p.a2 == 0 {
		return 0
	}
	return p.a1 / p.a2
}

func main() {
	p := Calc{2, 3}
	fmt.Println(p.Add())
	fmt.Println(p.Sub())

	q := Calc{5, 10}
	fmt.Println(q.Div())

}
