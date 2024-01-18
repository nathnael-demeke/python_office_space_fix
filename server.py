import socket
import pyautogui as au
import multiprocessing as mp
from pynput.mouse import Listener
from pynput.keyboard import Key,Listener
import threading


tab_pressed = False

def do_something(socket, message):
   socket.send(bytes(message, "utf-8"))
def detect_key_pressed():

   key_pressed_socket = socket.socket()
   key_pressed_socket.bind(("0.0.0.0", 10))
   key_pressed_socket.listen(13)
   cli, addr = key_pressed_socket.accept()
   def on_press(key):
      global tab_pressed
      tab_pressed = tab_pressed 
      if key == Key.tab:
         tab_pressed = True if tab_pressed == False else False
         print(tab_pressed)
      else:
         cli.send(bytes("{0}".format(key),"utf-8"))

         print('{0} pressed'.format(key))
   with Listener(on_press=on_press) as listener:
    listener.join()

def send_mouse_clicked():  
   send = False
   mouse_event_socket = socket.socket()
   mouse_event_socket.bind(("0.0.0.0",80))
   mouse_event_socket.listen(12) 
   cli, addr = mouse_event_socket.accept() 
   def on_click(x, y, button, pressed):  
      global send
      send = send
      if pressed:
            if tab_pressed == True:
               # cli.send(bytes("yes", "utf-8")) 
               if send == False:
                  do_something(cli, "yes")
                  send = True
               
               elif send == True:
               
                     send = False
   with Listener(on_click=on_click) as listener:
        listener.join()   
def send_mouse_location():
   server = socket.socket()
   server.bind(("0.0.0.0", 20))
   server.listen(1200)
   start_second_server = True
   au.FAILSAFE = False
   print(socket.gethostbyname(socket.gethostname()))

   while True:  
    client,InetAddress = server.accept()
    x = au.position().x
    y = au.position().y
    st = str(x) + " " + str(y)
    
    client.send(bytes(st, "utf-8"))
    client.close()
    

if __name__ == '__main__':
  parralel_mouse_event = mp.Process(target=send_mouse_clicked)
  parralel_mouse_location = mp.Process(target=send_mouse_location)
  parralel_key_pressed = mp.Process(target=detect_key_pressed)
  parralel_mouse_event.start()
  parralel_mouse_location.start()
  parralel_key_pressed.start()

