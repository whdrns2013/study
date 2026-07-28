# sleeping.py
import time

with open("/workspace/src/data/name.txt", "r", encoding="utf-8") as f:
    name = f.readline()

print("Go to Sleep...")
time.sleep(20)
print(f"Wake Up!!!! my name is {name}!!")