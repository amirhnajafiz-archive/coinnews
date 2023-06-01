package response

import "time"

type CryptoResponse struct {
	Name        string    `json:"name"`
	Value       int       `json:"value"`
	MarketValue int       `json:"market_value"`
	ROC         float64   `json:"roc"`
	UpdatedAt   time.Time `json:"updated_at"`
}
