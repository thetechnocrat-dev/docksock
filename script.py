import random
import time

messages = ["message 1", "message 2", "message 3", "message 4", "message 5", "message 6", "message 7", "message 8", "message 9", "message 10"]

for i in range(10):
    print(random.choice(messages))
    time.sleep(1)

