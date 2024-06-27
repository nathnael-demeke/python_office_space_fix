import socket
import pyautogui as au
import multiprocessing as mp
import threading
import time
from pynput.mouse import Listener as Mouse_Listener
from pynput.keyboard import Listener as Keyboard_Listener
from pynput.keyboard import Key
import asyncio
import json

mouse_event_client = None
client_address = None
try:
   config_file = open("settings.json","r")
   configurations = json.load(config_file)
   client_address = configurations["ClientAddress"]
   def detect_key_pressed():
      key_pressed_socket = socket.socket()
      key_pressed_socket.bind(("0.0.0.0", 10))
      key_pressed_socket.listen(13)
      cli, addr = key_pressed_socket.accept()
      def on_press(key):
         key_event = str(key).replace("'", "")
         cli.send(bytes(key_event,"utf-8"))
      with Keyboard_Listener(on_press=on_press) as listener:
         listener.join()
         print("keybooard")  

   def send_mouse_location():
      server = socket.socket()
      server.bind(("0.0.0.0", 20))
      server.listen(12)
      start_second_server = True
      au.FAILSAFE = False
      print(socket.gethostbyname(socket.gethostname()))

      while True:  
         client,InetAddress = server.accept()
         x = au.position().x
         y = au.position().y
         st = str(x) + " " + str(y)
         client.send(bytes(st, "utf-8"))  
         

   def send_mouse_event(message):
      server = socket.socket()  
      server.connect((client_address,100))
      server.send(bytes(message,"utf-8"))
      server.close()
   

   def click_parralel():
      def on_scroll(x,y,dx,dy):
         if dy > 0:
            send_mouse_event("scrollUp")
         else:
            send_mouse_event("scrollDown")
      def on_click(x, y, button, pressed):
         #I have noticed that the on_click function will run twice once for the if statmenet and one for else statment
         #My conclusion is if Pressed will make my code run a continous unwanted loop 
            if pressed:
               return False
            else:
               try:
                  send_mouse_event("clicked")
               except Exception as click_error:
                  print(click_error)
      while True:
         with Mouse_Listener(on_click=on_click,on_scroll=on_scroll) as listener:
            listener.join()
   if __name__ == '__main__':
      parralel_mouse_location = mp.Process(target=send_mouse_location)
      parralel_key_pressed = mp.Process(target=detect_key_pressed)
      parralel_mouse_click_listener = mp.Process(target=click_parralel)
      parralel_mouse_click_listener.start()
      parralel_mouse_location.start()
      parralel_key_pressed.start()
except Exception as e:  
   print("Please configure your settings at settings.json")
   print(e)