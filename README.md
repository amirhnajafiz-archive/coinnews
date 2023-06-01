# Coinnews

Providing a data source for students of Cloud Computing course (Spring 2023).
With this application you can generate fake data for current rate of digital currency.

## API Documents

### get available currencies

#### request

```shell
url: [GET] /api/data
```

#### response

```json
["bitcoin", "dogecoin", "usdcoin"]
```

### get a single currency value

#### request

```shell
url: [GET] /api/data/{name | example: bitcoin}
```

#### response

```json
{
  "name": "bitcoin",
  "value": 499,
  "market_value": 499,
  "roc": -0.2,
  "updated_at": "2023-06-01T09:45:46.4501+03:30"
}
```

### get a single currency history

#### request

```shell
url: [GET] /api/data/{name | example: bitcoin}/history
```

#### response

```json
[
  {
    "value": 500,
    "date": "2023-06-01T09:56:25.220238+03:30"
  },
  {
    "value": 501,
    "date": "2023-06-01T09:56:25.220881+03:30"
  }
]
```