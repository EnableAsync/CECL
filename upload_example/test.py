import sys
import time

print("test")
for i in range(1, 6):
    print(i)
    print(i + 1)
    time.sleep(1)

print("hello cecl")
sys.stdout.flush()
