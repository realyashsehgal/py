import time
import threading

count = 0
stop_thread = False

def timer():
    global count
    while not stop_thread:
        time.sleep(1)
        count += 1

x = threading.Thread(target=timer)
x.start()

y = int(input("Please enter 1 to exit this code: "))
if y == 1:
    stop_thread = True
    x.join()
    print(f"Oh man i took you {count} seconds damnn")
