package main

import (
	"data-generator/internal/cache"
	"data-generator/internal/config"
	"data-generator/internal/http/handler"
	"data-generator/internal/worker"
	"flag"
	"fmt"
	"log"

	"github.com/gofiber/fiber/v2"
)

func main() {
	var (
		ConfigFile = flag.String("config", "config.yml", "Config file path")
	)

	// parse flags
	flag.Parse()

	// read configs
	cfg := config.Load(*ConfigFile)

	// create cache
	c := cache.New(cfg.Units...)

	// init worker
	go worker.Worker{
		Cache: c,
	}.Do()

	// create handler
	h := handler.Handler{
		Cache: c,
	}

	// create a new fiber app
	app := fiber.New()

	app.Get("/api/data/:name", h.GetData)
	app.Get("/api/data", h.GetAvailable)

	if err := app.Listen(fmt.Sprintf(":%d", cfg.HTTPPort)); err != nil {
		log.Fatal(err)
	}
}
