from pynput import keyboard, mouse
from datetime import datetime
import json


# Class to record new macros
class Recorder:
    def __init__(self):
        self.events = []

    # Function to record keyboard events
    def on_key_press(self, key):
        try:
            self.events.append({'event': 'key_press', 'key': key.char, 'time': datetime.now().timestamp()})
        except AttributeError:
            self.events.append({'event': 'key_press', 'key': str(key), 'time': datetime.now().timestamp()})

    def on_key_release(self, key):
        self.events.append({'event': 'key_release', 'key': str(key), 'time': datetime.now().timestamp()})
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    # Function to record mouse events
    def on_click(self, x, y, button, pressed):
        self.events.append({
            'event': 'mouse_click',
            'button': str(button),
            'pressed': pressed,
            'position': (x, y),
            'time': datetime.now().timestamp()
        })

    def on_move(self, x, y):
        self.events.append({
            'event': 'mouse_move',
            'position': (x, y),
            'time': datetime.now().timestamp()
        })

    def on_scroll(self, x, y, dx, dy):
        self.events.append({
            'event': 'mouse_scroll',
            'position': (x, y),
            'scroll': (dx, dy),
            'time': datetime.now().timestamp()
        })

    # Start the listeners
    def start_listeners(self):
        with mouse.Listener(on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll) as mouse_listener, \
                keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release) as keyboard_listener:
            mouse_listener.join()
            keyboard_listener.join()

    # Save the recorded events to a file
    def save_events(self):
        with open('recorded_events.json', 'w') as f:
            json.dump(self.events, f, indent=4)
