package config

import (
	"data-generator/internal/model"
)

func Default() Config {
	return Config{
		HTTPPort: 8000,
		Units:    make([]model.Unit, 0),
	}
}
