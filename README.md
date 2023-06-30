# Coinnews

![](https://img.shields.io/github/v/release/amirhnajafiz/coinnews?include_prereleases)
![](https://img.shields.io/badge/language-Go-9cf)
![](https://img.shields.io/badge/go--version-1.20-9cc)

Providing a data source for students of Cloud Computing course (Spring 2023).
With this application you can generate fake data for current rate of digital currencies.
All you have to is set the name and initial prices, after that you can get your data
just by making some http calls.

Make sure to read the description carefully. ```Coinnews``` can be installed using ```docker```.
First try to run in on your local machine, after that use the kubernetes manifests in order
to set up the ```Coinnews``` on your kubernetes cluster.

## Docker image

Make sure to use the image based on your runtime os architecture.

### linux

```shell
docker pull amirhossein21/coinnews.linux:v0.2
```

### macos & windows

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

### macos & windows

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

Now you can access the api on ```localhost:8000```.

## API Documents

For reading information about how to use this api, visit ```localhost:8000``` or just
read the ```documents/swagger.yml``` file.

## Kubernetes

View all kubernetes manifests [here](kubernetes). Use these manifests in order
to set up ```coinnews``` cluster on Kubernetes. You don't need to use these manifests
exactly, you can make the changes that you like. This is just a base template.
