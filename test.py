import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    print(key)

def write_1():
    pass

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as l:
    l.join() 