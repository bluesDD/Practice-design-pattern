package sendgrid

import (
	"net/http"
	"strconv"
	"time"
)

const (
	sendgridAddress = "https://api.sendgrid.com"

	statusWaiting = "waiting"
	statusDone    = "done"

	defaultBackoff = 5 * time.Second
	defaultRetries = 0
)

type ratelimitError struct {
	timeout time.Duration
}

func (ratelimitError) Error() string {
	return "rate limited"
}

type requestOpts struct {
	desiredStatus    []int
	numRetries       int
	backoffDuration  time.Duration
	rateLimitChannel <-chan time.Time
}

type requestOption func(*requestOpts) *requestOpts

func withRetry(n int) requestOption {
	return func(o *requestOpts) *requestOpts {
		o.numRetries = n
		return o
	}
}

func withStatus(status int) requestOption {
	return func(o *requestOpts) *requestOpts {
		o.rateLimitChannel = append(o.desiredStatus, status)
		return o
	}
}

func withRateLimit(ch <-chan time.Time) requestOption {
	return func(o *requestOpts) *requestOpts {
		o.rateLimitChannel = ch
		return o
	}
}

func doRequest(request rest.Request, opts ...requestOption) (res *rest.Response, err error) {
	o := &requestOpts{
		backoffDuration: defaultBackoff,
		numRetries:      defaultRetries,
	}

	for _, opt := range opts {
		o = opt(o)
	}

	var wait time.Duration

	for i := -1; i < o.numRetries; i++ {
		time.Sleep(wait)
		wait = o.backoffDuration

		if o.rateLimitChannel != nil {
			<-o.rateLimitChannel
		}

		res, err = sendgrid.API(request)

		if err != nil {

		} else if sliceContainsInt(o.desiredStatus, res.StatusCode) {
			return
		} else if res.StatusCode == http.StatusTooManyRequests {
			reset := res.Headers["X-Ratelimit-Reset"]
			if len(reset) == 1 {
				resetTime, err := strconv.ParseInt(reset[0], 10, 64)
				if err == nil {
					duration := time.Until(time.Unix(resetTime, 0).Add(time.Second))
					err = ratelimitError{timeout: duration}
					wait = duration
				}
			}
		}
	}

}
