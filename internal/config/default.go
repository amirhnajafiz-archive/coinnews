package config

import (
	"data-generator/internal/model"
)

func Default() Config {
	return Config{
		HTTPPort:       8000,
		WorkerInterval: 2, // seconds
		WorkerEnable:   false,
		Units:          make([]model.Unit, 0),
	}
}
