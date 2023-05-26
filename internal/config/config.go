package config

import (
	"data-generator/internal/model"
	"log"

	"github.com/knadh/koanf/parsers/yaml"
	"github.com/knadh/koanf/providers/file"
	"github.com/knadh/koanf/providers/structs"
	"github.com/knadh/koanf/v2"
)

type Config struct {
	HTTPPort int          `koanf:"http_port"`
	Units    []model.Unit `koanf:"units"`
}

func Load(path string) Config {
	var instance Config

	k := koanf.New(".")

	if err := k.Load(structs.Provider(Default(), "koanf"), nil); err != nil {
		log.Fatalf("error loading default: %s", err)
	}

	if err := k.Load(file.Provider(path), yaml.Parser()); err != nil {
		log.Printf("error loading %s: %s", path, err)
	}

	if err := k.Unmarshal("", &instance); err != nil {
		log.Fatalf("error unmarshalling config: %s", err)
	}

	return instance
}
