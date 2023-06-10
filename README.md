# Coinnews

![](https://img.shields.io/github/v/release/amirhnajafiz/coinnews?include_prereleases)
![](https://img.shields.io/badge/language-Go-9cf)
![](https://img.shields.io/badge/go--version-1.20-9cc)

Providing a data source for students of Cloud Computing course (Spring 2023).
With this application you can generate fake data for current rate of digital currencies.
All you have to is set the name and initial prices.

## Docker image

Make sure to use the image based on your runtime os architecture.

### linux

```shell
docker pull amirhossein21/coinnews.linux:v0.2
```

### macos

```shell
docker pull amirhossein21/coinnews.macos:v0.2
```

## Local

In order to set up the project on your local machine using ```Docker```, first create
a ```config.yml``` with the following content.

```yaml
http_port: 8000
worker_enable: true
worker_interval: 5
units:
  - name: bitcoin
    value: 500
  - name: docoin
    value: 230
```

After that use the following command to start the container:

### macos

```shell
docker run -d \
  --name coinnews-container \
  --mount type=bind,source="$(pwd)"/config.yml,target=/go/src/app/config.yml \
  -p 8000:8000 \
  amirhossein21/coinnews.macos:v0.2
```

### linux

```shell
docker run -d \
  --name coinnews-container \
  --mount type=bind,source="$(pwd)"/config.yml,target=/go/src/app/config.yml \
  --network host \
  amirhossein21/coinnews.linux:v0.2
```

Now you can access the api using ```localhost:8000```.

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

## Kubernetes

View all kubernetes manifests [here](kubernetes). Use the ```deploy.sh``` script to deploy all files.
