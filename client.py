import socket
import pyautogui

pyautogui.FAILSAFE = False
print(socket.gethostbyname(socket.gethostname()))
while True:
    client = socket.socket()
    client.connect(("192.168.1.10", 12))
    list =  client.recv(1024).decode("utf-8").split()
    # for word in list:
    #     if word == "yesItIsClicked":
    #         print("mouse click")
    pyautogui.moveTo(int(list[0]), int(list[1]))
    client.close()
