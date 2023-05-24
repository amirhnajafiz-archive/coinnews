package cache

import (
	"errors"
)

var (
	errNotFound = errors.New("item not found")
)

type Cache struct {
	crypto map[string]int
}

// New returns a new cache module.
func New(values ...string) *Cache {
	list := make(map[string]int)

	for _, item := range values {
		list[item] = 0
	}

	return &Cache{
		crypto: list,
	}
}

// Get an item by it's name.
func (c *Cache) Get(name string) (int, error) {
	if value, ok := c.crypto[name]; ok {
		return value, nil
	}

	return 0, errNotFound
}
