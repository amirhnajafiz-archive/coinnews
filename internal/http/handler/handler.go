package handler

import (
	"data-generator/internal/cache"
	"data-generator/internal/http/response"
	"log"

	"github.com/gofiber/fiber/v2"
)

type Handler struct {
	Cache *cache.Cache
}

func (h *Handler) GetAvailable(ctx *fiber.Ctx) error {
	return ctx.Status(fiber.StatusOK).JSON(h.Cache.GetAllNames())
}

func (h *Handler) GetData(ctx *fiber.Ctx) error {
	name := ctx.Params("name", "bitcoin")

	log.Printf("request for: %s\n", name)

	if value, err := h.Cache.Get(name); err == nil {
		return ctx.Status(fiber.StatusOK).JSON(response.CryptoResponse{
			Name:  name,
			Value: value,
		})
	}

	return ctx.SendStatus(fiber.StatusNotFound)
}
