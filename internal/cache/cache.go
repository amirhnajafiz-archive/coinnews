package cache

import (
	"data-generator/internal/model"
	"errors"
)

var (
	errNotFound = errors.New("item not found")
)

type Cache struct {
	crypto map[string]*model.Unit
}

// New returns a new cache module.
func New(values ...model.Unit) *Cache {
	list := make(map[string]*model.Unit)

	for _, item := range values {
		list[item.Name] = &item
	}

	return &Cache{
		crypto: list,
	}
}

// Get an item by its name.
func (c *Cache) Get(name string) (*model.Unit, error) {
	if value, ok := c.crypto[name]; ok {
		return value, nil
	}

	return nil, errNotFound
}

// GetAllNames returns the map keys.
func (c *Cache) GetAllNames() []string {
	keys := make([]string, 0)

	for key := range c.crypto {
		keys = append(keys, key)
	}

	return keys
}

// Update item by setting a new value.
func (c *Cache) Update(name string, value int) {
	c.crypto[name].Value = value
}
