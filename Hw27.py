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

# Вызов функций последовательно
red_light()
yellow_light()
green_light()