import socket
import pyautogui as au
import multiprocessing as mu
from pynput.mouse import Listener
import threading

server = socket.socket()
server.bind(("localhost", 112))
server.listen(1200)
start_second_server = True
au.FAILSAFE = False
print(socket.gethostbyname(socket.gethostname()))
def send_mouse_clicked():
    while True:
        print("hello nati")
     
def send_mouse_location():
   while True:  
   
    client,InetAddress = server.accept()
    numbers = [x for x in range(1200)]
    x = au.position().x
    y = au.position().y
    st = str(x) + " " + str(y)
    
    client.send(bytes(st, "utf-8"))
    client.close()
    


parralel1 = mu.Process(target=send_mouse_location)
parralel2 = mu.Process(target=send_mouse_clicked)

parralel2.start()





   






