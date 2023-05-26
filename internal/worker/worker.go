package worker

import (
	"data-generator/internal/cache"
	"time"
)

type Worker struct {
	Cache    *cache.Cache
	Interval int
}

func (w *Worker) Do() {
	for {
		time.Sleep(time.Duration(w.Interval) * time.Millisecond)
	}
}
