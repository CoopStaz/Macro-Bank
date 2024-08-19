from pynput import keyboard, mouse
from datetime import datetime
import json
from threading import Thread
import time


class Recorder:
    def __init__(self):
        self.events = []
        self.listening = False

    # Function to record keyboard events
    def on_key_press(self, key):
        try:
            self.events.append({'event': 'key_press', 'key': key.char, 'time': datetime.now().timestamp()})
        except AttributeError:
            self.events.append({'event': 'key_press', 'key': str(key), 'time': datetime.now().timestamp()})

    def on_key_release(self, key):
        self.events.append({'event': 'key_release', 'key': str(key), 'time': datetime.now().timestamp()})
        if key == keyboard.Key.esc:
            print("ESC key pressed, stopping listener...")
            self.listening = False
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
        # TODO Add filter so that a mouse movement is only recorded if it surpasses a minimum distance
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
        print("Recording started. Press ESC to stop.")

        # Create new instances of the listeners
        mouse_listener = mouse.Listener(on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll)
        keyboard_listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)

        self.listening = True
        mouse_listener.start()
        keyboard_listener.start()

        keyboard_listener.join()  # Blocks until the keyboard listener is stopped (ESC pressed)
        mouse_listener.stop()     # Stop the mouse listener after keyboard listener stops

    # Save the recorded events to a file
    def save_events(self, name, map):
        with open(f'macros/{map}_macros.json', 'w') as f:
            json.dump({name: self.events}, f, indent=4)

    def load_events(self, filename='recorded_events.json'):
        with open(filename, 'r') as f:
            self.events = json.load(f)

    def replay_events(self):
        if not self.events:
            print("No events to replay. Please load or record events first.")
            return

        start_time = self.events[0]['time']

        for event in self.events:
            # Calculate the delay between events
            time.sleep(event['time'] - start_time)
            start_time = event['time']

            if event['event'] == 'key_press':
                key = event['key']
                if len(key) == 1:
                    keyboard.Controller().press(key)
                else:
                    keyboard.Controller().press(eval(f'keyboard.Key.{key.split(".")[1]}'))

            elif event['event'] == 'key_release':
                key = event['key']
                if len(key) == 1:
                    keyboard.Controller().release(key)
                else:
                    keyboard.Controller().release(eval(f'keyboard.Key.{key.split(".")[1]}'))

            elif event['event'] == 'mouse_click':
                x, y = event['position']
                button = eval(f'mouse.Button.{event["button"].split(".")[1]}')
                if event['pressed']:
                    mouse.Controller().press(button)
                else:
                    mouse.Controller().release(button)
                mouse.Controller().position = (x, y)

            elif event['event'] == 'mouse_move':
                x, y = event['position']
                mouse.Controller().position = (x, y)

            elif event['event'] == 'mouse_scroll':
                x, y = event['position']
                dx, dy = event['scroll']
                mouse.Controller().scroll(dx, dy)

    def record(self):
        if self.listening:
            print("Recording is already in progress.")
            return

        def run_listeners():
            try:
                print("The recording will start in: ")
                for i in reversed(range(6)):
                    print(f"{i} seconds...")
                    time.sleep(1)

                self.start_listeners()

            except KeyboardInterrupt:
                pass

            finally:
                self.save_events()
                print("Recording saved to 'recorded_events.json'")

        # Create and start a new thread for the listeners
        listener_thread = Thread(target=run_listeners)
        listener_thread.start()
