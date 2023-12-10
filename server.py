import socket
import pyautogui as au
import random

server = socket.socket()
server.bind(("localhost", 12))
server.listen(1200)
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


