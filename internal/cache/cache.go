package cache

import (
	"data-generator/internal/model"
	"errors"
	"math"
	"time"
)

var (
	errNotFound = errors.New("item not found")
)

type Cache struct {
	crypto map[string]*model.Currency
}

// New returns a new cache module.
func New(values ...model.Unit) *Cache {
	list := make(map[string]*model.Currency)

	for _, item := range values {
		list[item.Name] = &model.Currency{
			Value:       int64(item.Value),
			MarketValue: int64(item.Value),
			ROC:         0,
			UpdatedAt:   time.Now(),
		}
	}

	return &Cache{
		crypto: list,
	}
}

// Get an item by its name.
func (c *Cache) Get(name string) (int64, error) {
	if value, ok := c.crypto[name]; ok {
		return value.Value, nil
	}

	return 0, errNotFound
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
func (c *Cache) Update(name string, value int64) {
	item := c.crypto[name]

	item.Changes = append(item.Changes, model.History{
		Value: item.Value,
		Date:  item.UpdatedAt,
	})
	item.ROC = float64((value-item.Value)/item.Value) * 100
	item.UpdatedAt = time.Now()
	item.Value = value
	item.MarketValue = item.Changes[int(math.Max(float64(len(item.Changes)-10), 0))].Value
}
