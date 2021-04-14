package main

import "fmt"

func location(city string) (string, string) {
	var region string
	var continent string
	switch city {
	case "Delhi", "Hyberad", "Mumbai":
		region, continent = "India", "Asia"
	case "Irvine", "Los Angeles", "SanDiego":
		region, continent = "California", "USA"
	}
	return region, continent
}

func main() {
	region, continent := location("Irvine")
	fmt.Printf("John works in %s, %s \n", region, continent)
}
