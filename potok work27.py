import threading
import time

def red_light():
    print("Red light")
    time.sleep(5)

def yellow_light():
    print("Yellow light")
    time.sleep(2)

def green_light():
    print("Green light")
    time.sleep(3)

red_thread = threading.Thread(target=red_light)
yellow_thread = threading.Thread(target=yellow_light)
green_thread = threading.Thread(target=green_light)

red_thread.start()
yellow_thread.start()
green_thread.start()

red_thread.join()
yellow_thread.join()