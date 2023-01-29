FROM golang:latest

WORKDIR /app

COPY main.go .

RUN go mod init main

RUN go build -o main .

CMD ["./main"]

