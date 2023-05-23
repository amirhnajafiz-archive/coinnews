package handler

import (
	"github.com/gofiber/fiber/v2"
)

type Handler struct {
	crypto map[string]int
}

func (h *Handler) GetData(ctx *fiber.Ctx) error {
	return ctx.SendStatus(fiber.StatusNotImplemented)
}
