package handler

import (
	"github.com/gofiber/fiber/v2"
	"strconv"
)

type Handler struct {
	crypto map[string]int
}

func (h *Handler) GetData(ctx *fiber.Ctx) error {
	name := ctx.Params("name", "bitcoin")

	if value, ok := h.crypto[name]; ok {
		return ctx.Status(fiber.StatusOK).SendString(strconv.Itoa(value))
	}

	return ctx.SendStatus(fiber.StatusNotFound)
}
