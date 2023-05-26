package handler

import (
	"data-generator/internal/cache"
	"data-generator/internal/http/response"

	"github.com/gofiber/fiber/v2"
)

type Handler struct {
	Cache *cache.Cache
}

func (h *Handler) GetData(ctx *fiber.Ctx) error {
	name := ctx.Params("name", "bitcoin")

	if value, err := h.Cache.Get(name); err == nil {
		return ctx.Status(fiber.StatusOK).JSON(response.CryptoResponse{
			Type:  value.Type,
			Name:  value.Name,
			Value: value.Value,
		})
	}

	return ctx.SendStatus(fiber.StatusNotFound)
}
