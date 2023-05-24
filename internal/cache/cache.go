package cache

type Cache struct {
	crypto map[string]int
}

func New(values ...string) *Cache {
	list := make(map[string]int)

	for _, item := range values {
		list[item] = 0
	}

	return &Cache{
		crypto: list,
	}
}
