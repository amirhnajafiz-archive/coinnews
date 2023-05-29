# Data Generator

Providing a data source for students of Cloud Computing course (Spring 2023).
With this application you can generate fake data for current rate of digital currency.

## Docker

Use to following command to start the application on ```localhost:8000```:

```shell
docker compose up -d
```

## HAProxy

```shell
sudo systemctl restart haproxy
```

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
  "value": "500"
}
```
