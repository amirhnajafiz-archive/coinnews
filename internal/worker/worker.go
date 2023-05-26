package worker

import (
	"math/rand"
	"time"

	"data-generator/internal/cache"
)

type Worker struct {
	Cache    *cache.Cache
	Interval int
}

func (w *Worker) Do() {
	names := w.Cache.GetAllNames()

	for {
		for _, name := range names {
			w.process(name)
		}

		time.Sleep(time.Duration(w.Interval) * time.Millisecond)
	}
}

func (w *Worker) process(name string) {
	value, _ := w.Cache.Get(name)

	delta := rand.Int() % 5
	if delta == 0 || delta == 3 {
		value -= 1
	} else if delta == 1 || delta == 2 {
		value += 1
	}

	w.Cache.Update(name, delta)
}
