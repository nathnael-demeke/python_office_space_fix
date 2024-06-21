from pynput.mouse import Listener
def on_click(x, y, button, pressed):  
      if pressed:
            print("hello world")

with Listener(on_click=on_click) as listener:
               listener.join()   