package config

import (
	"data-generator/internal/model"
)

func Default() Config {
	return Config{
		HTTPPort:          8000,
		WorkerInterval:    5, // seconds
		WorkerEnable:      false,
		ChangeProbability: 5,
		ChangeFactor:      10,
		Units:             make([]model.Unit, 0),
	}
}
