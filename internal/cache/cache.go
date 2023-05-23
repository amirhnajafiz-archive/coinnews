package cache

type Cache struct {
	crypto map[string]int
}

func New() *Cache {
	return &Cache{
		crypto: make(map[string]int),
	}
}

func (c *Cache) InitValues(values ...string) {
	for _, item := range values {
		c.crypto[item] = 0
	}
}
