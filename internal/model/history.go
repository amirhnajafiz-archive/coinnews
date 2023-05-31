package model

import "time"

type History struct {
	Value int64     `json:"value"`
	Date  time.Time `json:"date"`
}
