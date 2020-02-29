# Simple demonstration of multithreading

import threading, time
print("Start of the program")

def sleep():
    time.sleep(5)
    print("Wake up!")

thread_obj = threading.Thread(target=sleep)
thread_obj.start()

print('End of the program')