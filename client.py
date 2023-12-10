import socket
import pyautogui

pyautogui.FAILSAFE = False
while True:
    print(socket.gethostbyname(socket.gethostname()))
    client = socket.socket()
    client.connect(("localhost", 12))
    list =  client.recv(1024).decode("utf-8").split()
    
    pyautogui.moveTo(int(list[0]), int(list[1]))
    print(list)
    client.close()
