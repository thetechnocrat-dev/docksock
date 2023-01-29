# longsock
testing Python WebSockets within Docker Containers

```
docker build -t docksock-example .
python server.py

# in a new tab
python client.py
```

This example will stream server side longs both inside and outside the Docker container to the client.
