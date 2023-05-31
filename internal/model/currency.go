package model

import "time"

type Currency struct {
	Changes     []History `json:"changes"`
	MarketValue int64     `json:"market_value"`
	Value       int64     `json:"value"`
	ROC         float64   `json:"roc"`
	UpdatedAt   time.Time `json:"updated_at"`
}
