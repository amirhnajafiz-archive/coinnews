package handler

import (
	"data-generator/internal/http/response"

	"github.com/gofiber/fiber/v2"
)

type Handler struct {
	crypto map[string]int
}

func (h *Handler) GetData(ctx *fiber.Ctx) error {
	name := ctx.Params("name", "bitcoin")

	if value, ok := h.crypto[name]; ok {
		return ctx.Status(fiber.StatusOK).JSON(response.CryptoResponse{
			Type:  "",
			Name:  name,
			Value: value,
		})
	}

	return ctx.SendStatus(fiber.StatusNotFound)
}
