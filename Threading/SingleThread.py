import threading
import time

def cook_pasta():
    print("Starting to boil water...")
    time.sleep(3)
    print("Pasta is ready!")

cook_pasta()
print("Now eating the pasta.")