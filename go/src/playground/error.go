package main

type Stringer interface {
	String() string
}

func ToStringer(v interface{}) (Stringer, error) {
	if s, ok := v.(Stringer); ok {
		return s, nil
	}
	return nil, MyError("CastError")
}

type MyError string

func (e MyError) Error() string {
	return string(e)
}
