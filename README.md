# DockSock
Testing Python WebSocket isomorphic logging within Docker Containers

```
docker build -t docksock-example .
python server.py

# in a new tab
python client.py
```

This example realtime streams server side logs (both inside and outside the Docker container) to the client.

Much help from from this [post](https://www.reddit.com/r/learnpython/comments/wrathb/streaming_stdoutin_realtimeto_a_client_from_a/)

![ezgif com-gif-maker](https://user-images.githubusercontent.com/9427089/215359057-4cfd168b-8c47-4cf2-9c6f-5f0071a348a5.gif)

