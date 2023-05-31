package model

import "time"

type Currency struct {
	Changes     []History
	MarketValue int64
	Value       int64
	ROC         float64
	UpdatedAt   time.Time
}
