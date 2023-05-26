FROM golang:1.20-alpine

WORKDIR src/app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build -o main

CMD ./main --config config.yml