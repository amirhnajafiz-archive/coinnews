package worker

import (
	"log"
	"math"
	"math/rand"
	"time"

	"data-generator/internal/cache"
)

type Worker struct {
	Cache             *cache.Cache
	Interval          int
	ChangeProbability int
	ChangeFactor      int
}

func (w Worker) Do() {
	log.Println("worker started")

	names := w.Cache.GetAllNames()

	for {
		for _, name := range names {
			w.process(name)
		}

		time.Sleep(time.Duration(w.Interval) * time.Second)
	}
}

func (w Worker) process(name string) {
	value, _ := w.Cache.Get(name)

	delta := rand.Intn(w.ChangeFactor)
	if delta < w.ChangeProbability {
		value = value + int64(rand.Intn(w.ChangeFactor)-w.ChangeFactor/2)
		value = math.Max(value, 0)
	}

	w.Cache.Update(name, value)
}
