import socket
import pyautogui as au
import multiprocessing as mu
from pynput.mouse import Listener
import threading

# def do_something(sock):
#    sock.send(bytes("yes", "utf-8"))
send = False
def do_something(socket):
   socket.send(bytes("yes", "utf-8"))
def send_mouse_clicked():  
  mouse_event_socket = socket.socket()
  mouse_event_socket.bind(("localhost",110))
  mouse_event_socket.listen(12) 
  cli, addr = mouse_event_socket.accept() 
  def on_click(x, y, button, pressed):  
    global send
    send = send
    if pressed:
            # cli.send(bytes("yes", "utf-8")) 
            if send == False:
               do_something(cli)
               print("sent")
               send = True
            
            elif send == True:
                  send = False
                  

           


  with Listener(on_click=on_click) as listener:
        listener.join()   
def send_mouse_location():
   server = socket.socket()
   server.bind(("localhost", 112))
   server.listen(1200)
   start_second_server = True
   au.FAILSAFE = False
   print(socket.gethostbyname(socket.gethostname()))

   while True:  
   
    client,InetAddress = server.accept()
    numbers = [x for x in range(1200)]
    x = au.position().x
    y = au.position().y
    st = str(x) + " " + str(y)
    
    client.send(bytes(st, "utf-8"))
    client.close()
    

if __name__ == '__main__':
  parralel_mouse_event = mu.Process(target=send_mouse_clicked)
  parralel_mouse_location = mu.Process(target=send_mouse_location)
  parralel_mouse_location.start()
  parralel_mouse_event.start()

